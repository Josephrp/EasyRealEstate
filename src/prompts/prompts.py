import datetime
from src.agents.agents import executor , code_writer_agent

today = datetime.datetime.now().date()

makeaplot = f"Today is {today}. "\
"Create a plot for the above "\
"Make sure the code is in markdown code block and save the figure"\
" to a file plot.png."""

code_writer_agent_system_message = code_writer_agent.system_message
code_writer_agent_system_message += executor.format_functions_for_prompt()

finance_agent_system_message = 