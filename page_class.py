from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import time

class Page:
    # constructor of the class includes instance variable for default wait time of 20 seconds
    def __init__(self, url, driver):
        self.base_url = url
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_browser(self):
        # This method opens browser navigating to the base url given during initialization of the class
        self.driver.get(self.base_url)

    def navigate_to_url(self, url):
        # This method navigates to the url given at the time of calling the method
        self.driver.get(url)
        
    def find_element_by_xpath(self, xpath):
        #This method returns the element found using given xpath
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except selenium.common.exceptions.NoSuchElementException:
            print (f"Element with following xpath could not be found: {xpath}")
    
    def click_to_element(self, element):
        element.click()

    def input_text(self, element, input_text):
        #This method is used to input given text into the given element
        element.send_keys(input_text)

    def get_text(self, element):
        #This method is used to get the text within given element
        return element.text

    def element_is_displayed(self, element):
        #This method returns True if given element is displayed and False otherwise
        try:
            return element.is_displayed()
        except AttributeError:
            print(f"Element locator is not found")

    def wait_until_visible(self, xpath):
        #This method is used to trigger wait until element located by the given xpath is visible
        element_locator = (By.XPATH, xpath)
        try:
            element = self.wait.until(EC.visibility_of_element_located(element_locator))
            return element
        except selenium.common.exceptions.TimeoutException:
            print (f"Timeout occurred, element with following locator is not visible: {element_locator}")

    def go_to_homepage(self):
        #Used to go to website home page
        self.driver.get(self.base_url)
        self.home_page_button = self.driver.find_element(By.CLASS_NAME, 'gap-2')
        self.click_to_element(self.home_page_button)

    def close_browser(self):
        self.driver.close()