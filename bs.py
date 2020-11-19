from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.racingcircuits.info/a-to-z-circuit-list.html?fbclid=IwAR0dFN6zqcJU011CQVlumPKNI6jK-lSKcWjV1GoRVkl0PwdnFqIQqmeXFYQ')
soup = BeautifulSoup(r.text, 'html.parser')
data = []

for el in soup.find_all("div", {"class": "az-item"}):
    data.append(el.get_text().strip())
track_name = []
slug = []
for i in data:
    if 'See More' not in i:
        track_name.append(i)
        slug.append(i.encode('ascii', 'ignore').decode("utf-8").replace(" ", "").replace(",", ""))