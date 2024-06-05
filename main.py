# main.py
from src.config.config import llm_config
import src.agents.agents
from src.agents.agents import planner , finance_agent , user_proxy, ragproxyagent, retrieve_content
from src.prompts.prompts import task, manager_system_message, intro_message
import autogen
from autogen.cache import Cache
from autogen import GroupChatManager
from pathlib import Path
from dotenv import load_dotenv

def main():
    dotenv_path = Path('./src/config/.env')
    load_dotenv(dotenv_path=dotenv_path)

    user_input = input(intro_message)
    
    message = user_input + "\n\n" + task
    
    # for caller in [planner, finance_agent, user_proxy]:
    #     d_retrieve_content = caller.register_for_llm(
    #         description="retrieve content for code generation and question answering.", api_style="function"
    #     )(retrieve_content)
    # for executor in [planner, finance_agent, user_proxy]:
    #     executor.register_for_execution()(d_retrieve_content)

    groupchat = autogen.GroupChat(
        agents=[planner,  finance_agent , ragproxyagent, user_proxy],
        messages=[],
        max_round=12,

    allowed_or_disallowed_speaker_transitions={
        planner: [user_proxy, ragproxyagent, finance_agent],
        user_proxy: [finance_agent, ragproxyagent, planner],
        ragproxyagent: [finance_agent, planner, user_proxy],
        # real_estate_listing_agent: [ragproxyagent, user_proxy],
        finance_agent: [ragproxyagent, planner],
    },
    speaker_transitions_type="allowed",
    )
    
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config, system_message=manager_system_message)

    with Cache.disk() as cache:    
        groupchat_result = user_proxy.initiate_chat(manager, message=message,)
    
    # You can handle the groupchat_result here if needed
    print(groupchat_result)

if __name__ == "__main__":
    main()