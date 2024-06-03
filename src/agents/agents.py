from autogen import register_function
from autogen import ConversableAgent, AssistantAgent
from autogen.coding import LocalCommandLineCodeExecutor
from src.plugins.tools import openbb , plot_stock_prices , get_stock_prices
from src.config.config import llm_config

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
    functions=[openbb, get_stock_prices, plot_stock_prices],
)

code_writer_agent = ConversableAgent(
    name="code_writer_agent",
    system_message=code_writer_agent_system_message,
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)
