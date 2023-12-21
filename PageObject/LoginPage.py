from selenium.webdriver.common.by import By

from PageObject.AccountPage import AccountPage


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    login_email_field_id = "input-email"
    login_password_field_id = "input-password"
    submit_button_xpath = "//input[@type='submit']"

    def login_email_field(self,login_name):
        self.driver.find_element(By.ID,self.login_email_field_id).click()
        self.driver.find_element(By.ID,self.login_email_field_id).clear()
        self.driver.find_element(By.ID,self.login_email_field_id).send_keys(login_name)

    def login_password_field(self,password_name):
        self.driver.find_element(By.ID,self.login_password_field_id).click()
        self.driver.find_element(By.ID,self.login_password_field_id).clear()
        self.driver.find_element(By.ID,self.login_password_field_id).send_keys(password_name)

    def submit_button(self):
        self.driver.find_element(By.XPATH,self.submit_button_xpath).click()
        return AccountPage(self.driver)

    def enter_email_password_click_submit_button(self,login_name,password_name):
        self.login_email_field(login_name)
        self.login_password_field(password_name)
        return self.submit_button()