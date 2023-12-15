from selenium.webdriver.common.by import By
from selenium import webdriver
from page_class import Page
import time

class HomePage(Page):

    def click_to_apply_now(self):
        element = self.find_element_by_xpath('//*[@id="__next"]/main/div/div[1]/section/div[1]/a')
        self.element_is_displayed(element)
        self.wait_until_visible('//*[@id="__next"]/main/nav/div/a/img')
        self.click_to_element(element)
        time.sleep(10)

