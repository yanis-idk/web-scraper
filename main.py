import requests
import json
from bs4 import BeautifulSoup
data = []
for page in range(1,11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    try:
        res = requests.get(url,timeout=5)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Page {page} failed: {e}")
        continue
    soup = BeautifulSoup(res.text,"html.parser")
    quotes = soup.find_all("span",class_="text")
    authors = soup.find_all("small",class_="author")
    for auth,quaot in zip(authors,quotes):
        data.append({"the author": auth.text , "the quote": quaot.text})

with open("quoets.json","w") as f:
    json.dump(data,f,indent=4)

