from PageObjects.BasePage import BasePage
from PageObjects.BusesPage import BusesPage
from PageObjects.HotelScreen import HotelScreen


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def goto_Hotels(self):
        self.click("hotels_ID")
        return HotelScreen(self.driver)

    def goto_Buses(self):
        self.click("buses_XPATH")
        return BusesPage(self.driver)

    def goto_Trains(self):
        pass


