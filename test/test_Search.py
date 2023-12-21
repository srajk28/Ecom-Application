from PageObject.HomePage import HomePage
from test.BaseTest import BaseTest

class Test_Search(BaseTest):
  def test_search_for_valid_product(self):
    home_page = HomePage(self.driver)
    search_page = home_page.search_product_click_search_button("HP")
    assert search_page.valid_search_product()

  def test_search_for_invalid_product(self):
    home_page = HomePage(self.driver)
    home_page.enter_product_search_box("Honda")
    search_page = home_page.click_search_button()
    exp_search_text_1 = "There is no product that matches the search criteria."
    assert search_page.invalid_search_product().__eq__(exp_search_text_1)

  def test_search_for_no_product(self):
    home_page = HomePage(self.driver)
    search_page = home_page.search_product_click_search_button("")
    exp_search_text_2 = "There is no product that matches the search criteria.ABC"
    assert search_page.invalid_search_product().__eq__(exp_search_text_2)