from selenium import webdriver
from bs4 import BeautifulSoup
import time, json, urllib.request, requests
from datetime import date

chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
link = "https://www.pagalworld.mobi/a-to-z-bollywood-mp3-list-of-a/list/p-1.html"
final_db = link_list = []

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option("prefs", {
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome('C:\\Users\\Abhay\\Downloads\\Documents\\chromedriver.exe',chrome_options=options)

# 3840x2160
# peg = 1
# while True:
driver.get(link)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
calss = soup.find_all('div', {'id': 'w0'})

for i in calss:
    main_link = i.select("div > a")
    print(f'\n\n{main_link}\n\n')
    for j in main_link:
        # print(j['href'])
        driver.get('https://www.pagalworld.mobi'+j['href'])
        html2 = driver.page_source
        soup2 = BeautifulSoup(html2, "html.parser")
        calss2 = soup2.find_all('div', {'id': 'w0'})

        print('\n\n')
        for k in calss2:
            sub_link = k.select('div > a')
            for l in sub_link:
                # print(l['href'])
                driver.get('https://www.pagalworld.mobi'+l['href'])
                html3 = driver.page_source
                soup3 = BeautifulSoup(html3, "html.parser")
                calss3 = soup3.find_all('div', {'class': 'file-details'})
                print(calss3[0].select('div > div > audio > source')[0]['src'])
                urllib.request.urlretrieve(calss3[0].select('div > div > audio > source')[0]['src'], calss3[0].select('div > div > audio > source')[0]['src'].split('/', 10)[-1:][0])
                # r = requests.get(calss3[0].select('div > div > audio > source')[0]['src'], stream=True)
                # open(calss3[0].select('div > div > audio > source')[0]['src'].split('/', 10)[-1:][0], 'wb').write(r.content)
                # with open(calss3[0].select('div > div > audio > source')[0]['src'].split('/', 10)[-1:][0],"wb") as pdf:
                #     for chunk in r.iter_content(chunk_size=1024):
                #          # writing one chunk at a time to pdf file 
                #          if chunk: 
                #              pdf.write(chunk)
