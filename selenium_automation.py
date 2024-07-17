import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeleniumAutomation:
    '''
    Class to automate using selenium
    '''
    def __init__(self, driver=None) -> None:
        if not driver:
            driver = webdriver.Chrome()
        
        self.driver = driver

    def open(self):
            self.driver.get(self.url)

    
    def get_element(self, path, selector, driver):
        try:
            element = self.is_element_loaded(path, selector, driver)
            if element:
                return element
            else:
                print('Element could not be found at path', path)
                return
        except:
            pass

    def wait_and_get_element(self, path, selector, driver):
        for i in range(self.TIMEOUT):
            element = self.get_element(
                path=path,
                selector=selector,
                driver=driver
            )
            if element:
                return element
            else:
                time.sleep(i)
        else:
            print(f'Waited for {self.TIMEOUT} seconds,but could not find {path}')
            return
        
    
    def is_element_loaded(self, path,selector, driver):
        try:
            element = driver.find_element(selector, path)
            return element
        except:
            return False

        
    def random_delay(self, start = 2, end = 5):
        return random.randint(4, 10)


            
