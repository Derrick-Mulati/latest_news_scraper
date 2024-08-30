import requests
from bs4 import BeautifulSoup

def get_latest_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2')  # This may need to be adjusted based on the site's structure
    
    for i, headline in enumerate(headlines[:5], 1):
        print(f"{i}. {headline.text.strip()}")

get_latest_headlines('https://www.bbc.com/news')
