 # python
import re

import requests
import json

def search_from_google(keyword):
url = "https://google.serper.dev/search"
payload = json.dumps({"q": keyword})
headers = {'X-API-KEY': 'SERP_KEY', 'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)
results = response.json()['organic']
urls = [result['link'] for result in results]
return urls

def clean_string(text):
text = text.replace("\n", " ")
cleaned_text = re.sub(r"\s+", " ", text.strip())
cleaned_text = cleaned_text.replace("\\", "")
cleaned_text = cleaned_text.replace("#", " ")
cleaned_text = re.sub(r"([^\w\s])\1*", r"\1", cleaned_text)
return cleaned_text

The load_data_from_url function       retrieves and cleans data from a web page.

  import requests
from bs4 import BeautifulSoup

def load_data_from_url(url):
response = requests.get(url)
data = response.content
soup = BeautifulSoup(data, "html.parser")
# Remove unnecessary tags and elements
tags_to_exclude = ["nav", "aside", "form", "header", "noscript", "svg", "canvas", "footer", "script", "style"]
for tag in soup(tags_to_exclude):
    tag.decompose()
content = soup.get_text()
content = clean_string(content)
return content

clean_string(text)
text (str): The text to be cleaned.

url (str): The URL of the web page to load data from.

Returns:
content (str): The cleaned text content from the web page.
search_from_google(keyword)

 Args:
keyword (str): The search keyword.
Returns:
urls (list): A list of URLs from the search results.
generate_data_file(name)

Description: Searches Google for a given name, retrieves data from the resulting URLs, and saves it to a file.

name (str): The name to search for.
Returns:
data (str): The concatenated data from the URLs.

generate_prompt_file(context)

context (str): The context to include in the prompt files.
