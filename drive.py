from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import requests


class Driver():
    def __init__(self):
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.headless = True
        self.navegador = webdriver.Firefox(options=firefoxOptions)
        
    def go_url(self, url):
        self.navegador.get(url)
        
    def fechar(self):
        self.navegador.quit()
        
    def get_links(self):
        page_itens = self.navegador.find_elements_by_css_selector(
           "a[class='ui-search-link']" 
        )
        
        itens = []
        for link in page_itens:
            tmp = link.get_attribute('href')
            itens.append(tmp)
        return itens

    def get_data(self, url):
        data = {}
        req = requests.get(url)
        page = req.text
        soup = BeautifulSoup(page, 'lxml')
        item_title = soup.find('h2', class_='ui-search-item__title').get_text().strip()
        item_price = soup.find('span', class_='price-tag-fraction').get_text().strip
        data['item_title'] = item_title
        data['item_price'] = item_price
        return data

