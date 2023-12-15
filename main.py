from selenium import webdriver
from page_class import Page
from home_page_class import HomePage
from apply_now_class import ApplyNow
import time

driver = webdriver.Chrome()
site_base_url = "https://heroco.am"
apply_now_url = "https://heroco.am/#apply"

heroco_page = Page(site_base_url, driver)
heroco_page.open_browser()

home_page = HomePage(site_base_url, driver)
home_page.click_to_apply_now()

apply_now_page = ApplyNow(apply_now_url, driver)
apply_now_page.fill_form("name", "test@mail.com", "1234567890")
time.sleep(10)

heroco_page.go_to_homepage()

heroco_page.close_browser()