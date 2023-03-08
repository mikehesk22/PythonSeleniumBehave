from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class BaseClass():

    def ChromeOptions():
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        return driver
    
    
    def FirefoxOptions():
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
        return driver
    

    def EdgeOptions():
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)
        return driver