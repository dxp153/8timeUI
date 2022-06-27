import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("云盘")
@allure.feature("测试云盘中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_license_record_my:

    @allure.story("我的云盘")
    @allure.title("点击跳转到我的云盘，查看页面是否有异常弹窗")
    def test_license_record_my_01(self, get_driver):
        s_m = get_driver[2]
        with allure.step("判断考勤管理是否展开，未展开将其展开"):
            text = s_m.get_cloud_storage()
            if "is-opened" not in text:
                s_m.click_cloud_storage()
                s_m.click_license_record_my()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
            else:
                s_m.click_license_record_my()
                with allure.step("断言当前页面是否出现异常提示"):
                    alert_text = s_m.alert()
                    pytest.assume(alert_text == False)
