import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("社保公积金")
@allure.feature("测试社保公积金中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_social_security_scheme:

    @allure.story("参保方案")
    @allure.title("点击跳转到参保方案，查看页面是否有异常弹窗")
    def test_social_security_scheme_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断社保公积金是否展开，未展开将其展开"):
            text = s_m.get_social_security_state()
            if "is-opened" not in text:
                s_m.click_social_security()
                s_m.click_social_security_scheme()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_social_security_scheme()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("社保公积金")
@allure.feature("测试社保公积金中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_social_security_staff:

    @allure.story("参保员工")
    @allure.title("点击跳转到参保员工，查看页面是否有异常弹窗")
    def test_social_security_staff_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断社保公积金是否展开，未展开将其展开"):
            text = s_m.get_remuneration_state()
            if "is-opened" not in text:
                s_m.click_social_security()
                s_m.click_social_security_staff()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_social_security_staff()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("社保公积金")
@allure.feature("测试社保公积金中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_social_security_monthly_scheme:

    @allure.story("月结方案")
    @allure.title("点击跳转到月结方案，查看页面是否有异常弹窗")
    def test_social_security_monthly_scheme_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断社保公积金是否展开，未展开将其展开"):
            text = s_m.get_remuneration_state()
            if "is-opened" not in text:
                s_m.click_social_security()
                s_m.click_social_security_monthly_scheme()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_social_security_monthly_scheme()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)