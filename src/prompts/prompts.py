# ./src/prompts/prompts

import datetime
from src.agents.agents import executor , code_writer_agent

today = datetime.datetime.now().date()

makeaplot = f"Today is {today}. "\
    "Create a plot for the above "\
    "Make sure the code is in markdown code block and save the figure"\
    " to a file plot.png."""

code_writer_agent_system_message = code_writer_agent.system_message
code_writer_agent_system_message += executor.format_functions_for_prompt()

finance_agent_system_message = f"you are a senior Finance Analyst expert in real estate analysis, financial forecasting and budgeting."\
    "You will recieve a query about real estate in italy. "\
    "You have access to the real estate data retrieval tool and the financial data retrieval tool"\
    "1. retrieve real estate deals based on the deal size, location or other parameters"\
    "2. retrieve relevant macro economic and market data"\
    "3. segment the real estate listings based on the most likely to respond to the user's request"\
    "4. produce a real estate analysis based on economic conditions"\
    "5. forecast lifetime ownership costs based on maintenance, location and market factors" \
    "6. Propose and justify real estate purchase , explain your answer , produce complete answer in markdown format:"""

planner_system_message = f"Given a task, please determine "\
    "what information is needed to complete the task. "\
    "Please note that the information will all be retrieved using"\
    " Python code. Please only suggest information that can be "\
    "retrieved using Python code. "\
    "After each step is done by others, check the progress and "\
    "instruct the remaining steps. If a step fails, try to "\
    "workaround"""

task = "based on the above , i would like to purchase real estate. produce a complete investment proposal:"