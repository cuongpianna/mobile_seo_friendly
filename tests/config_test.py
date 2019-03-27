import unittest
from base.browser_factory import WebDriverFactory


def get_driver():
    print("Running one time setUp")
    wdf = WebDriverFactory('chrome')
    driver = wdf.get_web_driver_instance('https://smallseotools.com/mobile-friendly-test/')
    return driver


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
