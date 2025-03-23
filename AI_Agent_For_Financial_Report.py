import os

# Ensure your API key is stored in the 'GROQ_API_KEY.txt' file or environment
with open("GROQ_API_KEY.txt") as file:
    os.environ['GROQ_API_KEY'] = file.readline().strip()  # Set the API key directly

print("GROQ_API_KEY has been set!")
with open("PHI_API_KEY.txt") as file:
    os.environ['PHI_API_KEY'] = file.readline().strip()  # Set the API key directly

print("PHI_API_KEY has been set!")

# IF you want to check if the keys are indeed set

print("Groq API key set:" if os.getenv("GROQ_API_KEY") else "Groq API key not set")
print("API keys have been set!")
from textwrap import dedent
from agno.models.groq import Groq  # Import the Groq class

from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools

# Create the stock agent
finance_agent = Agent(
    model=Groq(id="llama3-70b-8192"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            historical_prices=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions=dedent("""\
        You are a seasoned credit rating analyst with deep expertise in market analysis! 📊

        Follow these steps for comprehensive financial analysis:
        1. Market Overview
           - Latest stock price
           - 52-week high and low
        2. Financial Deep Dive
           - Key metrics (P/E, Market Cap, EPS)
        3. Market Context
           - Industry trends and positioning
           - Competitive analysis
           - Market sentiment indicators

        Your reporting style:
        - Begin with an executive summary
        - Use tables for data presentation
        - Include clear section headers
        - Highlight key insights with bullet points
        - Compare metrics to industry averages
        - Include technical term explanations
        - End with a forward-looking analysis

        Risk Disclosure:
        - Always highlight potential risk factors
        - Note market uncertainties
        - Mention relevant regulatory concerns
        
        4. Conclusion
        5. Rating Recommendation
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
)

# User query: Allowing dynamic ticker symbol input
ticker_symbol = input("Enter a ticker symbol: ")
query = f"How is {ticker_symbol} performing in the age of AI?"

# Get the response for the entered ticker symbol
finance_agent.print_response(query, stream=True)
