from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def element_type(self,text_value,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text_value)

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def element_status_check(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.is_displayed()

    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        return element