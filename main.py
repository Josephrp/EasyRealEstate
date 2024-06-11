# main.py  
  
import autogen  
from autogen.cache import Cache
from autogen import ConversableAgent, AssistantAgent, GroupChat, GroupChatManager  
from autogen.coding import LocalCommandLineCodeExecutor  
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent  
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent  
import chromadb  
from typing_extensions import Annotated  
import os  
# import streamlit as st  
from src.config.config import load_env_file, llm_config  
from src.prompts.prompts import task, manager_system_message, intro_message, finance_agent_system_message, planner_system_message  
  
# Load environment variables  
load_env_file('./src/config/.env')  
  
# Initialize chromadb client  
chroma_client = chromadb.HttpClient(host='localhost', port=8000)  
  
# Executor configuration  
executor = LocalCommandLineCodeExecutor(  
    timeout=3600,  
    work_dir="./src/codex",  
)  
  
# Agent configurations  
finance_agent = ConversableAgent(  
    name="finance_agent",  
    system_message=finance_agent_system_message,  
    llm_config=llm_config,  
    code_execution_config={"executor": executor},  
    human_input_mode="NEVER",  
)  
  
ragproxyagent = RetrieveUserProxyAgent(  
    name="italian_real_estate_listings",  
    human_input_mode="NEVER",  
    retrieve_config={  
        "task": "default",  
        "docs_path": "./src/sources/LISTINGS.csv",  
        "chunk_token_size": 1400,  
        "model": "gpt-4o",  
        "chunk_mode": "one_line",  
        "vector_db": chroma_client,  
        "embedding_model": "all-mpnet-base-v2",  
        "collection_name": "italianrealestate",  
        "get_or_create": True,  
    },  
)  
  
user_proxy = ConversableAgent(  
    name="Admin",  
    system_message="Give the task, and send instructions to planner to define the real-estate investment strategy",  
    llm_config=llm_config,  
    human_input_mode="TERMINATE",  
    code_execution_config={"executor": executor},  
)  
  
planner = ConversableAgent(  
    name="Planner",  
    system_message=planner_system_message,  
    description="Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps",  
    llm_config=llm_config,  
    code_execution_config={"executor": executor},  
)  
  
# Function to reset agents  
def _reset_agents():  
    finance_agent.reset()  
    ragproxyagent.reset()  
    user_proxy.reset()  
    planner.reset()  
  
# Function to retrieve content  
def retrieve_content(  
    message: Annotated[str, "Refined message which keeps the original meaning and can be used to retrieve content for code generation and question answering."],  
    n_results: Annotated[int, "number of results"] = 5,  
) -> str:  
    ragproxyagent.n_results = n_results  
    update_context_case1, update_context_case2 = ragproxyagent._check_update_context(message)  
    if (update_context_case1 or update_context_case2) and ragproxyagent.update_context:  
        ragproxyagent.problem = message if not hasattr(ragproxyagent, "problem") else ragproxyagent.problem  
        _, ret_msg = ragproxyagent._generate_retrieve_user_reply(message)  
    else:  
        _context = {"problem": message, "n_results": n_results}  
        ret_msg = ragproxyagent.message_generator(ragproxyagent, None, _context)  
    return ret_msg if ret_msg else message  
  
# Register functions for execution and LLM  
@finance_agent.register_for_execution()  
@user_proxy.register_for_execution()  
@planner.register_for_execution()  
@finance_agent.register_for_llm(description="Italian Real Estate Listings")  
@planner.register_for_llm(description="Italian Real Estate Listings")  
@user_proxy.register_for_llm(description="Italian Real Estate Listings")  
def retrieve_content_wrapper(message: str, n_results: int = 5) -> str:  
    return retrieve_content(message, n_results)  
  
# Main function  
def main():  
    _reset_agents()  
    user_input = input(intro_message)  
    message = user_input + "\n\n" + task  
  
    groupchat = GroupChat(  
        agents=[planner, finance_agent, ragproxyagent, user_proxy],  
        messages=[],  
        max_round=12,  
        allowed_or_disallowed_speaker_transitions={  
            planner: [user_proxy, ragproxyagent, finance_agent],  
            user_proxy: [finance_agent, ragproxyagent, planner],  
            ragproxyagent: [finance_agent, planner, user_proxy],  
            finance_agent: [ragproxyagent, planner],  
        },  
        speaker_transitions_type="allowed",  
    )  
  
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config, system_message=manager_system_message)  
    with Cache.disk() as cache:  
        groupchat_result = user_proxy.initiate_chat(manager, message=message)  
    print(groupchat_result)  
  
if __name__ == "__main__":  
    main()  
