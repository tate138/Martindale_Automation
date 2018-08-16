from library.selenium_driver import SeleniumDriver
from library.page_data.martindale_app.martindale_data import MartindalePageData
from testrail.testrail import *
from tests.test_model.web_data_model import WebDataModel


class CommonSetup():
    web_data_model = WebDataModel()

    # Test Rail Data
    client = APIClient(MartindalePageData.TEST_RAIL_URL)
    client.user = MartindalePageData.AUTOMATION_USER
    client.password = MartindalePageData.AUTOMATION_PW
    current_test_run_id = MartindalePageData.AUTOMATION_TEST_RUN_ID

    def fetch_webdriver(self):
        return self.web_data_model.get_web_driver()

    def close_webdriver(self):
        SeleniumDriver.close_web_driver(self.web_data_model.get_web_driver())
