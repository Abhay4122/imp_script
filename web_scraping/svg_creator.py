# import requests
# from bs4 import BeautifulSoup


# # Working Fine but lazyload no working

# R = requests.get('https://undraw.co/illustrations')
# content = R.content
# soup = BeautifulSoup(content, 'html.parser')
# calss = soup.find_all('div')
# print(calss)



# Working fine but without title

# page = open('Illustrations _ unDraw.html')
# soup = BeautifulSoup(page.read())
# svg_list = soup.find_all('svg')

# num = 1
# for i in svg_list:
#     f = open(str(num) + '.svg', 'w')
#     f.write(str(i))
#     f.close()
#     num += 1




import selenium as se
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
from datetime import date

link = "https://undraw.co/illustrations"
base_url = "https://undraw.co/illustrations"
final_db = []

options = se.webdriver.ChromeOptions()
options.add_argument('headless')

# driver = webdriver.PhantomJS('C:\\Users\\Abhay\\Downloads\\phantomjs\\bin\\phantomjs.exe')
# driver.get(link)

driver = webdriver.Chrome('C:\\Users\\Abhay\\Downloads\\chromedriver\\chromedriver.exe',chrome_options=options)
driver.get(link)

# ---

# scrolling

lastHeight = driver.execute_script("return document.body.scrollHeight")
#print(lastHeight)

pause = 2
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
    print(f'\nnew_hight = {newHeight}\n')

# ---

html = driver.page_source
# soup = BeautifulSoup(html, "html5lib")
soup = BeautifulSoup(html, "html.parser")


#driver.find_element_by_class_name

divs = soup.find_all('div', {'class': 'gridItem'})
for i in divs:
    title = i.find('div', {'class': 'gridItem__title'})
    svg = i.find('svg')

    # Append values in list

    try:
        final_db.append({'svg_title': str(title.text), 'svg_id': str(svg.get('id'))})
    except:
        pass

    # Save Files

    # f = open(str(title.text) + '.svg', 'w')
    # f.write(str(svg))
    # f.close()

    # print(title.text, svg.get('id'))

# print(final_db)
# Create database
final_json = 'final_' + str(date.today()) + '.json'
with open(final_json, 'w') as json_file:
    json.dump(final_db, json_file)