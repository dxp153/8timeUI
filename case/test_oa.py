import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("OA讯息")
@allure.feature("测试OA讯息中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_OA_message_board:

    @allure.story("讯息看板")
    @allure.title("点击跳转到讯息看板页，查看页面是否有异常弹窗")
    def test_message_board_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断OA讯息是否展开，未展开将其展开"):
            text = s_m.get_message_board_state()
            if "is-opened" not in text:
                s_m.click_message()
                s_m.click_message_board()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_message_board()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("OA讯息")
@allure.feature("测试OA讯息中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_OA_message_list:

    @allure.story("讯息列表")
    @allure.title("点击跳转到讯息看板页，查看页面是否有异常弹窗")
    def test_message_list_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断OA讯息是否展开，未展开将其展开"):
            text = s_m.get_message_board_state()
            if "is-opened" not in text:
                s_m.click_message()
                s_m.click_message_list()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_message_list()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("OA讯息")
@allure.feature("测试OA讯息中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_OA_message_approve:

    @allure.story("讯息审核")
    @allure.title("点击跳转到讯息审核页，查看页面是否有异常弹窗")
    def test_message_approve_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断OA讯息是否展开，未展开将其展开"):
            text = s_m.get_message_board_state()
            if "is-opened" not in text:
                s_m.click_message()
                s_m.click_message_approve()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_message_approve()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("OA讯息")
@allure.feature("测试OA讯息中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_OA_message_inform:

    @allure.story("企业通知")
    @allure.title("点击跳转到企业通知页，查看页面是否有异常弹窗")
    def test_message_inform_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断OA讯息是否展开，未展开将其展开"):
            text = s_m.get_message_board_state()
            if "is-opened" not in text:
                s_m.click_message()
                s_m.click_message_inform()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_message_inform()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


if __name__ ==  "__main__":
    Test_OA_message_approve()
    Test_OA_message_inform()
    Test_OA_message_list()
    Test_OA_message_board()