import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from Utilities import ReadConfiguration

@pytest.fixture()
def log_on_failure(request):
  yield
  item = request.node
  if item.rep_call.failed:
    allure.attach(driver.get_screenshot_as_png(),name="failed_test", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item,call):
  outcome = yield
  rep = outcome.get_result()
  setattr(item, "rep_" + rep.when, rep)
  return rep

@pytest.fixture()
def setup_and_teardown(request):
  app_browser = ReadConfiguration.read_configuration("basic info","browser")
  global driver
  driver = None
  if app_browser.__eq__("chrome"):
    driver = webdriver.Chrome()
  elif app_browser.__eq__("firefox"):
    driver = webdriver.Firefox()
  elif app_browser.__eq__("edge"):
    driver = webdriver.Edge()
  elif app_browser.__eq__("ie"):
    driver = webdriver.Ie()
  else:
   print("Provide valid web browser")
  driver.maximize_window()
  app_url = ReadConfiguration.read_configuration("basic info","url")
  driver.get(app_url)
  request.cls.driver = driver
  yield
  driver.quit()