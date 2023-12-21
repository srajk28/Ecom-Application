from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage
from PageObject.LoginPage import LoginPage
from PageObject.RegisterPage import RegisterPage
from PageObject.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    enter_product_search_box_name = "search"
    click_search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    click_my_account_drop_menu_link_text = "My Account"
    click_register_drop_menu_link_text = "Register"
    click_login_drop_menu_link_text = "Login"

    def enter_product_search_box(self,product_name):
        self.element_type(product_name,"enter_product_search_box_name",self.enter_product_search_box_name)

    def click_search_button(self):
        self.element_click("click_search_button_xpath",self.click_search_button_xpath)
        return SearchPage(self.driver)

    def click_my_account_drop_menu(self):
        self.driver.find_element(By.LINK_TEXT,self.click_my_account_drop_menu_link_text).click()

    def click_login_drop_menu(self):
        self.driver.find_element(By.LINK_TEXT,self.click_login_drop_menu_link_text).click()
        return LoginPage(self.driver)

    def click_register_drop_menu(self):
        self.driver.find_element(By.LINK_TEXT,self.click_register_drop_menu_link_text).click()
        return RegisterPage(self.driver)

    def search_product_click_search_button(self,product_name):
        self.enter_product_search_box(product_name)
        self.click_search_button()
        return SearchPage(self.driver)

    def click_my_account_navigate_login_option(self):
        self.click_my_account_drop_menu()
        return self.click_login_drop_menu()