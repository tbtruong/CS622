from youtubeLocator import *
from youtubeElement import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"
    # locator = "search-form"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    #The class the object is defined in is passed as the object (MainPage)
    #Search_text_element = 5 (5 is value)
    search_text_element = SearchTextElement()  

    def is_title_match(self):
        return "YouTube" in self.driver.title
    
    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_ICONBUTTON_LOCATOR)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source


