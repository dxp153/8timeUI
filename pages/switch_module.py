from common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from common.log import Log
import allure
from pages.login import Login
import time

_log = Log()

workbench_state = (By.XPATH, "//span[text()='工作台']/../..")
workbench = (By.XPATH, "//span[text()='工作台']")
my_workbench = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='我的工作台']")
OA_state = (By.XPATH, "//span[text()='OA讯息']/../..")
OA = (By.XPATH, "//span[text()='OA讯息']")
message_board = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='讯息看板']")
message_list = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='讯息列表']")
message_approve = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='讯息审核']")
message_inform = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='企业通知']")
approve_state = (By.XPATH, "//span[text()='审批']/../..")
approve = (By.XPATH, "//span[text()='审批']")
approve_manage = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='审批管理']")
approve_collect = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='审批汇总']")
approve_personage = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='个人审批']")
jobs_state = (By.XPATH, "//span[text()='招聘管理']/../..")
jobs = (By.XPATH, "//span[text()='招聘管理']")
jobs_recruitment = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='招聘中']")
jobs_obsolete = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='已淘汰']")
jobs_post = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='招聘职位']")
jobs_talents = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='人才库']")
staff = (By.XPATH, "//span[text()='员工管理']")
staff_board = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='人事仪表盘']")
staff_roll = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='员工名册']")
staff_dimission = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='离职管理']")
staff_contract = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='合同管理']")
organization_state = (By.XPATH, "//span[text()='组织管理']/../..")
organization = (By.XPATH, "//span[text()='组织管理']")
organization_structure = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='组织架构']")
organization_chart = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='架构图']")
checking_state = (By.XPATH, "//span[text()='考勤管理']/../..")
checking = (By.XPATH, "//span[text()='考勤管理']")
checking_monthly_statistics = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='月度汇总']")
checking_daily_statistics = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='每日统计']")
checking_source_record = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='原始记录']")
checking_set = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='考勤设置']")
checking_overtime_rule = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='加班规则']")
checking_recess_staff = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='员工假期']")
checking_recess_rule = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='假勤规则']")
CRM_state = (By.XPATH, "//span[text()='CRM管理']/../..")
CRM = (By.XPATH, "//span[text()='CRM管理']")
CRM_data_statistics = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='数据统计']")
CRM_my_customers = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='我的客户']")
CRM_seas_customers = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='客户公海']")
CRM_all_customers = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='所有客户']")
CRM_business_portfolio = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='业务组设置']")
remuneration_state = (By.XPATH, "//span[text()='薪酬管理']/../..")
remuneration = (By.XPATH, "//span[text()='薪酬管理']")
remuneration_payroll_computation = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='薪资计算']")
remuneration_payroll_files = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='薪资档案']")
remuneration_special_deduction = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='专项附加扣除']")
remuneration_tax_detail = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='个税计算明细']")
performance_state = (By.XPATH, "//span[text()='绩效']/../..")
performance = (By.XPATH, "//span[text()='绩效']")
performance_management = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='绩效管理']")
performance_my = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='我的绩效']")
performance_set_up = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='绩效设置']")
social_security_state = (By.XPATH, "//span[text()='社保公积金']/../..")
social_security = (By.XPATH, "//span[text()='社保公积金']")
social_security_scheme = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='参保方案']")
social_security_staff = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='参保员工']")
social_security_monthly_scheme = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='月结方案']")
contract_state = (By.XPATH, "//span[text()='合同证照']/../..")
contract = (By.XPATH, "//span[text()='合同证照']")
contract_record= (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='合同档案']")
license_record = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='证照档案']")
cloud_storage_state = (By.XPATH, "//span[text()='云盘']/../..")
cloud_storage = (By.XPATH, "//span[text()='云盘']")
license_record_my = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='我的云盘']")
guarantee_slip_state = (By.XPATH, "//span[text()='保单管理']/../..")
guarantee_slip = (By.XPATH, "//span[text()='保单管理']")
guarantee_slip_list = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='保单列表']")
guarantee_slip_set = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='投保信息设置']")
guarantee_slip_log = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='保单日志列表']")
business_center = (By.XPATH, "//span[text()='企业中心']")
business_center_account = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='企业账户']")
business_center_pay = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='付费管理']")
business_center_note = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='短信管理']")
business_center_log = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='操作日志']")
business_center_feedback = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='意见反馈']")
business_center_custom = (By.XPATH, "//li[@class='el-submenu is-opened' or @class='el-submenu is-active is-opened']//span[text()='企业自定义']")


class Switch_Module(Base):

    @allure.step("查看系统提示是否显示")
    def alert(self):
        r = self.alter()
        return r

    @allure.step("获取工作台状态")
    def get_workbench_state(self):
        self.js_scrollIntoView(workbench_state)
        text = self.get_att(workbench_state, "class")
        return text

    @allure.step("点击工作台")
    def click_workbench(self):
        self.clk(workbench)

    @allure.step("点击跳转到--我的工作台")
    def click_my_workbench(self):
        self.clk(my_workbench)

    @allure.step("获取OA讯息状态")
    def get_message_board_state(self):
        self.js_scrollIntoView(OA_state)
        text = self.get_att(OA_state, "class")
        return text

    @allure.step("点击OA讯息")
    def click_message(self):
        self.clk(OA)

    @allure.step("点击跳转到--讯息看板")
    def click_message_board(self):
        self.clk(message_board)

    @allure.step("点击跳转到--讯息列表")
    def click_message_list(self):
        self.clk(message_list)

    @allure.step("点击跳转到--讯息审核")
    def click_message_approve(self):
        self.clk(message_approve)

    @allure.step("点击跳转到--企业通知")
    def click_message_inform(self):
        self.clk(message_inform)

    @allure.step("获取审批状态")
    def get_approve_state(self):
        self.js_scrollIntoView(approve_state)
        text = self.get_att(approve_state, "class")
        return text

    @allure.step("点击审批")
    def click_approve(self):
        self.clk(approve)

    @allure.step("点击跳转到--审批管理")
    def click_approve_manage(self):
        self.clk(approve_manage)

    @allure.step("点击跳转到--审批汇总")
    def click_approve_collect(self):
        self.clk(approve_collect)

    @allure.step("点击跳转到--个人审批")
    def click_approve_personage(self):
        self.clk(approve_personage)

    @allure.step("获取招聘职位状态")
    def get_jobs_state(self):
        self.js_scrollIntoView(jobs_state)
        text = self.get_att(jobs_state, "class")
        return text

    @allure.step("点击招聘职位")
    def click_jobs(self):
        self.clk(jobs)

    @allure.step("点击跳转到--招聘中")
    def click_jobs_recruitment(self):
        self.clk(jobs_recruitment)

    @allure.step("点击跳转到--已淘汰")
    def click_jobs_obsolete(self):
        self.clk(jobs_obsolete)

    @allure.step("点击跳转到--招聘职位")
    def click_jobs_post(self):
        self.clk(jobs_post)

    @allure.step("点击跳转到--人才库")
    def click_jobs_talents(self):
        self.clk(jobs_talents)

    @allure.step("点击员工名册")
    def click_staff(self):
        self.clk(staff)

    @allure.step("点击跳转到--人事仪表盘")
    def click_staff_board(self):
        self.clk(staff_board)

    @allure.step("点击跳转到--员工名册")
    def click_staff_roll(self):
        self.clk(staff_roll)

    @allure.step("点击跳转到--离职管理")
    def click_staff_dimission(self):
        self.clk(staff_dimission)

    @allure.step("点击跳转到--合同管理")
    def click_staff_contract(self):
        self.clk(staff_contract)

    @allure.step("获取组织管理状态")
    def get_organization_state(self):
        self.js_scrollIntoView(organization_state)
        text = self.get_att(organization_state, "class")
        return text

    @allure.step("点击组织管理")
    def click_organization(self):
        self.clk(organization)

    @allure.step("点击跳转到--组织架构")
    def click_organization_structure(self):
        self.clk(organization_structure)

    @allure.step("点击跳转到--架构图")
    def click_organization_chart(self):
        self.clk(organization_chart)

    @allure.step("获取考勤管理状态")
    def get_checking_state(self):
        self.js_scrollIntoView(checking_state)
        text = self.get_att(checking_state, "class")
        return text

    @allure.step("点击考勤管理")
    def click_checking(self):
        self.clk(checking)

    @allure.step("点击跳转到--月度汇总")
    def click_checking_monthly_statistics(self):
        self.clk(checking_monthly_statistics)

    @allure.step("点击跳转到--每日统计")
    def click_checking_daily_statistics(self):
        self.clk(checking_daily_statistics)

    @allure.step("点击跳转到--原始记录")
    def click_checking_source_record(self):
        self.clk(checking_source_record)

    @allure.step("点击跳转到--考勤设置")
    def click_checking_set(self):
        self.clk(checking_set)

    @allure.step("点击跳转到--加班规则")
    def click_checking_overtime_rule(self):
        self.clk(checking_overtime_rule)

    @allure.step("点击跳转到--员工假期")
    def click_checking_recess_staff(self):
        self.clk(checking_recess_staff)

    @allure.step("点击跳转到--假勤规则")
    def click_checking_recess_rule(self):
        self.clk(checking_recess_rule)

    @allure.step("获取CRM管理状态")
    def get_CRM_state(self):
        self.js_scrollIntoView(CRM_state)
        text = self.get_att(CRM_state, "class")
        return text

    @allure.step("点击CRM管理")
    def click_CRM(self):
        self.clk(CRM)

    @allure.step("点击跳转到--数据统计")
    def click_CRM_data_statistics(self):
        self.clk(CRM_data_statistics)

    @allure.step("点击跳转到--我的客户")
    def click_CRM_my_customers(self):
        self.clk(CRM_my_customers)

    @allure.step("点击跳转到--客户公海")
    def click_CRM_seas_customers(self):
        self.clk(CRM_seas_customers)

    @allure.step("点击跳转到--所有客户")
    def click_CRM_all_customers(self):
        self.clk(CRM_all_customers)

    @allure.step("点击跳转到--业务组设置")
    def click_CRM_business_portfolio(self):
        self.clk(CRM_business_portfolio)

    @allure.step("获取薪酬管理状态")
    def get_remuneration_state(self):
        self.js_scrollIntoView(remuneration_state)
        text = self.get_att(remuneration_state, "class")
        return text

    @allure.step("点击薪酬管理")
    def click_remuneration(self):
        self.clk(remuneration)

    @allure.step("点击跳转到--薪资计算")
    def click_remuneration_payroll_computation(self):
        self.clk(remuneration_payroll_computation)

    @allure.step("点击跳转到--薪资档案")
    def click_remuneration_payroll_files(self):
        self.clk(remuneration_payroll_files)

    @allure.step("点击跳转到--专项附加扣除")
    def click_remuneration_special_deduction(self):
        self.clk(remuneration_special_deduction)

    @allure.step("点击跳转到--个税计算明细")
    def click_remuneration_tax_detail(self):
        self.clk(remuneration_tax_detail)

    @allure.step("获取绩效状态")
    def get_performance_state(self):
        self.js_scrollIntoView(performance_state)
        text = self.get_att(performance_state, "class")
        return text

    @allure.step("点击绩效")
    def click_performance(self):
        self.clk(performance)

    @allure.step("点击跳转到--绩效管理")
    def click_performance_management(self):
        self.clk(performance_management)

    @allure.step("点击跳转到--我的绩效")
    def click_performance_my(self):
        self.clk(performance_my)

    @allure.step("点击跳转到--绩效设置")
    def click_performance_set_up(self):
        self.clk(performance_set_up)

    @allure.step("获取社保公积金状态")
    def get_social_security_state(self):
        self.js_scrollIntoView(social_security_state)
        text = self.get_att(social_security_state, "class")
        return text

    @allure.step("点击社保公积金")
    def click_social_security(self):
        self.clk(social_security)

    @allure.step("点击跳转到--参保方案")
    def click_social_security_scheme(self):
        self.clk(social_security_scheme)

    @allure.step("点击跳转到--参保员工")
    def click_social_security_staff(self):
        self.clk(social_security_staff)

    @allure.step("点击跳转到--月结方案")
    def click_social_security_monthly_scheme(self):
        self.clk(social_security_monthly_scheme)

    @allure.step("获取合同证照状态")
    def get_contract_state(self):
        self.js_scrollIntoView(contract_state)
        text = self.get_att(contract_state, "class")
        return text

    @allure.step("点击合同证照")
    def click_contract(self):
        self.clk(contract)

    @allure.step("点击跳转到--合同档案")
    def click_contract_record(self):
        self.clk(contract_record)

    @allure.step("点击跳转到--证照档案")
    def click_license_record(self):
        self.clk(license_record)

    @allure.step("获取云盘状态")
    def get_cloud_storage(self):
        self.js_scrollIntoView(cloud_storage_state)
        text = self.get_att(cloud_storage_state, "class")
        return text

    @allure.step("点击云盘")
    def click_cloud_storage(self):
        self.clk(cloud_storage)

    @allure.step("点击跳转到--我的云盘")
    def click_license_record_my(self):
        self.clk(license_record_my)

    @allure.step("获取保单管理状态")
    def get_guarantee_slip_storage(self):
        self.js_scrollIntoView(guarantee_slip_state)
        text = self.get_att(guarantee_slip_state, "class")
        return text

    @allure.step("点击保单管理")
    def click_guarantee_slip(self):
        self.clk(guarantee_slip)

    @allure.step("点击跳转到--保单列表")
    def click_guarantee_slip_list(self):
        self.clk(guarantee_slip_list)

    @allure.step("点击跳转到--投保信息设置")
    def click_guarantee_slip_set(self):
        self.clk(guarantee_slip_set)

    @allure.step("点击跳转到--保单日志列表")
    def click_guarantee_slip_log(self):
        self.clk(guarantee_slip_log)

    @allure.step("获取企业中心状态")
    def get_business_center(self):
        self.js_scrollIntoView(business_center)
        text = self.get_att(business_center, "class")
        return text

    @allure.step("点击企业中心")
    def click_business_center(self):
        self.clk(business_center)

    @allure.step("点击跳转到--企业账户")
    def click_business_center_account(self):
        self.js_scrollIntoView(business_center_account)
        self.clk(business_center_account)

    @allure.step("点击跳转到--付费管理")
    def click_business_center_pay(self):
        self.js_scrollIntoView(business_center_pay)
        self.clk(business_center_pay)

    @allure.step("点击跳转到--短信管理")
    def click_business_center_note(self):
        self.js_scrollIntoView(business_center_note)
        self.clk(business_center_note)

    @allure.step("点击跳转到--操作日志")
    def click_business_center_log(self):
        self.js_scrollIntoView(business_center_log)
        self.clk(business_center_log)

    @allure.step("点击跳转到--意见反馈")
    def click_business_center_feedback(self):
        self.js_scrollIntoView(business_center_feedback)
        self.clk(business_center_feedback)

    @allure.step("点击跳转到--企业自定义")
    def click_business_center_custom(self):
        self.js_scrollIntoView(business_center_custom)
        self.clk(business_center_custom)