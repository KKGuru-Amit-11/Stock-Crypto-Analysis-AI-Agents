# Import Require Library
import streamlit as st
from crewai import Crew, Process
from agents import data_analyst_agent,trading_strategy_agent,execution_agent,risk_management_agent,llm_model
from tasks import data_analyst_task,strategy_development_task,execution_planning_task,risk_assessment_task

st.subheader('Multi AI Agents for Stock or Crypto Analysis...')

crew = Crew(
    agents=[data_analyst_agent,trading_strategy_agent,
            execution_agent,risk_management_agent],
    tasks=[data_analyst_task,strategy_development_task,
           execution_planning_task,risk_assessment_task],
    manager_llm=llm_model,
    process=Process.hierarchical,
    verbose=True
)
# Define the options for the dropdown
stock_options = ["Bitcoin", " Ethereum", "USDT Tether", "Doge Coin", "Binance Coin",
                 "Nestle India", "Apple Inc", "Tata Motar LTD", "Adani Power"
                 , "Reliance Industries", "Others (Please Specify)"]

trading_strategy_options = ["Intra Day Trading", " Future Option Trading", "Swing Trading",
                 "P2P Trading", "Long-Term Trading", "Scalping", "Momentum Trading"
                 , "Option Trading", "Others (Please Specify)"]

# Getting Task From Web
with st.form(key='financial_inputs'):
    stock_selection = st.selectbox(label="**Select Your Stock/Crypto:**", options=stock_options,index=None)
    initial_capital=st.slider(label="**Initial Your Capital:**",min_value=0,max_value=5000000,value=10000,step=500)
    risk_tolerance=st.selectbox(label='**Define Risk Tolerance:**', options=["Low","Medium","High"],index=None)
    trading_strategy_preference = st.selectbox(label="**Trading Strategy:**", options=trading_strategy_options,index=None)
    submit_button = st.form_submit_button('Submit.')

def stock_selection_func(value):
    if value == "Others (Please Specify)":
        input_value = st.text_input("**Please Specify the Name of Stock/Crypto:**")
        return input_value
    else:
        return stock_selection

def trading_strategy_func(value):
    if value == "Others (Please Specify)":

        custom_value = st.text_input("**Please Specify The Name of Trading Strategy:**")
        return custom_value
    else:
        return trading_strategy_preference
    
stock_value = stock_selection_func(stock_selection)
trading_strategy=trading_strategy_func(trading_strategy_preference)

financial_trading_input = {
    'stock_selection':stock_value,
    'initial_capital':initial_capital,
    'risk_tolerance':risk_tolerance,
    'trading_strategy_preference':trading_strategy,
    'new_impact_consideration':True
}

# Query Answering
if st.button("**Generate...**"):
    with st.spinner("Generating Response..."):
        st.info('Input Details...')
        st.markdown(f'Stock/Crypto Name: {stock_value} ...')
        st.markdown(f'Capital Initialise: {initial_capital} ...')
        st.markdown(f'Risk Tolrance: {risk_tolerance} ...')
        st.markdown(f'Trading Strategy Preference: {trading_strategy} ...')
        st.info('Here is a Response...')
        res=crew.kickoff(inputs=financial_trading_input)
        st.markdown(res)
        result=str(res)
        st.download_button(label='Download Text File',file_name=f'{stock_selection}Report.txt',data=result)