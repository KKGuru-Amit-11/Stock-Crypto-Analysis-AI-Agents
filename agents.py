# Import Require Library
import os
from crewai import Agent
from tools import scrape_tool,search_tool
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

# # Creating LLM Model
# os.environ['GOOGLE_API_KEY']='AIzaSyD5ggkVEWVzFE3NaFa73a0MHuJPmkT3U8M'
# llm_model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
#                                    api_key=os.getenv('GOOGLE_API_KEY'))

# Creating LLM Model
os.environ['GROQ_API_KEY']='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'
llm_model = ChatGroq(model='llama3-8b-8192',api_key=os.getenv('GROQ_API_KEY'))

# Creating Multi AI Agents
data_analyst_agent = Agent(
    role='Data Analyst',
    goal='''Monitor and Analyze Market Data in Real-Time
    to identify trend and predict market movements''',
    backstory='''Specializing in financial market, this agent uses
    statistical modeling and machine learning to provide crucial insights
    with a knack for data informing trading decisions.''',
    verbose=True,
    allow_delegation=True,
    tools = [search_tool,scrape_tool],
    llm=llm_model
)

trading_strategy_agent = Agent(
    role='''Trading Strategy developer''',
    goal='''develop and test various trading strategies based
    on insights from the Data Analyst Agent.''',
    backstory='''Equipped with a deep understanding of financial
    markets and quantitative analysis, this agent devises are refine
    trading strategies. it evaluates the performance of different approaches
    to determine the most profitable and risk-averse options.''',
    verbose=True,
    allow_delegation=True,
    tools=[search_tool,scrape_tool],
    llm=llm_model
)

execution_agent = Agent(
    role='Trade Advisor',
    goal='''Suggest optimal trade execution strategies 
    based on approved trading Strategies''',
    backstory='''This agent specialize in analyzing the timing, price and 
    logistical details of potential trades. By evaluting these factor, 
    it provies well-founded suggestions for when and how trades should be 
    executed to maximize efficiency and adherence to strategy.''' ,
    verbose=True,
    allow_delegation=True,
    tools=[search_tool,scrape_tool],
    llm=llm_model
)

risk_management_agent = Agent(
    role='Risk Advisor',
    goal='''Evaluate and provide insights on the risk 
    associalted with petential trading activities''',
    backstory='''Armed with a deep understanding of risk assessment models
    and market dynamics, this agent scrutinizes the potential risk of 
    proposed trades. It offers a detailed analysis of risk exposure and 
    suggests safeguards to ensure that trading activities aling with the firm's 
    risk tolerance.''',
    verbose=True,
    allow_delegation=True,
    tools=[search_tool,scrape_tool],
    llm=llm_model
)
