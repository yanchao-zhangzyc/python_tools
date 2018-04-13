from bs4 import BeautifulSoup
import requests
from selenium import webdriver

url="https://w2.hoopchina.com.cn/75/f0/ea/75f0ea6a1616b06cffb641aeaaf3f5c3001.jpg"
pic_html=requests.get(url)
with open('1.jpg','wb') as fp:
    fp.write(pic_html.content)
    fp.close()




