# bot.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import username, password
from utils import wait_for_element, click_element
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        wait_for_element(self.driver, By.NAME, 'username')
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)

        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        submit_button.click()
        time.sleep(10)

    def wait_for_element(self, driver, by, value):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))

    def close(self):
        self.driver.quit()

    def dismiss_notification_prompt(self):
        try:
            # Wait for the notification prompt to appear
            not_now_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1'))
            )
            print("Notification prompt found!")
            time.sleep(5)
            not_now_button.click()
            time.sleep(5)
            print("Clicked 'Not Now' button successfully!")
            time.sleep(5)
        except TimeoutException:
            print("Notification prompt not found!")
            # If the prompt doesn't appear, do nothing
            pass
        

    def search_for_id(self, id_to_search):
       
        try:
            # Click on the search icon
            search_icon = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Search"]'))
            )
            print("Search icon found!")
            time.sleep(2)
            search_icon.click()
            time.sleep(2)

            # Wait for the page to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # Enter the ID in the search field
            search_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search"]'))
            )
            print("Search field found!")
            time.sleep(2)
            search_field.send_keys(id_to_search)
            time.sleep(2)
            search_field.send_keys(Keys.ENTER)
            time.sleep(2)
            search_field.send_keys(Keys.ENTER)
            print("ENTER key pressed twice.")

            # Click on the first result
            first_result_xpath = f"//a[contains(@href, '/{id_to_search.lower()}/')]"
            first_result = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, first_result_xpath))
            )
            if first_result:
                print("First result found!")
                time.sleep(2)
                first_result.click()
                time.sleep(5)
            else:
                print("First result not found.")

        except NoSuchElementException as e:
            print("No such element exception:", str(e))
        except TimeoutException as e:
            print("Timeout exception:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))

    

    def follow_user(self):
        try:
            # Use XPath to find the button containing the text "Follow"
            follow_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button//div[text()="Follow"]'))
            )

            if follow_button:
                print("Follow button found")
                time.sleep(3)
                follow_button.click()
                print("Followed the user successfully!")
                time.sleep(5)
            else:
                print("Follow button not found or already following.")
        except NoSuchElementException as e:
            print("No such element exception:", str(e))
        except TimeoutException as e:
            print("Timeout exception:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))

    def like_post(self):
        try:
            # Use XPath to find the button containing the text "Follow"
            like_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button//div[text()="Follow"]'))
            )

            if like_button:
                print("Follow button found")
                time.sleep(3)
                like_button.click()
                print("Followed the user successfully!")
                time.sleep(5)
            else:
                print("Follow button not found or already following.")
        except NoSuchElementException as e:
            print("No such element exception:", str(e))
        except TimeoutException as e:
            print("Timeout exception:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))



if __name__ == '__main__':
    bot = InstagramBot(username, password)
    bot.login()
    bot.dismiss_notification_prompt()
    bot.search_for_id("_rohanshrma")
    bot.follow_user()
