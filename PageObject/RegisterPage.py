from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    enter_firstname_id = "input-firstname"
    enter_lastname_id = "input-lastname"
    enter_email_id = "input-email"
    enter_telephone_id = "input-telephone"
    enter_password_id = "input-password"
    enter_confirm_password_id = "input-confirm"
    click_newsletter_subscribe_xpath = "//input[@name='newsletter'][@value='1']"
    click_agree_name = "agree"
    click_continue_button_xpath = "//input[@value='Continue']"
    validate_content_xpath = "//div[@id='content']/h1"
    validate_warning_email_address_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    verify_first_name_alert_message_xpath = "(//div[@class='text-danger'])[1]"

    def enter_firstname(self,first_name):
        self.driver.find_element(By.ID,self.enter_firstname_id).click()
        self.driver.find_element(By.ID,self.enter_firstname_id).clear()
        self.driver.find_element(By.ID,self.enter_firstname_id).send_keys(first_name)

    def enter_lastname(self,last_name):
        self.driver.find_element(By.ID,self.enter_password_id).click()
        self.driver.find_element(By.ID,self.enter_password_id).clear()
        self.driver.find_element(By.ID,self.enter_password_id).send_keys(last_name)

    def enter_email(self,email_field):
        self.driver.find_element(By.ID,self.enter_email_id).click()
        self.driver.find_element(By.ID,self.enter_email_id).clear()
        self.driver.find_element(By.ID,self.enter_email_id).send_keys(email_field)

    def enter_telephone(self,telephone_field):
        self.driver.find_element(By.ID,self.enter_telephone_id).click()
        self.driver.find_element(By.ID,self.enter_telephone_id).clear()
        self.driver.find_element(By.ID,self.enter_telephone_id).send_keys(telephone_field)

    def enter_password(self,password_field):
        self.driver.find_element(By.ID,self.enter_password_id).click()
        self.driver.find_element(By.ID,self.enter_password_id).clear()
        self.driver.find_element(By.ID,self.enter_password_id).send_keys(password_field)

    def enter_confirm_password(self,confirm_password_field):
        self.driver.find_element(By.ID,self.enter_confirm_password_id).click()
        self.driver.find_element(By.ID,self.enter_confirm_password_id).clear()
        self.driver.find_element(By.ID,self.enter_confirm_password_id).send_keys(confirm_password_field)

    def click_newsletter_subscribe(self):
        self.driver.find_element(By.XPATH,self.click_newsletter_subscribe_xpath).click()

    def click_agree(self):
        self.driver.find_element(By.NAME,self.click_agree_name).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH,self.click_continue_button_xpath).click()

    def validate_content(self):
        return self.driver.find_element(By.XPATH,self.validate_content_xpath).is_displayed()

    def validate_warning_email_address(self):
        return self.driver.find_element(By.XPATH,self.validate_warning_email_address_xpath).text

    def verify_first_name_alert_message(self):
        return self.driver.find_element(By.XPATH,self.verify_first_name_alert_message_xpath).text

    def register_account(self,first_name,last_name,email_field,telephone_field,password_field,confirm_password_field):
        self.enter_firstname(first_name)
        self.enter_lastname(last_name)
        self.enter_email(email_field)
        self.enter_telephone(telephone_field)
        self.enter_password(password_field)
        self.enter_confirm_password(confirm_password_field)
        self.click_newsletter_subscribe()
        self.click_agree()
        return self.click_continue_button()

    def verify_all_warning(self,exp_first_name_alert):
        act_first_name_alert = self.verify_first_name_alert_message()
        status = False
        if exp_first_name_alert.__eq__(act_first_name_alert):
            status = True
        return status








