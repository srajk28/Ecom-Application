import pytest
from PageObject.HomePage import HomePage
from Utilities import ExcelUtils
from test.BaseTest import BaseTest


class Test_Login(BaseTest):
    @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel("Configuration/ExcelFiles/testdata.xlsx", "Sheet1"))
    def test_login_with_valid_email_valid_password(self, email_address, password):
        home_page = HomePage(self.driver)
        login_page = home_page.click_my_account_navigate_login_option()
        account_page = login_page.enter_email_password_click_submit_button(email_address, password)
        assert account_page.edit_your_account_information()

    def test_login_with_invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        login_page = home_page.click_login_drop_menu()
        login_page.login_email_field(self.gen_email_date_time())
        login_page.login_password_field("12345")
        account_page = login_page.submit_button()
        exp_login_warning_text_1 = "Warning: No match for E-Mail Address and/or Password."
        assert account_page.warning_no_match.__eq__(exp_login_warning_text_1)

    def test_login_with_valid_email_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        login_page = home_page.click_login_drop_menu()
        login_page.login_email_field("abcba@gmail.com")
        login_page.login_password_field("123abc")
        account_page = login_page.submit_button()
        exp_login_warning_text_2 = "Warning: No match for E-Mail Address and/or Password."
        assert account_page.warning_no_match.__eq__(exp_login_warning_text_2)

    def test_login_with_no_email_no_password(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        login_page = home_page.click_login_drop_menu()
        login_page.login_email_field("")
        login_page.login_password_field("")
        account_page = login_page.submit_button()
        exp_login_warning_text_3 = "Warning: No match for E-Mail Address and/or Password."
        assert account_page.warning_no_match.__eq__(exp_login_warning_text_3)