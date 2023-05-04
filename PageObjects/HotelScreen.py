from PageObjects.BasePage import BasePage


class HotelScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def SearchHotel(self,city):
        self.click("search_box_ID")
        self.send_keys("search_text_ID",city)
        self.click("select_destination_ID")
        self.click("home_search_button_XPATH")
        self.click("pop_up_ID") 