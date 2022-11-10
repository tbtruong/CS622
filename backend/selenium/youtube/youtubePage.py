from youtubeLocator import *
from youtubeElement import BasePageElement
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class SearchTextElement(BasePageElement):
    locator = '//input[@id="search"]'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    #Searchbar instantiation
    search_text_element = SearchTextElement()  
    
    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_ICONBUTTON_LOCATOR)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
    
    def getResults(self):
        results = []

        #
        WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element(*SearchResultsPageLocator.FIRST_VIDEO_LOCATOR))
        firstVideo = self.driver.find_element(*SearchResultsPageLocator.FIRST_VIDEO_LOCATOR)
        firstVideo.click()
        results.append(self.driver.current_url)
        self.driver.back()
    
        # self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()
        WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element(*SearchResultsPageLocator.SECOND_VIDEO_LOCATOR))
        time.sleep(10)
        # print(results)
        # time.sleep(5)

        secondVideo = self.driver.find_element(*SearchResultsPageLocator.SECOND_VIDEO_LOCATOR)
        secondVideo.click()
        results.append(self.driver.current_url)
        time.sleep(10)

        return results
        
       



