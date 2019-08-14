import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/natebargatze"

scraper_file = open("scrape_info.txt", "w")

results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

tweets = soup.select("div.tweet")

for tweet in tweets:
 scraper_file.write(tweet.text.replace(" ", "\n"))

 





