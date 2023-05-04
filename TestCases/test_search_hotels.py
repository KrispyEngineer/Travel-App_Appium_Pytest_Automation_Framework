import pytest

from PageObjects.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from Utilities.DataProvider import get_dataload


class Test_Search_Hotels(BaseTest):



    def test_Search_Hotels(self,data_load):
        home = HomeScreen(self.driver)
        home.goto_Hotels().SearchHotel(data_load)

    @pytest.fixture(params= get_dataload("TestHotel"))
    def data_load(self, request):
        return request.param