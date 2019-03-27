import logging
import time

from base.base_page import BasePage
from utilities.custom_logger import custom_logger
from utilities.base import remove_http


class Home(BasePage):
    logger = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.msg = 'Test'
        self.url = 'https://theseotools.net/mobile-friendly-test'

    ################
    ### Locators ###
    ################

    # _url_textbox = ('url-input-field', 'id')
    # _check_button = ('url-input-button', 'id')
    # _result_container = ('result-section', 'id')
    # _result_text = ('conclusion', 'id')
    # _error = ('dgExError', 'id')

    _url_textbox = ('myurl', 'id')
    _check_button = ('checkButton', 'id')
    _result_container = ('mobileRes', 'classname')
    _result_text = ('//*[@id="results"]/div/table/tbody/tr[2]/td[2]', 'xpath')
    _error = ('dgExError', 'id')
    _url_error = ('//*[@id="results"]/div/div', 'xpath')

    #################
    ### Behaviors ###
    #################

    def get_url_textbox(self):
        return self.get_element(self._url_textbox[0], self._url_textbox[1])

    def get_check_button(self):
        return self.get_element(self._check_button[0], self._check_button[1])

    def get_result_container(self):
        return self.get_element(self._result_container[0], self._result_container[1])

    def get_result_text_element(self):
        return self.get_element(self._result_text[0], self._result_text[1])

    def get_url_error_element(self):
        return self.get_element(self._url_error[0], self._url_error[1])

    def get_error(self):
        return self.get_element(self._error[0], self._error[1])

    def get_result_text(self):
        result = self.get_result_text_element()
        return self.get_text(element=result)

    #################
    ### Interacts ###
    #################

    def go_to_this_page(self):
        self.driver.get(self.url)

    def enter_url_textbox(self, domain):
        textbox = self.get_url_textbox()
        self.send_keys(data=domain, element=textbox)

    def click_on_check_button(self):
        button = self.get_check_button()
        self.element_click(element=button)

    def check_domain(self, domain):
        self.enter_url_textbox(domain=domain)
        self.click_on_check_button()
        time.sleep(4)
        count = 1
        flag = True
        while flag:
            count = count + 1
            # error = self.get_error()
            # if self.is_element_displayed(element=error):
            #     flag = False
            #     count = 0
            container = self.get_result_container()
            if container:
                flag = False
            error = self.get_url_error_element()
            if error:
                self.driver.refresh()
                count = 0
            time.sleep(5)
            if count == 12:
                flag = False
                count = 0
        return count

    ################
    #### Verify ####
    ################

    def verify_domain(self, domain):
        count = self.check_domain(domain=domain)
        result_text = self.get_result_text()
        if count == 0:
            msg = 'Tool bị lỗi bất ngờ tại : {} :: PASS'.format(domain)
            self.go_to_this_page()
            return True, msg
        if 'Awesome! This page is mobile-friendly!' == result_text:
            msg = 'Kiểm tra domain trang : {} :: PASS'.format(domain)
            self.go_to_this_page()
            return True, msg
        elif result_text == 'Oh No! This page is not mobile-friendly.':
            msg = 'Trang: {} không thân thiện với mobile'.format(remove_http(domain))
            self.screen_shot(msg)
            self.go_to_this_page()
            return False, msg


class Home(BasePage):
    logger = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.msg = 'Test'
        self.url = 'https://smallseotools.com/mobile-friendly-test/'

    ################
    ### Locators ###
    ################

    # _url_textbox = ('url-input-field', 'id')
    # _check_button = ('url-input-button', 'id')
    # _result_container = ('result-section', 'id')
    # _result_text = ('conclusion', 'id')
    # _error = ('dgExError', 'id')

    _url_textbox = ('word', 'id')
    _check_button = ('//*[@id="mobile"]/div[3]/button', 'xpath')
    _result_container = ('mobileRes', 'classname')
    _result_text = ('//*[@id="results"]/div/table/tbody/tr[2]/td[2]', 'xpath')
    _error = ('dgExError', 'id')
    _url_error = ('//*[@id="results"]/div/div', 'xpath')

    #################
    ### Behaviors ###
    #################

    def get_url_textbox(self):
        return self.get_element(self._url_textbox[0], self._url_textbox[1])

    def get_check_button(self):
        return self.get_element(self._check_button[0], self._check_button[1])

    def get_result_container(self):
        return self.get_element(self._result_container[0], self._result_container[1])

    def get_result_text_element(self):
        return self.get_element(self._result_text[0], self._result_text[1])

    def get_url_error_element(self):
        return self.get_element(self._url_error[0], self._url_error[1])

    def get_error(self):
        return self.get_element(self._error[0], self._error[1])

    def get_result_text(self):
        result = self.get_result_text_element()
        return self.get_text(element=result)

    #################
    ### Interacts ###
    #################

    def go_to_this_page(self):
        self.driver.get(self.url)

    def enter_url_textbox(self, domain):
        textbox = self.get_url_textbox()
        self.send_keys(data=domain, element=textbox)

    def click_on_check_button(self):
        button = self.get_check_button()
        self.element_click(element=button)

    def check_domain(self, domain):
        self.enter_url_textbox(domain=domain)
        self.click_on_check_button()
        time.sleep(4)
        count = 1
        flag = True
        while flag:
            count = count + 1
            # error = self.get_error()
            # if self.is_element_displayed(element=error):
            #     flag = False
            #     count = 0
            container = self.get_result_container()
            if container:
                flag = False
            error = self.get_url_error_element()
            if error:
                self.driver.refresh()
                count = 0
            time.sleep(5)
            if count == 12:
                flag = False
                count = 0
        return count

    ################
    #### Verify ####
    ################

    def verify_domain(self, domain):
        count = self.check_domain(domain=domain)
        result_text = self.get_result_text()
        if count == 0:
            msg = 'Tool bị lỗi bất ngờ tại : {} :: PASS'.format(domain)
            self.go_to_this_page()
            return True, msg
        if 'Awesome! This page is mobile-friendly!' == result_text:
            msg = 'Kiểm tra domain trang : {} :: PASS'.format(domain)
            self.go_to_this_page()
            return True, msg
        elif result_text == 'Oh No! This page is not mobile-friendly.':
            msg = 'Trang: {} không thân thiện với mobile'.format(remove_http(domain))
            self.screen_shot(msg)
            self.go_to_this_page()
            return False, msg

