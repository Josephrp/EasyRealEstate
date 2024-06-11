# EasyRealEstate

EasyRealEstate is a specialized application that helps you find perfectly segmented real estate deals and investment properties in Italy .

[Join us on Discord for more](https://discord.gg/JCjd88GQ) 

## Why Use It

EasyRealRealEstate is designed for anyone looking to invest in the Italian real estate market, whether you are a seasoned investor or new to property investment. It simplifies the complexity of financial and market analyses, providing insights that are typically only available to professional investment firms. This tool is particularly useful for:

- Identifying undervalued properties that meet specific investment criteria.
- Analyzing macroeconomic trends and their impact on real estate values.
- Generating financial models that predict the future profitability of investments.

## Advantages

- **Streamlined Workflow**: Combines several analytical tools into one comprehensive platform, minimizing the need for multiple software and extensive manual work.
- **Customization**: Tailors analysis based on user-defined criteria, allowing for personalized investment strategies.
- **Real-time Data Utilization**: Integrates with live data sources for up-to-date information and accuracy in forecasting.
- **User-friendly Interface**: Provides a simple interface for complex processes, making advanced investment analysis accessible to non-experts.

## Benefits

EasyRealEstate offers several benefits:

- **Time Efficiency**: Reduces the time required for market research and analysis, facilitating quicker investment decisions.
- **Cost Reduction**: Minimizes the cost associated with investment research and analysis typically incurred through professional services.
- **Increased Accuracy**: Improves the accuracy of investment assessments with AI-driven analysis and real-time data.
- **Enhanced Decision Making**: Provides a comprehensive view of the investment landscape, helping users make informed decisions that align with their financial goals.

## Investment Objectives Examples

- **Cash Flow**: Target properties that offer positive cash flow from rental income.
- **Capital Appreciation**: Focus on areas with high potential for increase in property value.
- **Portfolio Diversification**: Diversify investment across different types of properties and locations within Italy.
- **Tax Advantages**: Identify properties that offer beneficial tax considerations.

By incorporating these functionalities and objectives, EasyRealEstate stands out as a sophisticated tool that aligns with the needs of modern real estate investors, offering both high-level overviews and detailed financial insights.

## How It Works

EasyRealEstate leverages a multi-agent AI system to provide advanced analysis and decision-making tools tailored for the real estate market in Italy. The application incorporates several specialized AI agents, including a planner, a finance agent, and a user proxy. These agents interact dynamically within a constructed group chat environment to process user inputs, manage tasks, and retrieve relevant content.

1. **User Interaction**: The user starts by entering their criteria or questions regarding real estate investments in Italy. This input initiates the group chat.

2. **Task Processing**: Each of the AI agents has a specific role:
   - **Planner**: Orchestrates the workflow and ensures that tasks are assigned appropriately among agents.
   - **Finance Agent**: Handles all financial modeling aspects, analyzing potential returns and financial metrics.
   - **User Proxy**: Acts as the mediator between the user and the technical processes, presenting information in an understandable manner.

3. **Data Retrieval and Analysis**: Agents use OpenBB and Chroma for real-time data extraction and analysis. They access various datasets like the Italian Villa Dataset to pull current market data, trends, and forecasts.

4. **Group Chat Dynamics**: Through the group chat system, agents discuss and analyze the user’s query, each contributing from their expertise. The system handles natural language inputs and integrates responses into a cohesive reply.

5. **Output Generation**: The final output includes a comprehensive analysis of potential investment opportunities aligned with the user's preferences and objectives.

## Join the Community

1. **Join Discord**: Become a member of the [Tonic-AI community on Discord](https://discord.gg/JCjd88GQ) to connect with other contributors and stay updated with the latest project news. Joining Discord helps you stay connected with community support and discussions.

2. **Sign Up on Hosted GitLab**: The EasyRealEate source code is hosted on GitLab. Please sign up at [Tonic-AI GitLab](https://git.tonic-ai.com/positonic/EasyRealEstate/EasyRealEstate/) to gain access to the repository.


## Installation

**🌟STAR and 🍴FORK this Repository, then follow the instructions below exactly.**

> please note that EasyRealEstate `runs ai models locally` , the first time you install it and run it , it can take much over an hour to start up based on your computing power!

>> however subsequent deployments will take much less time !

### Run Docker

- install and run `Docker` if it's not already there on startup by [following these instructions](https://docs.docker.com/engine/install/)

- add your user to the `Docker` user group by running this command :
  - on Windows : 
    - `net localgroup docker-users "your-user-id" /ADD`
      your-user-id is your local Windows user name. You can determine this by looking at the folder name under C:\Users\ .
  - on Linux : 
    - [follow these instructions](https://docs.docker.com/engine/install/linux-postinstall/)

### Installation Instructions

**🌟STAR and 🍴FORK this Repository, then follow the instructions below exactly.**

1. **Clone the Repository**

   Clone the repository to a local machine:

   ```sh
   git clone https://github.com/Josephrp/EasyRealEstate
   cd EasyRealEstate
   ```

2. **Set your OpenAI API Key**

    currently we're providing two ways to plug in your llm:

    **Using Open AI :**
        - edit the `./src/config/config.py` file using a text editor and replace your api_key_here with your api key (keep the quotes!)

    ```python
    llm_config = {"model": "gpt-4o", 
                  "api_key": "your_api_key_here", 
                  "max_tokens": 4000 , # change this according to your needs
                  "temperature": 0.7, #change this according to your needs
        }
    ```

    **Using Azure:**
        - edit the `./src/OAI_CONFIG_LIST.json.example` file using a text editor and save it as `OAI_CONFIG_LIST.json` (without the `.example`at the end !)

    ```python
    llm_config =     {
            "model": "your_deployment_name_here", # mine is "tonicgpt"
            "api_key": "your_api_key_here",
            "base_url": "your_endpoint_url_here", # https://eastus2.api.cognitive.microsoft.com/
            "api_type": "azure",
            "api_version": "your_api_version_here", # eg "2024-02-01" for gpt-4o
            "max_tokens": 1800 ,# change this according to your needs
            "temperature": 0.7, #change this according to your needs
      }
    ```

    **In both cases:**
        - make sure you ["comment out"](https://www.datacamp.com/tutorial/python-block-comment) the method you are **not** using in `./src/config/config.py` !

3. **Set Your OpenBB Key Here**

    - then edit the `./src/config/.env.example` file using a text editor and replace your api_key_here with your api key also !

    - Get your openbb PAT from https://my.openbb.co/app/platform/pat and also add it to the `.env.example` file

    - save the `.env.example` file as `.env`in the same folder

4. **Install**

    in the command line :

    ```sh
    poetry install
    ```

5. **Run Chroma**

    - Open a new terminal and run this command to start chroma :

     ```sh
      chroma run --path ./src/memory/chromadb
      ```

6. **Run EasyRealEstate**

    in your virtual environment activated terminal from step #2 :

    ```sh
    poetry run python main.py
    ```

### Additional Configuration (Optional)

To improve results you may want to increase the number of `conversation turns` the group chat takes. Simply edit `main.py`using an editor and increase the number here :

```python
    groupchat = autogen.GroupChat(
      ...
        max_round=12, # <-- change this number !
      ...
```


## Contributing

Contributing to EasyRealEstate is a fantastic way to engage with the open source community, especially for those interested in real estate, investment tools, and AI technology. Tonic-AI encourages contributions of all types, including but not limited to new features, bug fixes, documentation improvements, and usage examples. Below are the steps to get started with contributing to the project.

You too can contribute to EasyRealEstate by following the [CONTRIBUTING](CONTRIBUTING.md) guidelines. [Join us on Discord](https://discord.gg/JCjd88GQ).
