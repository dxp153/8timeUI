import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("工作台测试")
@allure.feature("测试工作台中各个模块的功能")
@pytest.mark.usefixtures("login_8time", "get_driver")
class Test_Workbenck:

    @allure.story("我的工作台")
    @allure.title("查看当前页面处于侧边栏的模块")
    def test_workbenck_title_01(self, get_driver):
        l = get_driver[3]
        time.sleep(1)
        with allure.step("获取当前页标签"):
            text = l.text_title()
        with allure.step("断言侧边栏，当前标签页状态"):
            pytest.assume(text == "我的工作台")

    @allure.story("我的工作台")
    @allure.title("快捷切换至个人审批页，查看切换后页面标签")
    def test_workbenck_title_02(self, get_driver):
        l = get_driver[3]
        with allure.step("点击个人审批快捷跳转"):
            l.click_jump_approve()
            time.sleep(1)
        with allure.step("断言当前页面是否出现异常提示"):
            alert_text = l.alert()
            pytest.assume(alert_text == False)
        with allure.step("获取当前页标签"):
            text = l.text_title()
        with allure.step("断言侧边栏，当前标签页状态"):
            pytest.assume(text == "个人审批")
        with allure.step("返回工作台頁面"):
            get_driver[0].back()


    @allure.story("我的工作台")
    @allure.title("快捷切换至讯息看板页，查看切换后页面标签")
    def test_workbenck_title_03(self, get_driver):
        l = get_driver[3]
        with allure.step("点击讯息看板快捷跳转"):
            l.click_jump_message()
            time.sleep(1)
        with allure.step("断言当前页面是否出现异常提示"):
            alert_text = l.alert()
            pytest.assume(alert_text == False)
        with allure.step("获取当前页标签"):
            text = l.text_title()
        with allure.step("断言侧边栏，当前标签页状态"):
            pytest.assume(text == "讯息看板")
        with allure.step("返回工作台頁面"):
            get_driver[0].back()

    @allure.story("我的工作台")
    @allure.title("快捷切换至证照档案页，查看切换后页面标签")
    def test_workbenck_title_04(self, get_driver):
        l = get_driver[3]
        with allure.step("点击证照档案快捷跳转"):
            l.click_jump_license()
            time.sleep(1)
        with allure.step("断言当前页面是否出现异常提示"):
            alert_text = l.alert()
            pytest.assume(alert_text == False)
        with allure.step("获取当前页标签"):
            text = l.text_title()
        with allure.step("断言侧边栏，当前标签页状态"):
            pytest.assume(text == "证照档案")
        with allure.step("返回工作台頁面"):
            get_driver[0].back()

    @allure.story("我的工作台")
    @allure.title("快捷切换至我的绩效页，查看切换后页面标签")
    def test_workbenck_title_05(self, get_driver):
        l = get_driver[3]
        with allure.step("点击我的绩效快捷跳转"):
            l.click_jump_performance()
            time.sleep(1)
        with allure.step("断言当前页面是否出现异常提示"):
            alert_text = l.alert()
            pytest.assume(alert_text == False)
        with allure.step("获取当前页标签"):
            text = l.text_title()
        with allure.step("断言侧边栏，当前标签页状态"):
            pytest.assume(text == "我的绩效")
        with allure.step("返回工作台頁面"):
            get_driver[0].back()

    @allure.story("我的工作台")
    @allure.title("快捷切换至我的客户页，查看切换后页面标签")
    def test_workbenck_title_06(self, get_driver):
        l = get_driver[3]
        with allure.step("点击我的客户快捷跳转"):
            l.click_jump_client()
            time.sleep(1)
        with allure.step("断言当前页面是否出现异常提示"):
            alert_text = l.alert()
            pytest.assume(alert_text == False)
        with allure.step("获取当前页标签"):
            text = l.text_title()
        with allure.step("断言侧边栏，当前标签页状态"):
            pytest.assume(text == "我的客户")
        with allure.step("返回工作台頁面"):
            get_driver[0].back()

    @allure.story("我的工作台")
    @allure.title("点击最新的系统消息，查看讯息详情页能否正常展开")
    def test_workbenck_title_07(self, get_driver):
        l = get_driver[3]
        with allure.step("点击最新的系统消息"):
            l.click_new_message()
            time.sleep(1)
        with allure.step("断言当前页面是否出现异常提示"):
            alert_text = l.alert()
            pytest.assume(alert_text == False)
        with allure.step("断言详情页标题是否和列表中的一致"):
            new_title = l.text_new_message_title()
            detail_title = l.text_message_detail_title()
            pytest.assume(new_title == detail_title)
        with allure.step("关闭详情页"):
            l.click_close_button_message()