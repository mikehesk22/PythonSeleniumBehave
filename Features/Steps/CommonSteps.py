from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from Pages.Common import ElementsPage
from Pages.ElementPages import TextBoxPage
from Pages.ElementPages.CheckBoxPage import CheckBoxPage
from BaseClasses.BasePageClass import BasePage

@given('I launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path="C:\Python311\Scripts\chromedriver.exe")


@when('I navigate to site')
def goToSite(context):
    context.driver.get("https://demoqa.com/elements")


@when('I click {linkText} link')
def step_impl(context, linkText):
    if linkText.lower() == "text box":
        ElementsPage.ClickOnTextBoxLink()
        context.linkText == "text box"
    elif linkText.lower() == "check box":
        ElementsPage.ClickOnCheckBoxLink()
    elif linkText.lower() == "radio button":
        ElementsPage.ClickOnRadioButtonLink()

@then('I verify I am on {page} page')
def verifyPage(context, page):
    if page.lower() == "text box":
        pageHeading = TextBoxPage.GetHeadingText()
        assert pageHeading == page.title()
    elif page.lower() == "check box":
        pageHeading = CheckBoxPage.GetHeadingText()
        assert pageHeading == page.title()
    elif page.lower() == "radio button":
        ElementsPage.ClickOnRadioButtonLink()


@then('Close the browser')
def closeBrowser(context):
    context.driver.close()