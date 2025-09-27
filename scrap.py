import requests
from bs4 import BeautifulSoup as bs

resp = requests.get(
    "https://www.linkedin.com/jobs/search?keywords=Frontend%20Developer&location=Nepal"
)
soup = bs(resp.content,"html.parser")

items = soup.find_all("div", class_="base-card")
for item in items:
    link = item.find("a")["href"].strip()
    title = item.find("h3", class_="base-search-card__title").text.strip().replace(",","")
    company = item.find("a", class_="hidden-nested-link")["href"].strip().replace(",","")
    company_link = item.find("a", class_="hidden-nested-link").text.strip()
    location = item.find("span",class_="job-search-card__location").text.strip().replace(",","")
    print(f"{title},{company},{location},{company_link},{link}\n")