# main.py
from src.config.config import llm_config
from src.agents.agents import planner , finance_agent , user_proxy, ragproxyagent, real_estate_listing_agent
from src.prompts.prompts import task, manager_system_message, intro_message
import autogen
from autogen.cache import Cache
from autogen import GroupChatManager
from src.config.config import load_env_file
import os
import sys


def main():
    
    load_env_file('./src/config/.env')

    user_input = input(intro_message)
    
    message = user_input + "\n\n" + task
    
    groupchat = autogen.GroupChat(
        agents=[planner,  finance_agent , ragproxyagent, user_proxy , real_estate_listing_agent],
        messages=[],
        max_round=12,

    allowed_or_disallowed_speaker_transitions={
        planner: [user_proxy, ragproxyagent, finance_agent],
        user_proxy: [finance_agent, ragproxyagent, planner],
        ragproxyagent: [real_estate_listing_agent, planner, user_proxy],
        real_estate_listing_agent: [ragproxyagent, user_proxy],
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