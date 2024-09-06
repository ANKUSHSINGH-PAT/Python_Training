

import requests
from bs4 import BeautifulSoup
'''
def fetch_and_parse_valid_links(url):
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully fetched the content from {url}")
        # Parse the response content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and print valid links (URLs) from the page
        links = soup.find_all('a', href=True)
        print("Valid Links:")
        for link in links:
            abc = link.get('href')
            if abc.startswith("http://") or abc.startswith("https://"):
             print(abc)
        #     print(link)
        #     if link.startswith("http://"):
        #         print(link)
        
    else:
        print(f"Failed to fetch the content from {url}. Status code: {response.status_code}")
# Example usage
url = "https://www.python.org/"


fetch_and_parse_valid_links(url)

'''

import requests
from bs4 import BeautifulSoup

def fetch_and_parse_content(url):
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully fetched the content from {url}")
        # Parse the response content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and print text content from the page
        page_text = soup.get_text()
        print("Text Content")
        print(page_text)
        words = page_text.split()
        page_text_cleaned = ' '.join(words)
        print("Text Content:")
        print(page_text_cleaned[:300])  # Printing only the first 400 characters for clear view
        
        # Extract and print valid links (URLs) from the page
        links = soup.find_all('a', href=True)
        print("\nValid Links:")
        for link in links:
            href = link.get('href')
            if href.startswith("http://") or href.startswith("https://"):
                print(href)
    else:
        print(f"Failed to fetch the content from {url}. Status code: {response.status_code}")

# Example usage
url = "https://www.python.org/"
fetch_and_parse_content(url)