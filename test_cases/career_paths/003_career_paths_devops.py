from selenium import webdriver
import sys
import os

# Add necessary paths to sys.path using relative paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir_1 = os.path.dirname(current_dir)
parent_dir_2 = os.path.dirname(parent_dir_1)
sys.path.insert(0, os.path.join(parent_dir_2, 'page_classes'))
sys.path.insert(0, os.path.join(parent_dir_2, 'common'))

# Import custom classes
from page_class import Page
from career_paths import CareerPaths
from common_class import Common_class
import random
import string
import time

# Initialize the driver
driver = webdriver.Chrome()
base_url = "https://stg.heroco.am"
career_paths_url = f"{base_url}/#careerPaths"
career_paths_page = CareerPaths(career_paths_url, driver)
career_paths_page.open_browser()

career_paths_page.click_devops()
assert driver.current_url == f"{base_url}/career-paths/devops_path", "Wrong url for devops_path"

time.sleep(5)

career_paths_page.click_devops_cs()
assert driver.current_url == f"{base_url}/courses/cs", "Wrong url for DevOps Computer Science page"

time.sleep(5) 
driver.back()

career_paths_page.click_devops_python()
assert driver.current_url == f"{base_url}/courses/python", "Wrong url for DevOps Python page"

time.sleep(5)
driver.back()

career_paths_page.click_devops_devops()
assert driver.current_url == f"{base_url}/courses/devops", "Wrong url for DevOps DevOps page"

time.sleep(5)
driver.back()

common = Common_class()
mail = f'{common.get_random_string(8)}@test.com'
career_paths_page.fill_form_devops("name", mail, "+37412345678")

time.sleep(5)
assert career_paths_page.get_success_message() == "Thank you for your application!", "Wrong success message upon apply process" 