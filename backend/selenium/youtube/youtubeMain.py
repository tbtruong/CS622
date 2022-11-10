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
import subprocess

class YoutubeSearch(): 
    def __init__(self): 
        self.driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()

    
    def __enter__(self):
        return self
       
    def __exit__(self, exc_type, exc_val, exc_tb): 
        print("Exit called")
        self.driver.close()
        self.driver.quit()

    def enter_search(self, searchTerm):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = searchTerm
        mainPage.click_search_button()

    def get_results(self):
         resultsPage = page.SearchResultPage(self.driver)
         results = resultsPage.getResults()
         return results
    

if __name__ == '__main__':
    searchTerm =  sys.argv[1]

    with YoutubeSearch() as bot: 
        bot.enter_search(searchTerm)
        results = bot.get_results()
        print(results)
        subprocess.run(["yt-dlp", results[0]])
        subprocess.run(["yt-dlp", results[1]])

       
