from ast import main
import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import youtubePage  as page
import sys
from webdriver_manager.chrome import ChromeDriverManager

class YoutubeSearch(unittest.TestCase): 
    def setUp(self): 
        self.driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
    
    def tearDown(self): 
        self.driver.close()

    # def test_main(self): 
    #     print("Hello")
    #     return "Hi"


    # def test_example(self): 
    #     #will automatically run if test is in front
    #     assert True

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_match()
        mainPage.search_text_element = "10 Second Timer"
        mainPage.click_search_button()
        assert self.driver.title in "10 second timer - YouTube"
    
    # def test_title(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.is_title_match()


if __name__ == '__main__':
   unittest.main()