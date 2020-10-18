from selenium import webdriver
from bs4 import BeautifulSoup
import time, json, urllib.request, requests
from datetime import date

link = "https://wallpaperscraft.com/all/page"
final_db = []

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option("prefs", {
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome('C:\\Users\\Abhay\\Downloads\\Documents\\chromedriver.exe',chrome_options=options)

# 3840x2160
peg = 1
while True:
    driver.get(link + str(peg))

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    calss = soup.find_all('ul', {'class': 'wallpapers__list'})

    for i in calss:
        print('\n\n\n')
        a = i.select('li > a > span > img')
        print(a)
        for j in a:
            print(f"\n\n{j['src'].split('/', 10)[-1:][0][:-19]}\n\n")
            r = requests.get(j['src'][:-11]+'1920x1080.jpg', allow_redirects=True)
            open(j['src'].split('/', 10)[-1:][0][:-19]+'.jpg', 'wb').write(r.content)
    peg += 1