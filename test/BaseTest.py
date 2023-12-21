from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    def gen_email_date_time(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "abc" + timestamp + "@gmail.com"
