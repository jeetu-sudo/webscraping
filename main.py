# if you want to scrap a website:
# 1. use the API.
# 2.HTML web scraping using some tool like bs4
# step 0: install all the requerments
#pip install requests
# pip insall bs4
# pip install html5lib
 

import  requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

 # step 1: get the HTML requerments 
 r = requests.get(url)
 htmlContent = r.content
 print(htmlContent)
 # step 2: parse the HTML
 # step 3: HTML tree  traversal
