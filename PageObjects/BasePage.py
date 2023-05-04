from appium.webdriver.common.appiumby import AppiumBy

from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger.get_Logger()

class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def click(self,locator):
        if str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.get_config("locators",locator)).click()
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.get_config("locators",locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.get_config("locators",locator)).click()
        log.info("Clicking on an element" + str(locator))

    def send_keys(self,locator,value):
        if str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.get_config("locators",locator)).send_keys(value)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.get_config("locators",locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.get_config("locators",locator)).send_keys(value)
        log.info("Typing in an element" + str(locator) + "Entered the Value as: " + str(value))

    def get_text(self,locator):
        if str(locator).endswith("_ID"):
            text = self.driver.find_element(AppiumBy.ID, configReader.get_config("locators",locator)).text
        elif str(locator).endswith("_XPATH"):
            text = self.driver.find_element(AppiumBy.XPATH, configReader.get_config("locators",locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.get_config("locators",locator)).text
        log.info("Getting text from an element" + str(locator))
        return text