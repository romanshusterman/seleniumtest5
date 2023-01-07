from selenium import webdriver
from bs4 import BeautifulSoup
import os
import datetime
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

website = driver.get('https://www.ilmakiage.co.il/mineral-lip-pencil-4043')

for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup1 = driver.page_source.encode("utf-8")

driver.close()

soup = BeautifulSoup(soup1, 'lxml')

try:
    soup.find('span', class_='qtyValidate_color', style='display: block;').contents[0] == 'הכמות המבוקשת אינה קיימת'
    qty_validate = soup.find('span', class_='qtyValidate_color', style='display: block;').contents[0]
    result = f'Ooops, the stock is empty ({qty_validate}). Open the app later to check quantity \n'
except AttributeError as err:
    result = "Tut sheli, it'shopping time, your favorite lip pencil is in stock \n https://www.ilmakiage.co.il/mineral-lip-pencil-4043 \n"

current_time = datetime.datetime.now()
with open('rand2.txt', mode='a') as file:
    file.write(f"{current_time}, {result}")
