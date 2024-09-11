# Import Require Library
import os
from crewai_tools import SerperDevTool,ScrapeWebsiteTool

os.environ['SERPER_API_KEY'] = '5e91bacd42a33cdf4299197ce6d7e49aaca23310'

search_tool=SerperDevTool()
scrape_tool=ScrapeWebsiteTool()