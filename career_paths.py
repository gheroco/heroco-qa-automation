from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select;
from xpaths import Xpaths

from page_class import Page
import time

class CareerPaths(Page):
    
    def click_front_end(self):
        self.wait_until_visible(Xpaths.front_end)
        front_end_element = self.find_element_by_xpath(Xpaths.front_end)
        self.click_to_element(front_end_element)