from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_ICONBUTTON_LOCATOR = (By.ID, "search-icon-legacy")

class SearchResultsPageLocator(object):
    FIRST_VIDEO_LOCATOR = (By.XPATH, "//*[@id='contents']/ytd-video-renderer[1]")
    SECOND_VIDEO_LOCATOR = (By.XPATH, "//*[@id='contents']/ytd-video-renderer[2]")