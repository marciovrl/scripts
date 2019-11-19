from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time


class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def go_url(self, url):
        self.driver.get(url)

    def sleep(self, time_sleep):
        time.sleep(time_sleep)

    def get_element(self, *locator):
        return WebDriverWait(self.driver, 50).until(ec.visibility_of_element_located((locator[0], locator[1])))

    def input_text(self, text, *locator):
        self.get_element(*locator).send_keys(text)

    def click(self, *locator):
        self.get_element(*locator).click()

    def switch_frame(self, *locator):
        element = self.get_element(*locator)
        self.driver.switch_to.frame(element)
