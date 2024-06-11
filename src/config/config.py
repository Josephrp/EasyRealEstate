# ./src/config/config.py
from autogen.cache import Cache

# llm_config = {"model": "gpt-4o", 
#               "api_key": "your_api_key_here", 
#               "max_tokens": 4000 , # change this according to your needs
#               "temperature": 0.7, #change this according to your needs
#     }


filter_criteria = {"model": ["gptonic"]}
### AZURE 
llm_config =     {
        "model": "your_model_name_here", # mine is "tonicgpt"
        "api_key": "your_api_key_herre",
        "base_url": "your_endpoint_url_here", # https://eastus2.api.cognitive.microsoft.com/
        "api_type": "azure",
        "api_version": "your_endpoint_version_here", # eg "2024-02-01" for gpt-4o
        "max_tokens": 4000 ,# change this according to your needs
        "temperature": 0.7, #change this according to your needs
   }


import os

def load_env_file(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value