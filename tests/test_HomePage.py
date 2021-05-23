import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getlogger()
        # self.driver.find_element_by_name("name").send_keys("Srinivasan")
        # driver.find_element_by_css_selector("input[name='name']").send_keys("Srinivasan")
        home_page = HomePage(self.driver)
        log.debug("Firstname is "+getData["firstname"])
        home_page.getName().send_keys(getData["firstname"])
        # self.driver.find_element_by_xpath("//input[@name='email']").send_keys("test@email.com")
        home_page.getEmail().send_keys(getData["email"])
        # select the dropdown values
        self.selectOptionByText(home_page.getGender(), getData["gender"])
        # dropdown = Select(home_page.getGender())
        # dropdown.select_by_index(1)
        time.sleep(3)

        # self.driver.find_element_by_id("exampleCheck1").click()
        home_page.getCheckbox().click()
        # self.driver.find_element_by_xpath("//input[@type='submit']").click()
        home_page.clickSubmit().click()

        print(home_page.getAlert().text)
        message = home_page.getAlert().text
        log.info("Text received is" + message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param
