import unittest

from selenium import webdriver

from library.selenium_actions import SeleniumActions
from library.tools import Tools
from library.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select


#####
##
#  Basic Integration Test
##
#####


def test_selenium_integration():
    web_driver = SeleniumDriver.fetch_chrome_webdriver()
    url = 'http://www.google.com'
    web_driver.get(url)
    actual_url = web_driver.current_url
    print(actual_url)
    SeleniumDriver.close_web_driver(web_driver)

def test_select():
    web_driver = SeleniumDriver.fetch_chrome_webdriver()
    url ="http://the-internet.herokuapp.com/dropdown"
    web_driver.get(url)
    element_path = "//select[@id='dropdown']"
    web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

    Tools.sleep(2)
    select_1 = Select(web_element)
    print(len(select_1.options))

    select_1.select_by_visible_text('Option 1')
    Tools.sleep(3)
    print("**")
    select_2 = Select(web_element)
    select_2.select_by_index(2)
    Tools.sleep(3)
    print("--")
    select_3 = Select(web_element)
    select_3.select_by_value("1")
    text = select_3.first_selected_option.text
    print(text)

    Tools.sleep(5)
    web_driver.close()




#####
##
#  Run
##
#####

if __name__ == "__main__":
    #test_selenium_integration()
    test_select()
