from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from BaseClasses.BasePageClass import BasePage
from  selenium.webdriver.support.ui import  WebDriverWait

class TextBoxPage(BasePage):
    #region Elements    
    _name = (By.ID, "userName")
    _email = (By.ID, "userEmail")
    _currentAddress = (By.ID, "currentAddress")
    _permanentAddress = (By.ID, "permanentAddress")
    _submitButton = (By.ID, "submit")
    _pageHeading = (By.CLASS_NAME, "main-header")
    #endregion

    def EnterName(self):
        super().EnterData(self._name, "Name")


    def EnterEmail(self):
        super().EnterData(self._email, "Name@email.com")

    
    def EnterCurrentAddress(self):
        super().EnterData(self._currentAddress, "1 close")


    def EnterPermanentAddress(self):
        super().EnterData(self._permanentAddress, "2 road")
        

    def ClickSubmit(self):
        super().Click(self._submitButton)


    def GetHeadingText(self):
        super().ReturnElementText(self._pageHeading)

   
