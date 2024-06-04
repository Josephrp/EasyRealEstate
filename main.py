# main.py
from src.config.config import llm_config
import sys
from src.agents.agents import planner , finance_agent , code_writer_agent , code_executor_agent, user_proxy
from src.prompts.prompts import task
import autogen
from dotenv import load_dotenv
import os
from src.memory.mem import Upsert, retrieve_query
from autogen.cache import Cache

load_dotenv('./src/config/.env')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def main():
    
    # Initialize upsert to load data into ChromaDB
    upsert_instance = Upsert(file_path='./src/sources/LISTINGS.xlsx')
    # upsert_instance.upsert_documents()

    intro_message = "Speak to EasyRealEstate by stating your Italian real estate expectations. For example, the region, size of investment, and any other details: "
    user_input = input(intro_message)
    
    message = user_input + "\n\n" + task
    
    groupchat = autogen.GroupChat(
        agents=[user_proxy, finance_agent, code_writer_agent, code_executor_agent, planner],
        messages=[],
        max_round=12,
    )
    
    manager = autogen.GroupChatManager(
        groupchat=groupchat, llm_config=llm_config
    )

    with Cache.disk() as cache:    
        groupchat_result = user_proxy.initiate_chat(
            manager,
            message=message,
        )
    
    # You can handle the groupchat_result here if needed
    print(groupchat_result)

if __name__ == "__main__":
    main()