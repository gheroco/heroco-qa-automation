from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from xpaths import Xpaths

from page_class import Page
import time

class ApplyNow(Page):
    
    def fill_form(self, name, email, phone):
        name_element = self.find_element_by_xpath(Xpaths.name)
        self.click_to_element(name_element)
        self.input_text(name_element, name)
        email_element = self.find_element_by_xpath(Xpaths.email)
        self.click_to_element(email_element)
        self.input_text(email_element, email)
        phone_element = self.find_element_by_xpath(Xpaths.phone)
        self.click_to_element(phone_element)
        self.input_text(phone_element, phone)
        career_element = self.find_element_by_xpath(Xpaths.career)
        self.click_to_element(career_element)
        value_element = self.find_element_by_xpath(Xpaths.career_value)
        self.click_to_element(value_element)
        connect_element = self.find_element_by_xpath(Xpaths.connect_button)
        self.click_to_element(connect_element)

