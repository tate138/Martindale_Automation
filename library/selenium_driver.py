from selenium import webdriver
from library.tools import Tools


class SeleniumDriver:
    def __init__(self):
        pass

    @staticmethod
    def fetch_chrome_webdriver():
        driver_path = SeleniumDriver._set_chrome_directory()
        chrome_options = SeleniumDriver._set_chrome_option()
        driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        driver.maximize_window()
        return driver

    #####
    ##
    # Driver Close
    ##
    #####

    @staticmethod
    def close_web_driver(web_driver):
        """Close webdriver

        :param WebDriver web_driver:
        """
        Tools.sleep(3)
        web_driver.close()

    #####
    ##
    # Directory
    ##
    #####

    @staticmethod
    def _set_chrome_directory():
        directory_name = "driver\\"
        directory = Tools.build_relative_directory_path(directory_name)
        driver_name = "chromedriver.exe"
        driver_path = directory + driver_name
        return driver_path

    #####
    ##
    # Driver Options
    ##
    #####

    @staticmethod
    def _set_chrome_option():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        return chrome_options
