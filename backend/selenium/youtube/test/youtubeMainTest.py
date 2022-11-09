from ast import main
import threading
import traceback
# import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import youtubePage  as page
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class YoutubeSearch(unittest.TestCase): 
    def __init__(self): 
        self.driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()

    # def test_main(self): 
    #     print("Hello")
    #     return "Hi"


    # def test_example(self): 
    #     #will automatically run if test is in front
    #     assert True

    def test_search_python(self, link):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_match()
        mainPage.search_text_element = link
        mainPage.click_search_button()
        assert self.driver.title in "10 second timer - YouTube"
        self.driver.quit()
        print("hello")
        resultsPage = page.SearchResultPage(self.driver)
    
    # def test_title(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.is_title_match()


if __name__ == '__main__':
    unittest.main()