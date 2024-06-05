# ./src/agents/agents

import autogen
from autogen import ConversableAgent, AssistantAgent
from autogen.coding import LocalCommandLineCodeExecutor
from src.config.config import llm_config
from src.prompts.prompts import finance_agent_system_message, planner_system_message, retrieve_assistant_system_message
from autogen.cache import Cache
# import openbb
from openbb_agents.agent import openbb_agent
import os
from dotenv import load_dotenv
# from src.memory.mem import Upsert, Retriever
from autogen.cache import Cache
from src.config.config import llm_config
import chromadb
import pandas as pd
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import chromadb


chroma_client = chromadb.HttpClient(host='localhost', port=8000, database="./src/memory")

# RetrieveAssistantAgent instance named "assistant"
real_estate_listing_agent = RetrieveAssistantAgent(
    name="real_estate_listing_agent", 
    system_message=retrieve_assistant_system_message,
    llm_config=llm_config,
)

# RetrieveUserProxyAgent instance named "ragproxyagent"
ragproxyagent = RetrieveUserProxyAgent(
    name="italian_realestate_listings",
    human_input_mode="NEVER",
    # max_consecutive_auto_reply=10,
    retrieve_config={
    #     # "task": "qa",
        "docs_path": "./src/sources/LISTINGS.xlsx",
    #     "chunk_token_size": 2000,
    #     "model": "gpt-4",
        "client": chroma_client,
        "embedding_model": "all-mpnet-base-v2",
        "collection_name": "italianrealestate",
        "get_or_create": True,  # set to False if you don't want to reuse an existing collection, but you'll need to remove the collection manually
    },
)

user_proxy = ConversableAgent(
    name="Admin",
    system_message="Give the task, and send "
    "instructions to planner to define the real-estate investment strategy",
    code_execution_config=False,
    llm_config=llm_config,
    human_input_mode="TERMINATE",
)

planner = ConversableAgent(
    name="Planner",
    system_message=planner_system_message,
    description="Planner. Given a task, determine what "
    "information is needed to complete the task. "
    "After each step is done by others, check the progress and "
    "instruct the remaining steps",
    llm_config=llm_config,
)

executor = LocalCommandLineCodeExecutor(
    timeout=3600,
    work_dir="./src/codex",
    # functions=[italianhousing, openbb, get_stock_prices, plot_stock_prices],
)


# code_executor_agent = ConversableAgent(
#     name="code_executor_agent",
#     llm_config=llm_config,
#     code_execution_config={"executor": executor},
#     human_input_mode="ALWAYS",
#     default_auto_reply=
#     "Please continue. If everything is done, reply 'TERMINATE'."
# )

# code_writer_agent = AssistantAgent(
#     name="code_writer_agent",
#     # system_message=code_writer_agent_system_message,
#     llm_config=llm_config,
#     # code_execution_config={"executor": executor},
#     human_input_mode="NEVER",
# )

# code_writer_agent_system_message = code_writer_agent.system_message
# code_writer_agent_system_message += executor.format_functions_for_prompt()


finance_agent = ConversableAgent(
    name="finance_agent",
    system_message=finance_agent_system_message,
    llm_config=llm_config,
    code_execution_config={"executor": executor},
    human_input_mode="NEVER",
)

# italianhousingagent = RetrieveUserProxyAgent(
#     name="Italian Housing Market Information",
# #   is_termination_msg=termination_msg,
#     human_input_mode="NEVER",
#     default_auto_reply="Reply `TERMINATE` if the task is done.",
#     max_consecutive_auto_reply=6,
#     retrieve_config={
#         # "task": "code",
#         # "docs_path": "https://raw.githubusercontent.com/microsoft/FLAML/main/website/docs/Examples/Integrate%20-%20Spark.md",
#         # "chunk_token_size": 1000,
#         "model": llm_config,
#         "client": chromadb.PersistentClient(path="./src/memory"),  # deprecated, use "vector_db" instead
#         "vector_db": None,  # to use the deprecated `client` parameter, set to None and uncomment the line above
#         "overwrite": False,  # set to True if you want to overwrite an existing collection
#         # "collection_name": "groupchat",
#         "get_or_create": True,
#     },
#     code_execution_config=False,  # we don't want to execute code in this case.
#     description="Assistant who gathers information about real estate listing in Italy",
# )

# @code_writer_agent.register_for_execution()
# @finance_agent.register_for_llm(description="real estate listings in italy")
# def italianhousing(question: str) -> str: 
#     """get realestate listing in Italy
#     Args :
#         question (str) : a plain text question real estate listings in Italy 
#     Returns : 
#         result (str) : a plain text list of real estate listings in Italy
#     """
#     result = Retriever.retrieve(question)
#     return result 


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

# @code_writer_agent.register_for_execution()
# @finance_agent.register_for_llm(description="Stock Prices market information")
# def get_stock_prices(stock_symbols: str, start_date: str, end_date: str) -> "pd.DataFrame":
#     """Get the stock prices for the given stock symbols between
#     the start and end dates.

#     Args:
#         stock_symbols (str or list): The stock symbols to get the
#         prices for.
#         start_date (str): The start date in the format
#         'YYYY-MM-DD'.
#         end_date (str): The end date in the format 'YYYY-MM-DD'.

#     Returns:
#         pandas.DataFrame: The stock prices for the given stock
#         symbols indexed by date, with one column per stock
#         symbol.
#     """
#     import yfinance

#     stock_data = yfinance.download(
#         stock_symbols, start=start_date, end=end_date
#     )
#     return stock_data.get("Close")


# @code_writer_agent.register_for_execution()
# @finance_agent.register_for_llm(description="plotting stock prices")
# def plot_stock_prices(stock_prices: "pd.DataFrame", filename: str) -> None:
#     """Plot the stock prices for the given stock symbols.

#     Args:
#         stock_prices (pandas.DataFrame): The stock prices for the
#         given stock symbols.
#     """
#     import matplotlib.pyplot as plt

#     plt.figure(figsize=(10, 5))
#     for column in stock_prices.columns:
#         plt.plot(
#             stock_prices.index, stock_prices[column], label=column
#                 )
#     plt.title("Stock Prices")
#     plt.xlabel("Date")
#     plt.ylabel("Price")
#     plt.grid(True)
#     plt.savefig(filename)

