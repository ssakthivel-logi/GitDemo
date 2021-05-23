from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name_field = (By.NAME, "name")
    email_field = (By.XPATH, "//input[@name='email']")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    checkbox = (By.ID, "exampleCheck1")
    submit_button = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def shop_item(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    # self.driver.find_element_by_name("name").send_keys("Srinivasan")
    def getName(self):
        return self.driver.find_element(*HomePage.name_field)

    # self.driver.find_element_by_xpath("//input[@name='email']").send_keys("test@email.com")
    def getEmail(self):
        return self.driver.find_element(*HomePage.email_field)

    # self.driver.find_element_by_id("exampleFormControlSelect1"))
    def getGender(self):
        return self.driver.find_element(*HomePage.gender_dropdown)

    # self.driver.find_element_by_id("exampleCheck1").click()
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    # self.driver.find_element_by_xpath("//input[@type='submit']")
    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit_button)

    # self.driver.find_element_by_class_name("alert-success")
    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)



