import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("招聘职位")
@allure.feature("测试招聘职位中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_jobs_recruitment:

    @allure.story("招聘中")
    @allure.title("点击跳转到招聘中，查看页面是否有异常弹窗")
    def test_jobs_recruitment_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_jobs_state()
            if "is-opened" not in text:
                s_m.click_jobs()
                s_m.click_jobs_recruitment()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_jobs_recruitment()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("招聘职位")
@allure.feature("测试招聘职位中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_jobs_obsolete:

    @allure.story("已淘汰")
    @allure.title("点击跳转到已淘汰，查看页面是否有异常弹窗")
    def test_jobs_obsolete_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_jobs_state()
            if "is-opened" not in text:
                s_m.click_jobs()
                s_m.click_jobs_obsolete()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_jobs_obsolete()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("招聘职位")
@allure.feature("测试招聘职位中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_jobs_post:

    @allure.story("招聘职位")
    @allure.title("点击跳转到招聘职位，查看页面是否有异常弹窗")
    def test_jobs_post_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_jobs_state()
            if "is-opened" not in text:
                s_m.click_jobs()
                s_m.click_jobs_post()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_jobs_post()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)


@allure.epic("招聘职位")
@allure.feature("测试招聘职位中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_jobs_talents:

    @allure.story("人才库")
    @allure.title("点击跳转到人才库，查看页面是否有异常弹窗")
    def test_jobs_talents_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断保单管理是否展开，未展开将其展开"):
            text = s_m.get_jobs_state()
            if "is-opened" not in text:
                s_m.click_jobs()
                s_m.click_jobs_talents()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_jobs_talents()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)





