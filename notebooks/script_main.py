from selenium import webdriver
from bs4 import BeautifulSoup
import time, json, urllib.request, requests
from datetime import date

def prin(**kwargs):
    

category = '3d'
link = f"https://wallpaperscraft.com/catalog/{category}/page"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option("prefs", {
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=options)

# Open json file for page number
with open("data.json",'r') as file:
    file_data = json.load(file)

peg = file_data[category]['peg']
img_4k = file_data[category]['img_4k']
img_hd = file_data[category]['img_hd']
res_4k = '3840x2160.jpg'
res_hd = '3840x2160.jpg'

for i in range(file_data[category]['peg'], file_data[category]['max_peg']):
    driver.get(link + str(peg))
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    calss = soup.find_all('ul', {'class': 'wallpapers__list'})

    for i in calss:
        print('\n\n\n')
        a = i.select('li > a > span > img')
        for j in a:
            r = requests.get(j['src'][:-11] + res_4k, allow_redirects=True)
            if r.reason == 'OK':
                open(j['src'].split('/', 10)[-1:][0][:-19]+'.jpg', 'wb').write(r.content)
                file_data[category]['img_4k'] += 1
            else:
                r = requests.get(j['src'][:-11] + res_hd, allow_redirects=True)
                if r.resaon == 'OK':
                    open(j['src'].split('/', 10)[-1:][0][:-19]+'.jpg', 'wb').write(r.content)
                    file_data[category]['img_hd'] += 1
                else:
                    file_data[category]['no_img'] += 1
                    print('Image not found')

    peg += 1

    file_data[category] = peg

    with open("data.json",'w') as file:
        json.dump(file_data, file, indent = 4)
    
driver.close()