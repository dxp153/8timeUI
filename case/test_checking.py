import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("考勤管理")
@allure.feature("测试考勤管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_checking_monthly_statistics:

    @allure.story("月度汇总")
    @allure.title("点击跳转到月度汇总，查看页面是否有异常弹窗")
    def test_checking_monthly_statistics_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_checking_state()
            if "is-opened" not in text:
                s_m.click_checking()
                s_m.click_checking_monthly_statistics()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_checking_monthly_statistics()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("考勤管理")
@allure.feature("测试考勤管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_checking_daily_statistics:

    @allure.story("每日统计")
    @allure.title("点击跳转到每日统计，查看页面是否有异常弹窗")
    def test_checking_daily_statistics_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_checking_state()
            if "is-opened" not in text:
                s_m.click_checking()
                s_m.click_checking_daily_statistics()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_checking_daily_statistics()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("考勤管理")
@allure.feature("测试考勤管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_checking_source_record:

    @allure.story("原始记录")
    @allure.title("点击跳转到原始记录，查看页面是否有异常弹窗")
    def test_checking_source_record_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_checking_state()
            if "is-opened" not in text:
                s_m.click_checking()
                s_m.click_checking_source_record()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_checking_source_record()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("考勤管理")
@allure.feature("测试考勤管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_checking_set:

    @allure.story("考勤设置")
    @allure.title("点击跳转到考勤设置，查看页面是否有异常弹窗")
    def test_checking_set_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_checking_state()
            if "is-opened" not in text:
                s_m.click_checking()
                s_m.click_checking_set()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_checking_set()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("考勤管理")
@allure.feature("测试考勤管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_checking_overtime_rule:

    @allure.story("加班规则")
    @allure.title("点击跳转到加班规则，查看页面是否有异常弹窗")
    def test_checking_overtime_rule_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_checking_state()
            if "is-opened" not in text:
                s_m.click_checking()
                s_m.click_checking_overtime_rule()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_checking_overtime_rule()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("考勤管理")
@allure.feature("测试考勤管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_checking_recess_staff:

    @allure.story("员工假期")
    @allure.title("点击跳转到员工假期，查看页面是否有异常弹窗")
    def test_checking_recess_staff_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_checking_state()
            if "is-opened" not in text:
                s_m.click_checking()
                s_m.click_checking_recess_staff()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_checking_recess_staff()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("考勤管理")
@allure.feature("测试考勤管理中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_checking_recess_rule:

    @allure.story("假勤规则")
    @allure.title("点击跳转到假勤规则，查看页面是否有异常弹窗")
    def test_checking_recess_rule_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_checking_state()
            if "is-opened" not in text:
                s_m.click_checking()
                s_m.click_checking_recess_rule()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_checking_recess_rule()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
