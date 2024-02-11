# Import necessary libraries
import requests
from bs4 import BeautifulSoup 

# The URL of the website you want to scrape
url = "https://www.swiggy.com"

# Send a GET request to the website
response = requests.get(url) 

# Check if the request was successful
if response.status_code == 200: 
    print("Success!")
else:
    print("Error")