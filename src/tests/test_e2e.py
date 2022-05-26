import unittest
import ddt
from selenium import webdriver

from time import sleep

URL = 'http://localhost:5000'

@ddt.ddt
class TestStringMethods(unittest.TestCase):

    @ddt.data(
            (50, '1£'),
            (2000, 'N/A')
    )
    def test_before_one_hour(self, case):
        duration, payment = case

        self.type_into_input("duration_input", duration)
        self.click_on_the_element("submit_button")
        result = self.get_element_text("amount")

        self.assertEqual(result, f"You have to pay: {payment}")






    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(URL)
        self.driver.maximize_window()
        

    def tearDown(self):
        self.driver.close()

    def type_into_input(self, locator, text):
        duration_field = self.driver.find_element_by_id(locator)
        duration_field.send_keys(text)
    
    def click_on_the_element(self, locator):
        self.driver.find_element_by_id(locator).click()

    def get_element_text(self, locator):
        return self.driver.find_element_by_id(locator).text
