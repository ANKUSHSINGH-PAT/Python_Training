import requests
def fetch_json_from_url(url):
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully fetched the JSON data from {url}")
        # Parse the JSON content
        data = response.json()
        # Print the JSON data in a pretty format
        print(data)
    else:
        print(f"Failed to fetch the JSON data from {url}. Status code: {response.status_code}")
# Example usage
url = "http://127.0.0.1:8000/"
fetch_json_from_url(url)