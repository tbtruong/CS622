from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePageElement(object):
    def __set__(self, obj, value):
        #The class the object is defined in is passed as the object (MainPage)
        #Search_text_element = 5 (5 is value)
        print(value)
        print(self.locator)
        driver = obj.driver
        WebDriverWait(driver, 1000).until(
            lambda driver: driver.find_element(By.XPATH, self.locator))
        # driver.find_element(By.ID, self.locator).clear()
        # driver.find_element(By.ID, self.locator).send_keys(value)
        driver.find_element(By.XPATH, self.locator).clear()
        driver.find_element(By.XPATH, self.locator).send_keys(value)
    
    def __get__(self, obj, owner):
        #x = search_text_element
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

