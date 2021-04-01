from selenium import webdriver

class Driver():
    def __init__(self):
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.headless = True
        self.navegador = webdriver.Firefox(options=firefoxOptions)
        
    def go_url(self, url):
        self.navegador.get(url)
        
    def fechar(self):
        self.navegador.quit()
        

URL = 'https://lista.mercadolivre.com.br/nintendo-switch#D[A:nintendo%20switch]'

navegador = Driver()
navegador.go_url(URL)
navegador.fechar()