#chmod +x <filename>.py
#sudo pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
page = requests.get("http://news.sanook.com/lotto/check/01102560/")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(class_="lotto__number lotto__number--first").get_text()
print(seven_day)
