import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("CRM管理")
@allure.feature("测试CRM管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_CRM_data_statistics:

    @allure.story("数据统计")
    @allure.title("点击跳转到数据统计，查看页面是否有异常弹窗")
    def test_CRM_data_statistics(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_CRM_state()
            if "is-opened" not in text:
                s_m.click_CRM()
                s_m.click_CRM_data_statistics()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_CRM_data_statistics()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("CRM管理")
@allure.feature("测试CRM管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_CRM_my_customers:

    @allure.story("我的客户")
    @allure.title("点击跳转到我的客户，查看页面是否有异常弹窗")
    def test_CRM_my_customers(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_CRM_state()
            if "is-opened" not in text:
                s_m.click_CRM()
                s_m.click_CRM_my_customers()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_CRM_my_customers()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("CRM管理")
@allure.feature("测试CRM管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_CRM_seas_customers:

    @allure.story("客户公海")
    @allure.title("点击跳转到客户公海，查看页面是否有异常弹窗")
    def test_CRM_seas_customers(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_CRM_state()
            if "is-opened" not in text:
                s_m.click_CRM()
                s_m.click_CRM_seas_customers()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_CRM_seas_customers()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("CRM管理")
@allure.feature("测试CRM管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_CRM_all_customers:

    @allure.story("所有客户")
    @allure.title("点击跳转到所有客户，查看页面是否有异常弹窗")
    def test_CRM_all_customers(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_CRM_state()
            if "is-opened" not in text:
                s_m.click_CRM()
                s_m.click_CRM_all_customers()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_CRM_all_customers()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("CRM管理")
@allure.feature("测试CRM管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_CRM_business_portfolio:

    @allure.story("业务组设置")
    @allure.title("点击跳转到业务组设置，查看页面是否有异常弹窗")
    def test_CRM_business_portfolio(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_CRM_state()
            if "is-opened" not in text:
                s_m.click_CRM()
                s_m.click_CRM_business_portfolio()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_CRM_business_portfolio()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)