import requests
from bs4 import BeautifulSoup

url = "https://reddit.com/search"

results = requests.get(url,
params={"q": "food allergies"},
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
)

soup = BeautifulSoup(results.text, "html.parser")

make_file = open("reddit_info.text", "w")

# red_post = soup.select("h3._eYtD2XCVieq6emjKBH3m")

# for post in red_post:
#   print(results)
#   make_file.write(str(post.text))

# red_cat = soup.select("div._2mHuuvyV9doV3zwbZPtIPG href")
red_cat = soup.select("a._1L0pdcPf58t25Jy6ljHIKR")
#print(red_cat.text)

# for cat in red_cat:
#   print(results)
#   make_file.write(str(cat.text).replace('/', '\n'))

red_cat_two = soup.select("a._3ryJoIoycVkA88fy40qNJc")

red_comments = soup.select("span.FHCV02u6Cp2zYL0fhQPsO")

# for comment in red_comments:
#   print(results)
#   make_file.write(str(comment.text).replace(' ', '\n'))

