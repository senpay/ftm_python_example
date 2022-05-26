import unittest
import ddt
from selenium import webdriver

from time import sleep

URL = 'http://localhost:5000'

@ddt.ddt
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(URL)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    @ddt.data(
            (50, '1£'),
            (59, '1£'),
            (60, '1£'),
            (61, '1£40p'),
            (180, '2£10p'),
            (200, '2£80p'),
            (239, '2£80p'),
            (240, '2£80p'),
            (241, '15£'),
            (300, '15£'),
            (1440, '15£')
    )
    def test_before_one_hour(self, case):
        duration, payment = case
        duration_field = self.driver.find_element_by_id("duration_input")
        duration_field.send_keys(duration)
        self.driver.find_element_by_id("submit_button").click()
        result = self.driver.find_element_by_id("amount")
        self.assertEqual(result.text, f"You have to pay: {payment}")
