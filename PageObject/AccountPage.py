from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self,driver):
        self.driver = driver

    edit_your_account_information_link_text = "Edit your account information"
    warning_no_match_xpath = "//div[@id='account-login']/div[1]"

    def edit_your_account_information(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_your_account_information_link_text).is_displayed()

    def warning_no_match(self):
        return self.driver.find_element(By.XPATH,self.warning_no_match_xpath()).text