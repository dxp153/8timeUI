import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("企业中心")
@allure.feature("测试企业中心中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_business_center_account:

    @allure.story("企业账户")
    @allure.title("点击跳转到企业账户，查看页面是否有异常弹窗")
    def test_business_center_account_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断企业中心是否展开，未展开将其展开"):
            text = s_m.get_business_center()
            if "is-opened" not in text:
                s_m.click_business_center()
                s_m.click_business_center_account()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_business_center_account()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("企业中心")
@allure.feature("测试企业中心中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_business_center_pay:

    @allure.story("付费管理")
    @allure.title("点击跳转到付费管理，查看页面是否有异常弹窗")
    def test_business_center_pay_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断企业中心是否展开，未展开将其展开"):
            text = s_m.get_business_center()
            print(text)
            if "is-opened" not in text:
                s_m.click_business_center()
                s_m.click_business_center_pay()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_business_center_pay()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("企业中心")
@allure.feature("测试企业中心中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_business_center_note:

    @allure.story("短信管理")
    @allure.title("点击跳转到短信管理，查看页面是否有异常弹窗")
    def test_business_center_note_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断企业中心是否展开，未展开将其展开"):
            text = s_m.get_business_center()
            if "is-opened" not in text:
                s_m.click_business_center()
                s_m.click_business_center_note()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_business_center_note()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("企业中心")
@allure.feature("测试企业中心中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_business_center_log:

    @allure.story("操作日志")
    @allure.title("点击跳转到操作日志，查看页面是否有异常弹窗")
    def test_business_center_log_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断企业中心是否展开，未展开将其展开"):
            text = s_m.get_business_center()
            if "is-opened" not in text:
                s_m.click_business_center()
                s_m.click_business_center_log()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_business_center_log()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("企业中心")
@allure.feature("测试企业中心中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_business_center_feedback:

    @allure.story("意见反馈")
    @allure.title("点击跳转到意见反馈，查看页面是否有异常弹窗")
    def test_business_center_feedback_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断企业中心是否展开，未展开将其展开"):
            text = s_m.get_business_center()
            if "is-opened" not in text:
                s_m.click_business_center()
                s_m.click_business_center_feedback()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_business_center_feedback()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("企业中心")
@allure.feature("测试企业中心中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_business_center_custom:

    @allure.story("企业自定义")
    @allure.title("点击跳转到企业自定义，查看页面是否有异常弹窗")
    def test_business_center_custom_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断企业中心是否展开，未展开将其展开"):
            text = s_m.get_business_center()
            if "is-opened" not in text:
                s_m.click_business_center()
                s_m.click_business_center_custom()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_business_center_custom()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
