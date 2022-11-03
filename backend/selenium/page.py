from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    #The class the object is defined in is passed as the object (MainPage)
    #Search_text_element = 5 (5 is value)
    search_text_element = SearchTextElement()  

    def is_title_match(self):
        return "String" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON_LOCATOR)
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source


