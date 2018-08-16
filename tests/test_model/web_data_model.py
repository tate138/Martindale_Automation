from library.selenium_driver import SeleniumDriver


class WebDataModel:

    web_driver = None
    client = None
    current_test_run_id = -1

    ###############
    ##
    # Setter
    ##
    ###############

    def set_web_driver(self, web_driver):
        self.web_driver = web_driver

    def set_client(self, client):
        self.client = client


    ###############
    ##
    # Getter
    ##
    ###############

    def get_web_driver(self):
        if self.web_driver is not None:
            return self.web_driver
        else:
            web_driver = SeleniumDriver.fetch_chrome_webdriver()
            self.set_web_driver(web_driver)
            return self.web_driver

    def get_client(self):
        return self.client


    ###############
    ##
    # Release
    ##
    ###############

    def release_webdriver(self):
        self.web_driver = None
