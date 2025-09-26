import requests
from bs4 import BeautifulSoup as bs

resp = requests.get("https://www.linkedin.com/jobs/search?keywords=Frontend%20Developer&location=Nepal")
soup = bs(resp.content)
print(soup.text)