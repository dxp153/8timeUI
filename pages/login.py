from common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from common.log import Log
import allure
import pytest
import time

_log = Log()

phone = (By.CSS_SELECTOR, ".phone_num .el-input__inner")
pwd = (By.CSS_SELECTOR, ".login_mode .el-input__inner")
login = (By.CSS_SELECTOR, "#pane-phoneLogin button")
user = (By.CSS_SELECTOR, ".avatar-wrapper.el-dropdown-selfdefine")
q = (By.XPATH, "//span[text()='退出登录']/..")

class Login(Base):

    @allure.step("查看系统提示是否显示")
    def alert(self):
        r = self.alter()
        return r

    @allure.step("输入手机号")
    def send_phone(self, phone_num="15797629873"):
        _log.info("输入手机号-- %s" % phone[1])
        self.sendkeys(phone, phone_num)

    @allure.step("输入密码")
    def send_pwd(self, pwd_num="dxp153"):
        _log.info("输入密码-- %s" % pwd[1])
        self.sendkeys(pwd, pwd_num)

    @allure.step("点击登录")
    def clikc_login(self):
        _log.info("点击登录-- %s" % login[1])
        self.clk(login)

    @allure.step("点击用户头像，退出登录")
    def user_quit(self):
        self.clk(user)
        time.sleep(0.5)
        self.clk(q)

    @allure.step("登录8小时")
    def login_8time(self, phone, pwd, alert=''):
        with allure.step("输入手机号"):
            self.send_phone(phone_num=phone)
        with allure.step("输入密码"):
            self.send_pwd(pwd_num=pwd)
        with allure.step("点击登录"):
            self.clikc_login()
        with allure.step("获取alter弹窗提示"):
            if self.alter():
                pytest.assume(self.alert == alert)
            else:
                return True


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://client.8timer.cn/#")
    driver.maximize_window()
    Login(driver).login_8time(phone='15797629873', pwd="dxp153")
    Login(driver).user_quit()
