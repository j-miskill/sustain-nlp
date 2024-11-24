import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_company_cdp_score(company_ticker):
    # URL to scrape
    url = "https://www.google.com/finance/quote/BEI:ETR"

    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the element by its text
        target_element = soup.find(string="CDP Climate Change Score")
        
        # If found, get the parent element to show the containing div
        if target_element:
            parent = target_element.find_parent("span").find_parent("div")
            grade_element = parent.find("div", recursive=False)
            return grade_element.text
    return None


esg_documents_df = pd.read_csv('./dax_esg_media_dataset/esg_documents_for_dax_companies.csv', sep='|')
for index, ticker in enumerate(esg_documents_df['symbol']):
    print(f"Row {index}, Ticker: {symbol}")