from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

from library.tools import Tools



'''
Selenium Methods
'''

class SeleniumActions:

    ##########
    #####
    ## Browser
    #####
    ##########

    @staticmethod
    def refresh_page(web_driver):
        """Refreshes the page
        
        :param WebDriver web_driver:

        :rtype: bool
        :return: boolean 
        """
        try:
            web_driver.navigate().refresh()
            Tools.sleep(1)
            return True
        except Exception as error:
            return False

    ##########
    #####
    ## Visibility
    #####
    ##########

    @staticmethod
    def wait_for_element(web_driver, web_element):
        """waits for element
        
        :param WebDriver web_driver: 
        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        try:
            WebDriverWait(web_driver, 3).until(expected_conditions.presence_of_element_located(web_element))
            return True
        except Exception as error:
            return False

    @staticmethod
    def element_is_visible(web_driver, web_element):
        """checks to see if element is visible
        
        :param WebDriver web_driver: 
        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        SeleniumActions.wait_for_element(web_driver, web_element)
        if web_element is not None and web_element.is_displayed():
            return True
        else:
            return False


    @staticmethod
    def element_is_not_visible(web_element):
        """checks to see if element is not visible
        
        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        if web_element is None or not web_element.is_displayed():
            return True
        else:
            return False
    
    ##########
    #####
    ## Click
    #####
    ##########

    @staticmethod
    def click_element(web_driver, web_element):
        """Tries to click a WebElement three times
        
        :param WebDriver web_driver: 
        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        if SeleniumActions.element_is_visible(web_driver, web_element):
            has_click_passed = SeleniumActions.click_was_successful(web_element)
            if not has_click_passed:
                SeleniumActions.move_to_element(web_driver, web_element)
                has_click_passed_now = SeleniumActions.click_was_successful(web_element)
                if not has_click_passed_now:
                    has_click_passed_finally = SeleniumActions.send_enter_to_element(web_driver, web_element)
                    if not has_click_passed_finally:
                        return False
        else:
            return False
    

    @staticmethod
    def click_was_successful(web_element):
        """WebElement click was successful

        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        try:
            web_element.click()
            return True
        except Exception as error:
            return False
    

    @staticmethod
    def move_to_element(web_driver, web_element):
        """Moves to WebElement
        
        :param WebDriver web_driver: 
        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        try:
            move_to = ActionChains(web_driver).move_to_element(web_element)
            move_to.perform()
            return True
        except Exception as error:
            return False
    
    @staticmethod
    def send_enter_to_element(web_driver, web_element):
        """Sends the text enter to a WebElement
        
        :param WebDriver web_driver: 
        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        if SeleniumActions.element_is_visible(web_driver, web_element):
            try:
                web_element.sendKeys(Keys.RETURN)
                return False
            except Exception as error:
                return True

    ##########
    #####
    ## Select
    #####
    ##########

    @staticmethod
    def select_by_index(web_element, index):
        try:
            select = Select(web_element)
            select.select_by_index(index)
            return True
        except Exception as error:
            return False

    @staticmethod
    def select_by_value(web_element, value):
        try:
            select = Select(web_element)
            select.select_by_value(value)
            return True
        except Exception as error:
            return False

    @staticmethod
    def select_by_text(web_element, visible_text):
        try:
            select = Select(web_element)
            select.select_by_visible_text(visible_text)
            return True
        except Exception as error:
            return False



    ##########
    #####
    ## Read
    #####
    ##########

    @staticmethod
    def read_web_element_text(web_element):
        """

        :param WebElement web_element:
        :return:
        """
        try:
            text = web_element.text
            return text
        except Exception as error:
            return None

    @staticmethod
    def read_select_text(web_element):
        try:
            select = Select(web_element)
            return select.first_selected_option.text
        except Exception as error:
            return None

    ##########
    #####
    ## Write
    #####
    ##########
    
    @staticmethod
    def write_to_element(web_driver, web_element, write_text):
        """Writes to a WebElement
        
        :param WebDriver web_driver: 
        :param WebElement web_element:
        :param str write_text:

        :rtype: bool
        :return: boolean
        """
        if SeleniumActions.element_is_visible(web_driver, web_element):
            try:
                web_element.send_keys(write_text)
                return True
            except Exception as error:
                return False
        else:
            return False

    ##########
    #####
    ## Clear Text
    #####
    ##########
    
    @staticmethod
    def clearTextField(web_driver, web_element):
        """Clears the text from a WebElement
        
        :param WebDriver web_driver: 
        :param WebElement web_element:

        :rtype: bool
        :return: boolean
        """
        if SeleniumActions.element_is_visible(web_driver, web_element):
            try:
                web_element.clear()
                return True
            except Exception as error:
                return False

    ##########
    #####
    ## Navigate
    #####
    ##########

    @staticmethod
    def navigate_to_url(web_driver, url):
        """Navigates to a url
        
        :param WebDriver web_driver: 
        :param str url:

        :rtype: bool
        :return: boolean
        """
        try:
            web_driver.get(url)
            return True
        except Exception as error:
            return False

    ##########
    #####
    ## Capture Element
    #####
    ##########

    @staticmethod
    def fetch_web_element(web_driver, element_path):
        """Fetches a web element object from a object path. Uses multiple methods to allows for different kinds of paths
        
        :param WebDriver web_driver: 
        :param str element_path:

        :rtype: WebElement
        :return: WebElement
        """
        if Tools.object_has_value(element_path):
    
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
                
            if web_element is None:
                web_element = SeleniumActions.find_by_css_path(web_driver, element_path)

            '''
            if web_element is None:
                web_element = SeleniumActions.find_by_id(web_driver, element_path)
    
            if web_element is None:
                web_element = SeleniumActions.find_by_class_name(web_driver, element_path)
            '''
    
            if web_element is not None:
                return web_element
            else:
                error = "No web element"
                Tools.raise_exception(error)
                return None
        else:
            error = "No element path"
            Tools.raise_exception(error)
            return None
    
    ##########
    #####
    ## Find
    #####
    ##########

    @staticmethod
    def find_by_partial_link_text(web_driver, element_path):
        """Finds a WebElement from a partial link text

        :param WebDriver web_driver:
        :param str element_path:

        :rtype: WebElement
        :return: WebElement
        """
        try:
            my_element = web_driver.find_element(By.PARTIAL_LINK_TEXT, element_path)
            return my_element
        except Exception as error:
            print("Error :: " + str(error) + "\nElement Path: \n" + str(element_path))
            return None

    @staticmethod
    def find_by_xpath(web_driver, element_path):
        """Finds a WebElement from an xpath
        
        :param WebDriver web_driver: 
        :param str element_path:

        :rtype: WebElement
        :return: WebElement
        """
        try:
            my_element = web_driver.find_element(By.XPATH, element_path)
            return my_element
        except Exception as error:
            print("Error :: " + str(error) + "\nElement Path: \n" + str(element_path))
            return None
    
    @staticmethod
    def find_by_css_path(web_driver, element_path):
        """finds a WebElement from a css path
        
        :param WebDriver web_driver: 
        :param str element_path:
        :return: WebElement
        """
        try:
            return web_driver.find_element_by_css_selector(element_path)
        except Exception as error:
            print("Error :: " + str(error) + "\nElement Path: \n" + str(element_path))
            return None
    
    @staticmethod
    def find_by_id(web_driver, element_path):
        """finds a WebElement from an id
        
        :param WebDriver web_driver: 
        :param str element_path:
        :return: WebElement
        """
        try:
            return web_driver.find_element_by_id(element_path)
        except Exception as error:
            print("Error :: " + str(error) + "\nElement Path: \n" + str(element_path))
            return None
    
    @staticmethod
    def find_by_class_name(web_driver, element_path):
        """finds a WebElement from a class
        
        :param WebDriver web_driver: 
        :param str element_path:
        :return: WebElement
        """
        try:
            return web_driver.find_element_by_class_name(element_path)
        except Exception as error:
            print("Error :: " + str(error) + "\nElement Path: \n" + str(element_path))
            return None

    @staticmethod
    def check_element_exists(web_driver, element_path):
        """Check if element exists

        :param WebDriver web_driver:
        :param str element_path:

        :rtype: WebElement
        :return: WebElement
        """
        try:
            my_element = web_driver.find_elements(By.XPATH, element_path)
            return my_element
        except Exception as error:
            print("Error :: " + str(error) + "\nElement Path: \n" + str(element_path))
            return None

