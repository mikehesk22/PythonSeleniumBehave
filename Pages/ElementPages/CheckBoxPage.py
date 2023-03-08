from selenium import webdriver
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from BaseClasses.BasePageClass import BasePage

class CheckBoxPage(BasePage):

    #region Elements    
    _homeToggle = (By.XPATH, "//span[@class='rct-text']/button")
    _expandAll = (By.XPATH, "//div[@class='rct-options']/button[@title='Expand all']")
    _collapseAll = (By.XPATH, "//div[@class='rct-options']/button[@title='Collapse all']")
    _homeCheckbox = (By.ID, "tree-node-home")
    _desktopCheckbox = (By.ID, "tree-node-desktop")
    _notesCheckbox = (By.ID, "tree-node-notes")
    _commandsCheckbox = (By.ID, "tree-node-commands")
    _documentsCheckbox = (By.ID, "tree-node-documents")
    _workspaceCheckbox = (By.ID, "tree-node-workspace")
    _reactCheckbox = (By.ID, "tree-node-react")
    _submitButton = (By.ID, "submit")
    #endregion

    def SelectHomeCheckbox(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._homeCheckbox)).click()

    
    def GetHeadingText(self):
        try:
            element = WebDriverWait(self.driver).until(EC.visibility_of_element_located((By.CLASS_NAME, "main-header")))
            return element.text
        except EX as e:
            print("Exception! Cannot return Element text")

    