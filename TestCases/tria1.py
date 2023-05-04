import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Utilities.ScrollUtil import ScrollUtil


def test_trial(setup_function):
    driver = setup_function
    driver.find_element(AppiumBy.ID, "com.goibibo:id/icon").click()
    driver.find_element(AppiumBy.ID, "com.goibibo:id/txtPlaceName").click()
    driver.find_element(AppiumBy.ID, "com.goibibo:id/edtSearch").send_keys("Pune")
    driver.find_element(AppiumBy.ID, "com.goibibo:id/lytPlace").click()
    driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()
    driver.find_element(AppiumBy.ID, "com.goibibo:id/ivClose").click()
    ScrollUtil.ScrollUp(3,driver)


@pytest.fixture(params=['pune', 'delhi'])
def get_data(request):
    return request.param
