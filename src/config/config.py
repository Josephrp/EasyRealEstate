# ./src/config/config.py
from autogen.cache import Cache
import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('./src/config/.env')
load_dotenv(dotenv_path=dotenv_path)

openai_api_key = os.getenv("OPENAI_API_KEY")
llm_config = {"model": "gpt-4-turbo", "api_key": openai_api_key }
