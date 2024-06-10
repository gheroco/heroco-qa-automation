from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select;
from xpaths import Xpaths

from page_class import Page
import time

class CareerPaths(Page):
    '''
        This class is inherited from Page class and contains methods related to Career Paths tab
    '''
    def click_front_end(self):
        #Used to click on Front End section

        self.wait_until_visible(Xpaths.front_end)
        front_end_element = self.find_element_by_xpath(Xpaths.front_end)
        self.click_to_element(front_end_element)
    
    def click_back_end(self):
        #Used to click on Back End section

        self.wait_until_visible(Xpaths.back_end)
        back_end_element = self.find_element_by_xpath(Xpaths.back_end)
        self.click_to_element(back_end_element)

    def click_devops(self):
        #Used to click on Devops section

        self.wait_until_visible(Xpaths.devops)
        devops_element = self.find_element_by_xpath(Xpaths.devops)
        self.click_to_element(devops_element)

    def click_data_science(self):
        #Used to click on Data Science section

        self.wait_until_visible(Xpaths.data_science)
        data_science_element = self.find_element_by_xpath(Xpaths.data_science)
        self.click_to_element(data_science_element)

    def click_android(self):
        #Used to click on Android section

        self.wait_until_visible(Xpaths.android)
        android_element = self.find_element_by_xpath(Xpaths.android)
        self.click_to_element(android_element)