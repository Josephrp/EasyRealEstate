# ./src/agents/agents

from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
from src.plugins.tools import openbb , plot_stock_prices , get_stock_prices , italianhousing
from src.config.config import llm_config
from src.prompts.prompts import code_writer_agent_system_message, finance_agent_system_message, planner_system_message

user_proxy = ConversableAgent(
    name="Admin",
    system_message="Give the task, and send "
    "instructions to planner to define the real-estate investment strategy",
    code_execution_config=False,
    llm_config=llm_config,
    human_input_mode="ALWAYS",
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
    work_dir="/src/codex",
)

code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",
    default_auto_reply=
    "Please continue. If everything is done, reply 'TERMINATE'.",
    functions=[get_stock_prices, plot_stock_prices],
)

code_writer_agent = ConversableAgent(
    name="code_writer_agent",
    system_message=code_writer_agent_system_message,
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)

finance_agent = ConversableAgent(
    name="finance_agent",
    system_message=finance_agent_system_message,
    llm_config=llm_config,
    code_execution_config={"executor": executor},
    functions=[italianhousing, openbb],
    human_input_mode="NEVER",
)