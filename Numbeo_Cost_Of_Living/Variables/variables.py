import requests
from bs4 import BeautifulSoup
from Setup.setup import *

headers = requests.utils.default_headers()
url = 'https://www.numbeo.com/cost-of-living/in/'+city+'?displayCurrency='+currency
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, features="html.parser")
print(url)


Last_Update = []
items_list = []
prices_list = []
Markets_Items = []