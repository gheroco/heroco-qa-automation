from selenium.webdriver.common.by import By
from selenium import webdriver
from page_class import Page
from xpaths import Xpaths
import time

class HomePage(Page):
    '''
        This class is inherited from Page class and contains methods related to home page
    '''

    def click_to_apply_now(self):
        
        #Used to click on "Apply Now" button

        element = self.find_element_by_xpath(Xpaths.apply_now)
        self.element_is_displayed(element)
        self.click_to_element(element)
        time.sleep(10)