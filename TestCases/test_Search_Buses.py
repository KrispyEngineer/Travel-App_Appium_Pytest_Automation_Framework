import pytest

from PageObjects.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from Utilities.DataProvider import get_dataload


class Test_Search_Buses(BaseTest):

    def test_search_Buses(self,data_load):
        home = HomeScreen(self.driver)
        home.goto_Buses().search_Buses(data_load)

    @pytest.fixture(params= get_dataload("TestBuses"))
    def data_load(self,request):
        return request.param











#
# driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='bus']/android.widget.ImageView").click()
# # Click from
# driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='FromTextField']/android.view.ViewGroup[2]/android.widget.TextView").click()
# # send Kyes Pune
# driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText").send_keys \
#     ("pune")
# # click Pune
    # driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='ContinueButton'])[1]/android.view.ViewGroup/android.widget.TextView").click()
# # Click Destination
# driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='ToTextField']/android.view.ViewGroup[2]/android.widget.TextView").click()
# # Send keys Mumbai
# driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText").send_keys \
#     ('Mumbai')
# driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='ContinueButton'])[1]/android.view.ViewGroup/android.widget.TextView").click()
#
# driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Tomorrow']/android.widget.TextView").click()
# driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='SearchBuses']/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()
# driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]").click()
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#                     "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"Ganga Travels\").instance(0))").click()
