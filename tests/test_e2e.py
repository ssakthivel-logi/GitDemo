from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        # self.driver.find_element_by_link_text("Shop").click()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_item()

        log.info("Selecting all the products")
        # products = self.driver.find_elements_by_css_selector("div[class='card h-100']")
        # checkout_page = CheckoutPage(self.driver)
        products = checkout_page.getCartTitles()
        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            if product_name == "Blackberry":
                log.info("Add item to the cart")
                product.find_element_by_xpath("div/button").click()
                # checkout_page.getCartTitles()[i].click()
        checkout_page.clickCheckout().click()
        log.info("clicking on the check out button")
        confirm_page = checkout_page.checkoutItems()
        log.info("entering the country name")
        # confirm_page = ConfirmPage(self.driver)
        confirm_page.countryName().send_keys("ind")
        # explict wait for country search
        self.verifyElementLocatedUsingLinkText("India")
        log.info("selecting india country")
        log.info("selecting india country2")
        confirm_page.countrySelection().click()
        # clicking on checkbox
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        # clicking on the purchase button
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        log.debug("checking whether order is placed successfully")
        self.verifyElementLocatedUsingClassName("alert-success")
        success_message = self.driver.find_element_by_class_name("alert-success").text
        # assert success_message == 'Success! Thank you! Your order will be delivered in next few weeks :-).'
        log.info("Test Received is " + success_message)
        assert 'Success1' in success_message
