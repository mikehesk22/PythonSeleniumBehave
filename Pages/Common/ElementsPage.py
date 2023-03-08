from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from BaseClasses.BasePageClass import BasePage

class ElementsPage(BasePage):
    #region Elements    
    _textBoxLink = (By.XPATH, "//span[text()='Text Box')]")
    _checkBoxLink = (By.XPATH, "//span[text()='Check Box')]")
    _radioButtonLink = (By.XPATH, "//span[text()='Radio Button')]")
    _webTablesLink = (By.XPATH, "//span[text()='Web Tables')]")
    _buttonsLink = (By.XPATH, "//span[text()='Buttons')]")
    _linksLink = (By.XPATH, "//span[text()='Links']")
    _brokenLinksLink = (By.XPATH, "//span[text()='Broken Links - Images']")
    #endregion

    def ClickOnTextBoxLink(self):
        BasePage.click(self._textBoxLink)


    def ClickOnCheckBoxLink(self):
        BasePage.click(self._checkBoxLink)


    def ClickOnRadioButtonLink(self):
        BasePage.click(self._radioButtonLink)


    def ClickOnWebTablesLink(self):
        BasePage.click(self._webTablesLink)


    def ClickOnButtonsLink(self):
        BasePage.click(self._buttonsLink)


    def ClickOnLinksLink(self):
        BasePage.click(self._linksLink)