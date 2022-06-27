import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("薪酬管理")
@allure.feature("测试薪酬管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_remuneration_payroll_computation:

    @allure.story("薪资计算")
    @allure.title("点击跳转到薪资计算，查看页面是否有异常弹窗")
    def test_remuneration_payroll_computation_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断薪酬管理是否展开，未展开将其展开"):
            text = s_m.get_remuneration_state()
            if "is-opened" not in text:
                s_m.click_remuneration()
                s_m.click_remuneration_payroll_computation()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_remuneration_payroll_computation()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("薪酬管理")
@allure.feature("测试薪酬管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_remuneration_payroll_files:

    @allure.story("薪资档案")
    @allure.title("点击跳转到薪资档案，查看页面是否有异常弹窗")
    def test_remuneration_payroll_files_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断薪酬管理是否展开，未展开将其展开"):
            text = s_m.get_remuneration_state()
            if "is-opened" not in text:
                s_m.click_remuneration()
                s_m.click_remuneration_payroll_files()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_remuneration_payroll_files()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)



@allure.epic("薪酬管理")
@allure.feature("测试薪酬管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_remuneration_special_deduction:

    @allure.story("专项附加扣除")
    @allure.title("点击跳转到专项附加扣除，查看页面是否有异常弹窗")
    def test_remuneration_special_deduction_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断薪酬管理是否展开，未展开将其展开"):
            text = s_m.get_remuneration_state()
            if "is-opened" not in text:
                s_m.click_remuneration()
                s_m.click_remuneration_special_deduction()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_remuneration_special_deduction()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("薪酬管理")
@allure.feature("测试薪酬管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_remuneration_tax_detail:

    @allure.story("个税计算明细")
    @allure.title("点击跳转到个税计算明细，查看页面是否有异常弹窗")
    def test_remuneration_tax_detail_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断薪酬管理是否展开，未展开将其展开"):
            text = s_m.get_remuneration_state()
            if "is-opened" not in text:
                s_m.click_remuneration()
                s_m.click_remuneration_tax_detail()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_remuneration_tax_detail()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
