import requests
from bs4 import BeautifulSoup

def crawl(url, depth):
    if depth == 0:
        return

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Crawling: {url}")

            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href and href.startswith("http"):
                    crawl(href, depth - 1)
    except requests.RequestException as e:
        print(f"Failed to crawl {url}: {str(e)}")


start_url = "http://example.com" 
depth = 2  # Depth of the crawl

crawl(start_url, depth)
