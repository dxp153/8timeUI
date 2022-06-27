import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("绩效")
@allure.feature("测试绩效中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_performance_management:

    @allure.story("绩效管理")
    @allure.title("点击跳转到绩效管理，查看页面是否有异常弹窗")
    def test_performance_management_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_performance_state()
            if "is-opened" not in text:
                s_m.click_performance()
                s_m.click_performance_management()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_performance_management()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("绩效管理")
@allure.feature("测试绩效管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_performance_my:

    @allure.story("我的绩效")
    @allure.title("点击跳转到我的绩效，查看页面是否有异常弹窗")
    def test_performance_my_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_performance_state()
            if "is-opened" not in text:
                s_m.click_performance()
                s_m.click_performance_my()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_performance_my()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("绩效")
@allure.feature("测试绩效中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_performance_set_up:

    @allure.story("绩效设置")
    @allure.title("点击跳转到绩效设置，查看页面是否有异常弹窗")
    def test_performance_set_up_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_performance_state()
            if "is-opened" not in text:
                s_m.click_performance()
                s_m.click_performance_set_up()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_performance_set_up()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)