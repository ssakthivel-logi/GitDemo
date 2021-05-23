from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    card_title = (By.CSS_SELECTOR, "div[class='card h-100']")
    card_footer = (By.XPATH, "div/button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    final_checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCartTitles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    # product.find_element_by_xpath("div/button").click()
    def getCartFooter(self):
        return self.driver.find_element(*CheckoutPage.card_footer)

    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    def clickCheckout(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.final_checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

