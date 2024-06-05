# EasyRealEstate

EasyRealEstate is a specialized application that helps you find perfectly segmented real estate deals and investment properties in Italy .

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

# How It Works

EasyRealEstate leverages a multi-agent AI system to provide advanced analysis and decision-making tools tailored for the real estate market in Italy. The application incorporates several specialized AI agents, including a planner, a finance agent, and a user proxy. These agents interact dynamically within a constructed group chat environment to process user inputs, manage tasks, and retrieve relevant content.

1. **User Interaction**: The user starts by entering their criteria or questions regarding real estate investments in Italy. This input initiates the group chat.
   
2. **Task Processing**: Each of the AI agents has a specific role:
   - **Planner**: Orchestrates the workflow and ensures that tasks are assigned appropriately among agents.
   - **Finance Agent**: Handles all financial modeling aspects, analyzing potential returns and financial metrics.
   - **User Proxy**: Acts as the mediator between the user and the technical processes, presenting information in an understandable manner.

3. **Data Retrieval and Analysis**: Agents use OpenBB and Chroma for real-time data extraction and analysis. They access various datasets like the Italian Villa Dataset to pull current market data, trends, and forecasts.

4. **Group Chat Dynamics**: Through the group chat system, agents discuss and analyze the user’s query, each contributing from their expertise. The system handles natural language inputs and integrates responses into a cohesive reply.

5. **Output Generation**: The final output includes a comprehensive analysis of potential investment opportunities aligned with the user's preferences and objectives.

## Installation

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

1. **Clone the Repository**

   Clone the repository to a local machine:

   ```sh
   git clone https://github.com/tonic/investinitaly
   cd investinitaly
   ```

2. **Set your OpenAI API Key**

- edit the `./src/config/config.py` file using a text editor and replace your api_key_here with your api key (keep the quotes!)

  `llm_config = {"model": "gpt-4-turbo", "api_key": "your_api_key_here" }`

- then edit the `./src/config/.env.example` file using a text editor and replace your api_key_here with your api key also !

- Get your openbb PAT from https://my.openbb.co/app/platform/pat and also add it to the `.env.example` file

- save the `.env.example` file as `.env`in the same folder

2. **Set Up the Environment**

   Run the setup script to create and activate the virtual environment, and install the dependencies:

   - On Windows:

     ```bash
     .\setup_env.bat
     ```

   - On macOS/Linux:

     ```bash
     chmod +x setup_env.sh
     ./setup_env.sh
     ```

   then

   - On Windows:

      ```sh
      venv\Scripts\activate
      ```

   - On macOS/Linux:

      ```sh
      source venv/bin/activate
      ```

Once activated, you should see the name of your virtual environment in the command prompt, indicating that you are now working within the virtual environment.

3. **Run Chroma**

Open a new terminal and run this command to start chroma :

- ```chroma run --path ./src/memory/chromadb```

4. **Run EasyRealEstate**

in your virtual environment activated terminal from step #2 :

```bash
python main.py
```

### Installation Problems

1. **OpenBB Agents** 

Sometimes installation can fail because of `openbb-agents`. If this happens , you will see some red text on the steps above. Simply install it using the following command additionally: 

```bash
pip install --no-cache-dir openbb-agents
```

### Additional Configuration (Optional)

To improve results you may want to increase the number of `conversation turns` the group chat takes. Simply edit `main.py`using an editor and increase the number here :

```python
    groupchat = autogen.GroupChat(
      ...
        max_round=12, # <-- change this number !
      ...
```

### References

- Open BB Dev
  - https://hackathon.openbb.dev/docs#/equity/equity_fundamental_metrics
  - https://github.com/OpenBB-finance/openbb-agents
  - https://github.com/OpenBB-finance/OpenBBTerminal

- Digital Regulatory Reporting Master
  - https://drive.google.com/drive/u/3/folders/1EvNruvaPFpjOw7RFXTngky_mYkmTixXz
  - https://pypi.org/project/openbb/

- Italian Villa Dataset
  - https://docs.google.com/spreadsheets/d/1VZsiTju0C3As3CZrjBF7ciSSoMTqTe3TwjRlE6rkMC8/edit#gid=526569133

- Structured Finance Hackathon
  - https://structured-finance.notion.site/Toolkit-0c51802b71784a32b0293736d02bc77e
  - https://structured-finance.notion.site/About-3ffbce1c93864a74a795c187f7019370
  - https://structured-finance.notion.site/Challenges-Prizes-49e52746b9384a92a8a69112f4d65668

- FinOS
  - https://cdm.finos.org/docs/event-model/