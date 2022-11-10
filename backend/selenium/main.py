from ast import main
import sys
import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import page
from webdriver_manager.chrome import ChromeDriverManager

class PythonOrgSearch(unittest.TestCase): 
    def setUp(self): 
        self.driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.google.com/")
    
    def tearDown(self): 
        self.driver.close()


    def test_example(self): 
        #will automatically run if test is in front
        assert True

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_match()
        mainPage.search_text_element = "What to search for"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found
    
    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_match()


if __name__ == '__main__':
    # unittest.main()
    print(sys.argv[1])
    print("Hey man")