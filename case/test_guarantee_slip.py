import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("保单管理")
@allure.feature("测试保单管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_guarantee_slip_list:

    @allure.story("保单列表")
    @allure.title("点击跳转到保单列表，查看页面是否有异常弹窗")
    def test_guarantee_slip_list_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_guarantee_slip_storage()
            if "is-opened" not in text:
                s_m.click_guarantee_slip()
                s_m.click_guarantee_slip_list()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_guarantee_slip_list()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("保单管理")
@allure.feature("测试保单管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_guarantee_slip_set:

    @allure.story("投保信息设置")
    @allure.title("点击跳转到投保信息设置，查看页面是否有异常弹窗")
    def test_guarantee_slip_set_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_guarantee_slip_storage()
            if "is-opened" not in text:
                s_m.click_guarantee_slip()
                s_m.click_guarantee_slip_set()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_guarantee_slip_list()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("保单管理")
@allure.feature("测试保单管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_guarantee_slip_log:

    @allure.story("保单日志列表")
    @allure.title("点击跳转到保单日志列表，查看页面是否有异常弹窗")
    def test_guarantee_slip_log_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_guarantee_slip_storage()
            if "is-opened" not in text:
                s_m.click_guarantee_slip()
                s_m.click_guarantee_slip_log()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_guarantee_slip_list()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


