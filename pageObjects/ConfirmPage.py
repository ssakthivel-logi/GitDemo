from selenium.webdriver.common.by import By


class ConfirmPage:
    country_field = (By.CSS_SELECTOR, "#country")
    country_india = (By.LINK_TEXT, "India")

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("#country").send_keys("ind")
    def countryName(self):
        return self.driver.find_element(*ConfirmPage.country_field)

    # self.driver.find_element_by_link_text("India").click()
    def countrySelection(self):
        return self.driver.find_element(*ConfirmPage.country_india)
