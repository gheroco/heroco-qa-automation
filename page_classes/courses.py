from xpaths import Xpaths
from selenium.webdriver.support.wait import WebDriverWait 

from page_class import Page
import time

class Courses(Page):
    '''
        This class is inherited from Page class and contains methods related to Courses tab
    '''
    def click(self, xpath):
        html_css_element = self.find_element_by_xpath(xpath)
        self.click_to_element(html_css_element)

    def click_html_css(self):
        self.click(Xpaths.html_css)
    
    def click_javascript(self):
        self.click(Xpaths.javascript)
    
    def click_reactjs(self):
        self.click(Xpaths.reactjs)
    
    def click_android(self):
        self.click(Xpaths.androidcourse)
    
    def click_nodejs(self):
        self.click(Xpaths.nodejs)

    def click_kotlin(self):
        self.click(Xpaths.kotlin)

    def click_expand(self):
        self.click(Xpaths.expand_button)

    def click_java(self):
        self.click(Xpaths.java)

    def click_algorithms_and_ds(self):
        self.click(Xpaths.algorithms_and_ds)

    def click_computer_science(self):
        self.click(Xpaths.computer_science)
    
    def click_machine_learning(self):
        self.click(Xpaths.machine_learning)

    def click_databases(self):
        self.click(Xpaths.databases)
    
    def click_devops_course(self):
        self.click(Xpaths.devops_course)

    def click_python(self):
        self.click(Xpaths.python)

    def click_manual_qa(self):
        self.click(Xpaths.manual_qa)


