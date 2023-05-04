import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope='function')
def setup_function(request):

    desired_caps = dict()

    desired_caps['deviceName'] = 'Realme'
    desired_caps['platformName'] = 'Android'
    desired_caps['appPackage'] = 'com.goibibo'
    desired_caps['appActivity'] = '.common.HomeActivity'
    desired_caps['noReset'] = True
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield driver
    time.sleep(3)
    driver.quit()

@pytest.fixture()
def log_on_failure(request, setup_function):
    yield
    item = request.node
    driver = setup_function
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
