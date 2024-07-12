import os
import pandas as pd
from langchain_openai import AzureChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

os.environ["AZURE_OPENAI_API_KEY"] = "402b6da1cb77449db7bd3cd47c252eaf"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://oai-bispoc-dev-001.openai.azure.com"

llm=AzureChatOpenAI(
    openai_api_version="2023-07-01-preview",
    azure_deployment="gpt432k",
)
df = pd.read_csv("test.csv") # Replace input file
agent = create_pandas_dataframe_agent(llm, df, agent_type="openai-tools", verbose=True, allow_dangerous_code=True)
agent.invoke( # Replace prompt
    {
        "input": "Create a summary survival rate, by analysing how different aspects of the passenger impact the rate, and tell which aspect has the most impact"
    }
)
