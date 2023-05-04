from appium.webdriver.common.appiumby import AppiumBy

from PageObjects.BasePage import BasePage


class BusesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_Buses(self, city):
        self.click("click_from_XPATH")
        self.send_keys('enter_from_city_XPATH', city[0])
        self.click('select_from_city_XPATH')
        self.click('destination_XPATH')
        self.send_keys('enter_to_city_XPATH',city[1])
        self.click('select_to_city_XPATH')
        self.click('select_date_XPATH')
        self.click('search_button_XPATH')
        self.click('primo_bus_XPATH')
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                             "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"" + city[2] + "\").instance(0))").click()

        bus_name = self.get_text("verify_text_XPATH")
        assert "Ganga Travels Go!Red BENZ" == bus_name, "Inccorect Bus Selected."