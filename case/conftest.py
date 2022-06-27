import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login import Login
from pages.workbench import Workbench
from pages.switch_module import Switch_Module


@pytest.fixture(scope='session')
def get_driver():
    #   打开浏览器
    # option = webdriver.ChromeOptions()
    # option.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=option)  # 静默启动
    driver = webdriver.Chrome()
    #   隐示等待20秒
    driver.implicitly_wait(20)
    #   实例化 LoginFun
    login = Login(driver)
    switch = Switch_Module(driver)
    work = Workbench(driver)
    yield driver, login, switch, work
    #   退出浏览器
    driver.quit()


@allure.step("登录8小时协同办公")
@pytest.fixture(scope="class")
def login_8time(get_driver):
    """登录8小时协同办公"""
    driver = get_driver[0]
    driver.get("http://client.8timer.cn/#")
    driver.maximize_window()
    driver.refresh()
    login = get_driver[1]
    login.login_8time(phone='15797629873', pwd="dxp153")
    yield
    login.user_quit()


if __name__ == "__main__":
    login_8time()
