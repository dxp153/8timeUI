import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("组织管理")
@allure.feature("测试组织管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_organization_structure:

    @allure.story("组织架构")
    @allure.title("点击跳转到组织架构，查看页面是否有异常弹窗")
    def test_organization_structure_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_organization_state()
            if "is-opened" not in text:
                s_m.click_organization()
                s_m.click_organization_structure()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_organization_structure()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("组织管理")
@allure.feature("测试组织管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_organization_chart:

    @allure.story("架构图")
    @allure.title("点击跳转到架构图，查看页面是否有异常弹窗")
    def test_organization_chart_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_organization_state()
            if "is-opened" not in text:
                s_m.click_organization()
                s_m.click_organization_chart()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_organization_chart()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)