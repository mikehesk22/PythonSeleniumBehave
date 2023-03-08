from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

   
    def Click(self, by_locator):
        try:
            WebDriverWait(self.driver).until(EC.presence_of_element_located(by_locator)).click()
        except EX as e:
            print("Exception! Can't click on the element")

    
    def EnterData(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except EX as e:
            print("Exception! Can't enter data")

    
    def ReturnElementText(self, by_locator):
        try:
            element = WebDriverWait(self.driver).until(EC.visibility_of_element_located((by_locator)))
            return element.text
        except EX as e:
            print("Exception! Cannot return Element text")


    def GetPageTitle(self):
        return self.driver.title
