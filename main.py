import requests
from io import BytesIO
from PIL import Image
import os
from bs4 import BeautifulSoup


search = input('Search : ')

dir_name = search.replace(' ', '_')
if not os.path.isdir(dir_name) :
    os.makedirs(dir_name)

params = {'q' : search}
url_name = 'https://www.bing.com/images/search'
req = requests.get(url_name, params)

soup = BeautifulSoup(req.text, 'html.parser')

#link = soup.find('div', {'class' : 'imgpt'})
links = soup.findAll('a', {'class' : 'thumb'})
for item in links:
    try :
        img_link = item.attrs['href']
        img = requests.get(img_link)
        img_name = img_link.split("/")[-1]
        i = Image.open(BytesIO(img.content))
        path = './' + dir_name + '/' + img_name
        i.save(path, i.format)
        print(img_name  + "      :      " + img_link)
    except :
        print("Couldn't save")