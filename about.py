from xpaths import Xpaths
from selenium.webdriver.support.wait import WebDriverWait 

from page_class import Page
import time

class About(Page):
    '''
        This class is inherited from Page class and contains methods related to About tab
    '''
    def click(self, xpath):
        html_css_element = self.find_element_by_xpath(xpath)
        self.click_to_element(html_css_element)
    
    def click_karo_muradyan(self):
        self.click(Xpaths.karo)
    
    def click_smbat_poghosyan(self):
        self.click(Xpaths.smbat)
    
    def click_vahe_petrosyan(self):
        self.click(Xpaths.vahe)

    def click_georgi_khalatyan(self):
        self.click(Xpaths.georgi)
    
    def click_vardges_vardanyan(self):
        self.click(Xpaths.vardges)