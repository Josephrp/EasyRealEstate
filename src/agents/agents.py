# ./src/agents/agents

import autogen
from autogen import ConversableAgent, AssistantAgent
from autogen.coding import LocalCommandLineCodeExecutor
from src.config.config import llm_config
from src.prompts.prompts import finance_agent_system_message, planner_system_message, retrieve_assistant_system_message
from autogen.cache import Cache
# import openbb
from openbb_agents.agent import openbb_agent
# import os
# from dotenv import load_dotenv
# from src.memory.mem import Upsert, Retriever
from autogen.cache import Cache
from src.config.config import llm_config
import chromadb
# import pandas as pd
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import chromadb
from typing import Annotated
from src.config.config import load_env_file


load_env_file('./src/config/.env')

chroma_client = chromadb.HttpClient(host='localhost', port=8000)


executor = LocalCommandLineCodeExecutor(
    timeout=3600,
    work_dir="./src/codex",
    # functions=[italianhousing, openbb, get_stock_prices, plot_stock_prices],
)

# RetrieveUserProxyAgent instance named "ragproxyagent"
ragproxyagent = RetrieveUserProxyAgent(
    name="italian_real_estate_listings",
    human_input_mode="NEVER",
    # max_consecutive_auto_reply=10,
    retrieve_config={
        "task": "default",
        "docs_path": "./src/sources/LISTINGS.csv",
        "chunk_token_size": 1350,
        "model": "gpt-4o",
        "chunk_mode" : "one_line",
        "vector_db" : chroma_client,
        # "client": chroma_client,
        "embedding_model": "all-mpnet-base-v2",
        "collection_name": "italianrealestate",
        "get_or_create": True,
        # "overwrite" : True,
    },
)

user_proxy = ConversableAgent(
    name="Admin",
    system_message="Give the task, and send "
    "instructions to planner to define the real-estate investment strategy",
    # code_execution_config=False,
    llm_config=llm_config,
    human_input_mode="TERMINATE",
    code_execution_config={"executor": executor},
)

planner = ConversableAgent(
    name="Planner",
    system_message=planner_system_message,
    description="Planner. Given a task, determine what "
    "information is needed to complete the task. "
    "After each step is done by others, check the progress and "
    "instruct the remaining steps",
    llm_config=llm_config,
    code_execution_config={"executor": executor},
)


@finance_agent.register_for_execution()
@finance_agent.register_for_llm(description="Financial and market information")
def openbb(query: str) -> str:
    """get macroeconomic and real time market information
    Args :
        query (str) : a plain text question about markets or macroeconomics 
    Returns : 
        result (str) : a plain text analysis based on the query
    """
    result = openbb_agent(query)
    return result

@finance_agent.register_for_execution()
@user_proxy.register_for_execution()
@planner.register_for_execution()
@finance_agent.register_for_llm(description="Italian Real Estate Listings")
@planner.register_for_llm(description="Italian Real Estate Listings")
@user_proxy.register_for_llm(description="Italian Real Estate Listings")
def retrieve_content(
    message: Annotated[ str, "Refined message which keeps the original meaning and can be used to retrieve content for code generation and question answering.",],    n_results: Annotated[int, "number of results"] = 5,) -> str:
    ragproxyagent.n_results = n_results  # Set the number of results to be retrieved.
    # Check if we need to update the context.
    update_context_case1, update_context_case2 = ragproxyagent._check_update_context(message)
    if (update_context_case1 or update_context_case2) and ragproxyagent.update_context:
        ragproxyagent.problem = message if not hasattr(ragproxyagent, "problem") else ragproxyagent.problem
        _, ret_msg = ragproxyagent._generate_retrieve_user_reply(message)
    else:
        _context = {"problem": message, "n_results": n_results}
        ret_msg = ragproxyagent.message_generator(ragproxyagent, None, _context)
    return ret_msg if ret_msg else message