from selenium import webdriver
from page_class import Page
from home_page import HomePage
from apply_now import ApplyNow
from career_paths import CareerPaths
import time

driver = webdriver.Chrome()
site_base_url = "https://heroco.am"
apply_now_url = "https://heroco.am/#apply"
career_paths_url = "https://heroco.am/#careerPaths"

heroco_page = Page(site_base_url, driver)
heroco_page.open_browser()

home_page = HomePage(site_base_url, driver)
home_page.click_to_apply_now()

apply_now_page = ApplyNow(apply_now_url, driver)
apply_now_page.fill_form("name", "test@mail.com", "+37412345678")

career_paths = CareerPaths(career_paths_url, driver)
career_paths.click_front_end()
time.sleep(10)

heroco_page.close_browser()