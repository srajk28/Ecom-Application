from PageObject.HomePage import HomePage
from test.BaseTest import BaseTest


class Test_Register(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        register_page = home_page.click_register_drop_menu()
        register_page.register_account("abc","abc",self.gen_email_date_time(),"987654321","12345","12345")
        assert register_page.validate_content()

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        register_page = home_page.click_register_drop_menu()
        register_page.register_account("abc","abc",self.gen_email_date_time(),"987654321","12345","12345")
        assert register_page.validate_content()

    def test_register_with_exist_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        register_page = home_page.click_register_drop_menu()
        register_page.register_account("abc","abc","abc123@gmail.com","987654321","12345","12345")
        exp_register_warning_text_1 = "Warning: E-Mail Address is already registered!"
        assert register_page.validate_warning_email_address().__eq__(exp_register_warning_text_1)

    def test_register_without_field(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        register_page = home_page.click_register_drop_menu()
        register_page.register_account("","","","","","")
        assert register_page.verify_all_warning("First Name must be between 1 and 32 characters!")