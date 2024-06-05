# positonic

Positonic is a specialized agent that helps you find perfectly segmented real estate deals and investment properties in Italy .

## Installation

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

```bash
python main.py
```

### Installation Problems

1. **OpenBB Agents** 

Sometimes installation can fail because of `openbb-agents`. If this happens , you will see some red text on the steps above. Simply install it using the following command additionally: 

```bash
pip install --no-cache-dir openbb-agents
```

### Refs:

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