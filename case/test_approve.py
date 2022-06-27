import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("审批")
@allure.feature("测试审批中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_approve_manage:

    @allure.story("审批管理")
    @allure.title("点击跳转到审批管理，查看页面是否有异常弹窗")
    def test_approve_manage_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断审批是否展开，未展开将其展开"):
            text = s_m.get_approve_state()
            if "is-opened" not in text:
                s_m.click_approve()
                s_m.click_approve_manage()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_approve_manage()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("审批")
@allure.feature("测试审批中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_approve_collect:

    @allure.story("审批汇总")
    @allure.title("点击跳转到审批汇总，查看页面是否有异常弹窗")
    def test_approve_collect_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断审批是否展开，未展开将其展开"):
            text = s_m.get_approve_state()
            if "is-opened" not in text:
                s_m.click_approve()
                s_m.click_approve_collect()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_approve_collect()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("审批")
@allure.feature("测试审批中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_approve_personage:

    @allure.story("个人审批")
    @allure.title("点击跳转到个人审批，查看页面是否有异常弹窗")
    def test_approve_personage_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断审批是否展开，未展开将其展开"):
            text = s_m.get_approve_state()
            if "is-opened" not in text:
                s_m.click_approve()
                s_m.click_approve_personage()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_approve_personage()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)

