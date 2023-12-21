from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage

class SearchPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    valid_search_product_link_text = "HP LP3065"
    invalid_search_product_xpath = "//input[@id='button-search']/following-sibling::p"

    def valid_search_product(self):
        return self.element_status_check("valid_search_product_link_text",self.valid_search_product_link_text)

    def invalid_search_product(self):
        return self.driver.find_element(By.XPATH,self.invalid_search_product_xpath).text
