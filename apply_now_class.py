from selenium.webdriver.common.by import By
from selenium import webdriver
from page_class import Page
import time

class ApplyNow(Page):
    
    def fill_form(self, name, email, phone):
        name_element = self.find_element_by_xpath('//*[@id="__next"]/main/div/div[2]/section/div[1]/div[2]/form/label[1]/input')
        self.click_to_element(name_element)
        self.input_text(name_element, name)
        email_element = self.find_element_by_xpath('//*[@id="__next"]/main/div/div[2]/section/div[1]/div[2]/form/label[2]/input')
        self.click_to_element(email_element)
        self.input_text(email_element, email)
        phone_element = self.find_element_by_xpath('//*[@id="__next"]/main/div/div[2]/section/div[1]/div[2]/form/label[3]/input')
        self.click_to_element(phone_element)
        self.input_text(phone_element, phone)

