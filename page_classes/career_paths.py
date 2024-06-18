from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.common.action_chains import ActionChains

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

    def click_front_end_cs(self):
        front_end_cs_element = self.find_element_by_xpath(Xpaths.front_end_cs)
        actions = ActionChains(self.driver)
        actions.move_to_element(front_end_cs_element).perform()
        self.wait_until_visible(Xpaths.front_end_cs)
        self.click_to_element(front_end_cs_element)

    def click_front_end_html(self):
        front_end_html_element = self.find_element_by_xpath(Xpaths.front_end_html)
        actions = ActionChains(self.driver)
        actions.move_to_element(front_end_html_element).perform()
        self.wait_until_visible(Xpaths.front_end_html)
        self.click_to_element(front_end_html_element)

    def click_front_end_js(self):
        front_end_js_element = self.find_element_by_xpath(Xpaths.front_end_js)
        actions = ActionChains(self.driver)
        actions.move_to_element(front_end_js_element).perform()
        self.wait_until_visible(Xpaths.front_end_js)
        self.click_to_element(front_end_js_element)
    
    def click_front_end_react(self):
        front_end_react_element = self.find_element_by_xpath(Xpaths.front_end_react)
        actions = ActionChains(self.driver)
        actions.move_to_element(front_end_react_element).perform()
        self.wait_until_visible(Xpaths.front_end_react)
        self.click_to_element(front_end_react_element)

    def fill_form(self, name, email, phone):
        #Used to fill out "Apply Now" form using given data
        name_element = self.find_element_by_xpath(Xpaths.name_career_paths)
        actions = ActionChains(self.driver)
        actions.move_to_element(name_element).perform()
        name_element = self.find_element_by_xpath(Xpaths.name_career_paths)
        self.click_to_element(name_element)
        self.input_text(name_element, name)
        email_element = self.find_element_by_xpath(Xpaths.email_career_paths)
        self.click_to_element(email_element)
        self.input_text(email_element, email)
        phone_element = self.find_element_by_xpath(Xpaths.phone_career_paths)
        self.click_to_element(phone_element)
        self.input_text(phone_element, phone)
        career_element = self.find_element_by_xpath(Xpaths.career_career_paths)
        self.click_to_element(career_element)
        value_element = self.find_element_by_xpath(Xpaths.career_value_career_paths)
        self.click_to_element(value_element)
        connect_element = self.find_element_by_xpath(Xpaths.connect_button_career_paths)
        self.click_to_element(connect_element)
        
    def get_success_message(self):
        success_message_element = self.find_element_by_xpath(Xpaths.success_message)
        return self.get_text(success_message_element)