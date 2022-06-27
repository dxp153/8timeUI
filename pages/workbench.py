from common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from common.log import Log
import allure
from pages.login import Login
import time

_log = Log()

system_prompt = (By.CSS_SELECTOR, ".el-message--error .el-message__content")
title = (By.CSS_SELECTOR, ".el-menu-item.is-active span")
jump_approve = (By.XPATH, "//div[text()='个人审批']/..")
jump_message = (By.XPATH, "//div[text()='讯息看板']/..")
jump_license = (By.XPATH, "//div[text()='证照档案']/..")
jump_performance = (By.XPATH, "//div[text()='我的绩效']/..")
jump_client = (By.XPATH, "//div[text()='我的客户']/..")
new_message = (By.CSS_SELECTOR, ".news_title.clearfix+div")
new_message_title = (By.CSS_SELECTOR, ".news_title.clearfix+div span.newscontentbox")
message_detail_title = (By.CSS_SELECTOR, ".grid-content.bg-purple.lookStyle")
close_button_message = (By.CSS_SELECTOR, ".el-dialog__body+div .dialog-footer button")
close_x_message = (By.CSS_SELECTOR, ".app-main  div.el-dialog__wrapper:nth-child(5) i")
message_detail = (By.XPATH, "//div[@class='el-dialog__wrapper' and @style != 'display: none;'][1]")



class Workbench(Base):

    @allure.step("查看系统提示是否显示")
    def alert(self):
        r = self.alter()
        return r

    @allure.step("获取当前页面标签")
    def text_title(self):
        #   点击状态is-active
        _log.info("定位工作台侧边栏菜单-- %s" % title[1])
        text = self.rtext(title)
        return text

    @allure.step("点击个人审批的快捷跳转")
    def click_jump_approve(self):
        _log.info("点击个人审批的快捷跳转-- %s" % jump_approve[1])
        self.clk(jump_approve)

    @allure.step("点击讯息看板的快捷跳转")
    def click_jump_message(self):
        _log.info("点击讯息看板的快捷跳转-- %s" % jump_message[1])
        self.clk(jump_message)

    @allure.step("点击证照档案的快捷跳转")
    def click_jump_license(self):
        _log.info("点击证照档案的快捷跳转-- %s" % jump_license[1])
        self.clk(jump_license)

    @allure.step("点击我的绩效的快捷跳转")
    def click_jump_performance(self):
        _log.info("点击我的绩效的快捷跳转-- %s" % jump_performance[1])
        self.clk(jump_performance)

    @allure.step("点击我的客户的快捷跳转")
    def click_jump_client(self):
        _log.info("点击我的客户的快捷跳转-- %s" % jump_client[1])
        self.clk(jump_client)

    @allure.step("点击最新的一条消息提醒")
    def click_new_message(self):
        _log.info("点击最新的一条消息提醒-- %s" % new_message[1])
        self.clk(new_message)

    @allure.step("获取最新一条消息的标题")
    def text_new_message_title(self):
        _log.info("获取最新一条消息的标题-- %s" % new_message_title[1])
        self.rtext(new_message_title)

    @allure.step("获取讯息详情页标题名")
    def text_message_detail_title(self):
        _log.info("获取讯息详情页标题名-- %s" % message_detail_title[1])
        self.rtext(message_detail_title)

    @allure.step("关闭按钮关闭讯息")
    def click_close_button_message(self):
        _log.info("关闭按钮关闭讯息-- %s" % close_button_message[1])
        self.clk(close_button_message)

    @allure.step("点击X号关闭讯息")
    def click_close_x_message(self):
        _log.info("点击X号关闭讯息-- %s" % close_x_message[1])
        self.clk(close_x_message)

    @allure.step("滑动关闭讯息")
    def slid_close_message(self):
        self.js_scrollIntoView(close_button_message)
        self.click_close_button_message()

    @allure.step("判断讯息弹窗是否关闭")
    def assume_close_message(self):
        r = EC.staleness_of(message_detail)
        return r


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://client.8timer.cn/#")
    driver.maximize_window()
    Login(driver).login_8time(phone='15797629873', pwd="dxp153")
    time.sleep(1)
    Workbench(driver).click_new_message()
    time.sleep(1)
    Workbench(driver).slid_close_message()
    time.sleep(1)
    t = Workbench(driver).assume_close_message()
    print(t)
    driver.quit()