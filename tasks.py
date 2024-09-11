# Import Require Library
from crewai import Task
from agents import data_analyst_agent,trading_strategy_agent,execution_agent,risk_management_agent

# Task For the Agents
data_analyst_task = Task(
    description='''Continuosly Moniter and Analyze Market Data for
    the selected stock {stock_selection}. use statistical modeling and 
    Machine learning to identify trends and predict marketmovement''',
    expected_output='''A comprehensive data analysis report detailing potential 
    Insights and alert about significant market oppotunities or threate for {stock_selection}''',
    agent=data_analyst_agent
)

strategy_development_task = Task(
    description='''Develop and refine trading strategies 
    based on the insights from the Data analyst and user 
    defined risk tolerance {risk_tolerance}. Consider 
    trading preferences {trading_strategy_preference}''',
    expected_output='''A set of potential Trading strategies for 
    {stock_selection} that align with the user's risk tolerance''',
    agent=trading_strategy_agent
)

execution_planning_task = Task(
    description='''Analyze Approved trading strategies to 
    determine the best execution method for {stock_selection}, 
    Considering current Market Condition and Optimal Pricing''',
    expected_output='''Detailed execution plan suggesting how 
    and when to execute trades for {stock_selection}''',
    agent=execution_agent
)

risk_assessment_task = Task(
    description='''Evaluate the risk associated with the 
    proposed trading strategies and execution plan for 
    {stock_selection}. provide a detailed analysis of 
    potential risks and suggest mitigation strategies''',
    expected_output='''A comprehensive risk analysis report detailing potential
    risk and mitigation recommendations for {stock_selection}.''',
    agent=risk_management_agent
)