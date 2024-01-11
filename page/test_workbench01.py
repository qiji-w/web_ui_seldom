import time
from datetime import datetime
from time import sleep

import seldom

from selenium.webdriver.common.by import By

from element.login import IndLoginPage
from element.privatization_workbench import WorkbenchPage
from config import privatization_config


#
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
#
# # 等待元素加载 - 显示等待
# def wait_presence(driver, locator, timeout=10, poll=0.2):
#     """
#     :param locator: 元素表达式。格式为：('id', 'kw')
#     :param timeout: 元素等待请求时间
#     :param poll:    元素等待请求间隔时间
#     :return:
#     """
#     try:
#         wait = WebDriverWait(driver, timeout=timeout, poll_frequency=poll)
#         el = wait.until(expected_conditions.presence_of_element_located(locator))
#         return el
#     except Exception as e:
#         print("等待元素加载失败:", e)
#
#
# # 等待元素可以被点击
# def wait_clickable(driver, locator, timeout=10, poll=0.2):
#     """
#     :param locator: 元素表达式。格式为：('id', 'kw')
#     :param timeout: 元素等待请求时间
#     :param poll:    元素等待请求间隔时间
#     :return:
#     """
#     try:
#         wait = WebDriverWait(driver, timeout=timeout, poll_frequency=poll)
#         el = wait.until(expected_conditions.element_to_be_clickable(locator))
#         return el
#     except Exception as e:
#         print("等待元素可以被点击方法失败:", e)
#
#
# # 显示等待查找元素 显示等待+条件判断，等到元素加载到dom中且可见
# def explicit_wait_util_ele_locate(driver, locator, timeout) :
#     """locator：元素定位器
#         timeout：显示等待超时时间
#     """
#     return WebDriverWait(driver, timeout).until(
#         ec.visibility_of_element_located(locator), message="element not located!")
#

# @seldom.skip()
class WorkbenchTest01(seldom.TestCase):
    """
    主要包含场景：登录
    """

    def start_class(self):
        # 先访问地址
        login_page = IndLoginPage(self.driver)
        login_page.open(privatization_config.TEST_URL)

        # request_login_url = privatization_config.TEST_URL + 'api/v1/signin'
        # headers = {'Content-Type': 'application/json'}
        # cookie = {'company': 'mastergo'}
        # json = {"identity": privatization_config.TEST_ACCOUNT, "password": privatization_config.TEST_PASSWORD}
        # cookies = self.post(url=request_login_url, headers=headers, json=json).cookies.get_dict()
        # cookies = self.post(url=request_login_url, headers=headers, json=json, cookies=cookie).cookies.get_dict()
        # driver_cookies_list = [{'name': name, 'value': value} for name, value in cookies.items()]
        # self.add_cookies(driver_cookies_list)
        # self.add_cookie({'name': 'company', 'value': 'mastergo'})
        #
        # # cookies添加成功之后，带cookies访问
        # login_page = IndLoginPage(self.driver)
        # login_page.open(privatization_config.TEST_URL)

        # self.max_window()
        self.set_window(1500, 1000)
        print("11111111111")
        sleep(200)

    def test_01_login(self):
        """私有化登录测试"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.homepage.click()

    def test_02_delete_team(self):
        """初始化删除所有团队项目"""
        workbench_page = WorkbenchPage(self.driver)
        while True:
            try:
                text = workbench_page.team_name_setup1.text.strip()
            except Exception as e:
                # print(e)
                # self.refresh()
                self.open(privatization_config.TEST_URL)
                break
            else:
                workbench_page.team_name_setup1.click()
                sleep(1)
                workbench_page.team_setting.click()
                sleep(1)
                workbench_page.team_setting_deleteBtn.click()
                sleep(3)
                # workbench_page.team_name_setup1.context_click()
                # workbench_page.team_context_click_delete.click()
                workbench_page.team_delete_input_name.send_keys(text)
                sleep(2)

                workbench_page.team_delete_confirm_button.click()
                sleep(1)

                # self.refresh()
                self.open(privatization_config.TEST_URL)


# @seldom.skip()
class WorkbenchTest02(seldom.TestCase):
    """
    场景：初始化创建团队项目、文件分组、文件容器图层
    """

    def test_01_create_team(self):
        """创建团队"""
        workbench_page = WorkbenchPage(self.driver)
        sleep(2)
        workbench_page.new_team_button.click()
        sleep(2)
        workbench_page.input_team_name.send_keys('autoceshi的团队')
        sleep(2)
        workbench_page.create_team_button.click()
        toast = workbench_page.create_team_toast.text
        self.assertEqual(toast, '团队创建成功')
        sleep(2)
        workbench_page.close_member_invitation_window.click()

    def test_02_create_project(self):
        """创建项目"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.create_project_button.click()
        sleep(2)
        workbench_page.input_project_name.send_keys('团队项目')
        sleep(2)
        workbench_page.create_project_determine_button.click()
        sleep(2)
        title = workbench_page.project_header_title.text
        self.assertEqual(title, '团队项目')

    def test_03_create_team_file(self):
        """创建文件"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.create_file_button.click()
        sleep(5)

        # file_name = workbench_page.file_name_div.text
        # self.assertEqual(file_name, '新文件')

        # ele = self.driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/span/div[1]/div[1]/div[2]/div[2]/div')[0]
        # ele.click()

        workbench_page.project_name_div.click()
        sleep(3)

    def test_04_rename_team_file(self):
        """项目落地页-文件右键-重命名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.project_first_file_name.context_click()
        sleep(2)
        workbench_page.context_click_rename.click()
        sleep(2)
        workbench_page.project_first_file_rename_input.send_keys('Beats耳机落地页')
        sleep(2)
        workbench_page.project_first_file_rename_input.enter()
        sleep(2)
        file_name = workbench_page.project_first_file_name.text
        self.assertEqual(file_name, 'Beats耳机落地页')

    def test_05_file_create_group(self):
        """项目团队-选择文件分组"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.my_team_project.click()
        sleep(2)
        workbench_page.new_group_right.click()
        sleep(2)
        workbench_page.new_group_right_file.click()

    def test_06_second_enter_canvas(self):
        """画布页返回工作台，再次点击文件进入文件页"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.my_team_project.click()
        sleep(2)
        workbench_page.project_first_file_name.double_click()
        # file_name = workbench_page.file_name_div.text
        # self.assertEqual(file_name, 'Beats耳机落地页')

    def test_07_file_create_group(self):
        """画布页-创建容器"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.file_group_button.click()
        sleep(2)
        workbench_page.file_canvas_button.double_click()
        sleep(2)
        workbench_page.left_corner_menu.click()
        sleep(2)
        workbench_page.left_corner_menu_return.click()


# @seldom.skip()
class WorkbenchTest03(seldom.TestCase):
    """
    场景：创建团队、项目、团队文件，重命名文件、项目、团队，创建团队文件副本，删除团队文件副本、团队文件、项目、团队，
    永久删除团队文件、团队文件副本
    """

    def test_01_create_team(self):
        """创建团队"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.new_team_button.click()
        sleep(2)
        workbench_page.input_team_name.send_keys('自动化测试团队')
        sleep(2)
        workbench_page.input_team_desc.send_keys('自动化测试团队描述')
        workbench_page.create_team_button.click()
        sleep(2)
        toast = workbench_page.create_team_toast.text
        self.assertEqual(toast, '团队创建成功')
        sleep(2)
        workbench_page.close_member_invitation_window.click()

    def test_02_create_project(self):
        """创建项目"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.create_project_button.click()
        sleep(2)
        workbench_page.input_project_name.send_keys('自动化项目')
        sleep(2)
        workbench_page.create_project_determine_button.click()
        title = workbench_page.project_header_title.text
        sleep(1)
        self.assertEqual(title, '自动化项目')

        privatization_config.HERF = self.get_url
        sleep(5)

    def test_03_create_team_file(self):
        """创建文件"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.create_file_button.click()
        sleep(2)
        # file_name = workbench_page.file_name_div.text
        # self.assertEqual(file_name, '新文件')
        workbench_page.project_name_div.click()
        sleep(2)

    def test_04_creat_copy(self):
        """项目落地页-文件右键-创建副本"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.project_first_file_name.context_click()
        sleep(2)
        workbench_page.context_click_create_copy.click()
        sleep(2)
        copy_name = workbench_page.first_file.text.strip()
        sleep(1)
        self.assertEqual(copy_name, '新文件 副本')

    def test_05_rename_team_file(self):
        """项目落地页-文件右键-重命名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.project_first_file_name.context_click()
        sleep(2)
        workbench_page.context_click_rename.click()
        sleep(2)
        workbench_page.project_first_file_rename_input.send_keys('自动化文件重命名')
        sleep(2)
        workbench_page.project_first_file_rename_input.enter()
        sleep(2)
        file_name = workbench_page.project_first_file_name.text.strip()
        sleep(1)
        self.assertEqual(file_name, '自动化文件重命名')

        self.open(privatization_config.HERF)
        sleep(8)

    def test_06_delete_file(self):
        """项目落地页-文件右键-删除"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.first_file.click()
        sleep(2)
        workbench_page.first_file.context_click()
        workbench_page.context_click_delete.click()
        sleep(2)
        workbench_page.project_first_file_name.click()
        sleep(2)
        workbench_page.project_first_file_name.context_click()
        sleep(2)
        workbench_page.context_click_delete.click()
        sleep(1)
        self.assertEqual(workbench_page.no_file.text.strip(), '这里还没有文件')

    def test_07_team_recycle_bin(self):
        """团队回收站操作恢复、永久删除"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.team_name.click()
        sleep(2)
        workbench_page.team_recycling_tab.click()

        workbench_page.first_file.context_click()
        sleep(2)
        workbench_page.recycle_bin_recover.click()
        sleep(2)

        workbench_page.first_file.context_click()
        sleep(2)
        workbench_page.recycle_bin_permanently_delete.click()
        sleep(2)
        workbench_page.recycle_bin_permanently_delete_confirm.click()
        sleep(1)

        self.assertEqual(workbench_page.no_file.text.strip(), '回收站是空的')

    def test_08_rename_project(self):
        """项目重命名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.project_name.context_click()
        sleep(2)
        workbench_page.project_context_click_rename.click()
        sleep(2)
        workbench_page.project_first_file_rename_input.send_keys('项目重命名测试')
        sleep(2)
        workbench_page.project_first_file_rename_input.enter()
        sleep(2)
        project_name = workbench_page.project_name.text.strip()
        sleep(1)
        self.assertEqual(project_name, '项目重命名测试')

    def test_09_delete_project(self):
        """项目删除"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.project_name.click()
        sleep(2)
        workbench_page.project_name.context_click()
        sleep(2)
        workbench_page.project_context_click_delete.click()
        sleep(2)
        workbench_page.project_delete_confirm_button.click()
        sleep(1)
        self.assertEqual(workbench_page.no_project.text, '暂无项目')

    def test_10_rename_team(self):
        """团队重命名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.team_name.context_click()
        sleep(2)
        workbench_page.team_context_click_rename.click()
        sleep(2)
        workbench_page.project_first_file_rename_input.send_keys('团队重命名测试')
        sleep(2)
        workbench_page.project_first_file_rename_input.enter()
        sleep(2)
        team_name = workbench_page.team_name.text.strip()
        sleep(1)
        self.assertEqual(team_name, '团队重命名测试')

    def test_11_delete_team(self):
        """删除团队"""
        # workbench_page = WorkbenchPage(self.driver)
        # workbench_page.team_name.context_click()
        # workbench_page.team_context_click_delete.click()
        # workbench_page.team_delete_input_name.send_keys('团队重命名测试')
        # workbench_page.team_delete_confirm_button.click()
        # workbench_page.sleep(1)
        # self.assertEqual(workbench_page.homepage_title.text, "主页")
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.team_name.click()
        sleep(1)
        workbench_page.team_setting.click()
        sleep(1)
        workbench_page.team_setting_deleteBtn.click()
        sleep(3)
        workbench_page.team_delete_input_name.send_keys('团队重命名测试')
        sleep(2)
        workbench_page.team_delete_confirm_button.click()
        sleep(1)
        # self.refresh()
        sleep(1)
        self.assertEqual(workbench_page.homepage_title.text, "主页")


# @seldom.skip()
class WorkbenchTest04(seldom.TestCase):
    """
    场景：主页、草稿箱、分享给我的、回收站页面跳转功能
    """

    def test_jump_01(self):
        """登录后跳转草稿箱"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.drafts.click()
        sleep(1)
        drafts_title = workbench_page.drafts_tab.text
        self.assertEqual(drafts_title, "草稿箱")

    def test_jump_02(self):
        """跳转分享给我的"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.share_with_me.click()
        sleep(2)
        share_with_me_title = workbench_page.share_with_me_title.text
        sleep(1)
        self.assertEqual(share_with_me_title, "分享给我的")

    def test_jump_03(self):
        """跳转至主页"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.homepage.click()
        sleep(2)
        homepage_title = workbench_page.homepage_title.text
        sleep(1)
        self.assertEqual(homepage_title, "主页")

    def test_jump_04(self):
        """跳转个人草稿箱tab"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.drafts.click()
        sleep(2)
        workbench_page.drafts_tab.click()
        sleep(1)
        self.assertEqual(workbench_page.no_file.text, '这里还没有文件')

    def test_jump_05(self):
        """跳转草稿箱回收站tab"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.personal_recycle_bin_tab.click()
        sleep(1)
        self.assertEqual(workbench_page.no_file.text, '回收站是空的')


# @seldom.skip()
class WorkbenchTest05(seldom.TestCase):
    """
    场景：新建个人文件，个人文件创建副本，删除个人文件、副本，回收站恢复个人文件、个人文件副本，
    回收站彻底删除个人文件、个人文件副本
    """

    def test_01_create_personal_file(self):
        """创建个人文件"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.drafts.click()
        sleep(2)
        workbench_page.create_file_button.click()
        sleep(2)
        # file_name = workbench_page.file_name_div.text
        # self.assertEqual(file_name, '新文件')
        workbench_page.project_name_div.click()

    def test_02_create_personal_file_copy(self):
        """个人文件-右键创建副本"""
        workbench_page = WorkbenchPage(self.driver)
        sleep(2)
        workbench_page.project_first_file_name.context_click()
        sleep(2)
        workbench_page.context_click_create_copy.click()
        sleep(2)
        copy_name = workbench_page.first_file.text
        sleep(1)
        self.assertEqual(copy_name, '新文件 副本')

    def test_03_delete_personal_file(self):
        """删除个人文件副本、个人文件"""
        workbench_page = WorkbenchPage(self.driver)
        for i in range(len(workbench_page.file_name_list)):
            workbench_page.first_file.context_click()
            workbench_page.context_click_delete.click()
            workbench_page.sleep(1)
        self.assertEqual(workbench_page.no_file.text, '这里还没有文件')

    def test_04_recover_file(self):
        """回收站恢复个人文件、个人文件副本"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.personal_recycle_bin_tab.click()
        for i in range(len(workbench_page.file_name_list)):
            workbench_page.first_file.context_click()
            workbench_page.recycle_bin_recover.click()
            sleep(1)
        self.assertEqual(workbench_page.no_file.text, '回收站是空的')

    def test_05_permanently_delete_personal_file(self):
        """永久删除回收站的个人文件、个人文件副本"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.drafts_tab.click()

        for i in range(len(workbench_page.file_name_list)):
            workbench_page.first_file.context_click()
            workbench_page.context_click_delete.click()
            sleep(1)

        workbench_page.personal_recycle_bin_tab.click()

        for i in range(len(workbench_page.file_name_list)):
            workbench_page.first_file.context_click()
            workbench_page.recycle_bin_permanently_delete.click()
            workbench_page.recycle_bin_permanently_delete_confirm.click()
            sleep(1)

        self.assertEqual(workbench_page.no_file.text, '回收站是空的')


# @seldom.skip()
class WorkbenchTest06(seldom.TestCase):
    """
    场景：
    新增、修改、删除分组
    主页-切换列表视图、网格视图
    深浅色模式切换
    团队成员备注名
    """

    def test_01_new_group(self):
        """新建分组"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.my_team_project.click()
        sleep(2)
        workbench_page.new_group.click()
        workbench_page.input_group_name.send_keys('自动化分组')
        sleep(2)
        workbench_page.new_group_confirm_button.click()
        sleep(1)
        self.assertEqual(workbench_page.new_group_name.text, '自动化分组')

    def test_02_rename_group(self):
        """分组重命名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.new_group_name.context_click()
        sleep(2)
        workbench_page.group_rename.click()
        sleep(2)
        workbench_page.input_group_name.select_all()
        sleep(2)
        workbench_page.input_group_name.backspace()
        sleep(2)
        workbench_page.input_group_name.send_keys('分组重命名')
        sleep(2)
        workbench_page.new_group_confirm_button.click()
        sleep(1)
        self.assertEqual(workbench_page.new_group_name.text, '分组重命名')

    def test_03_remove_group(self):
        """分组删除"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.new_group_name.context_click()
        sleep(2)
        workbench_page.group_remove.click()
        sleep(2)
        workbench_page.group_remove_confirm_button.click()
        sleep(1)
        self.assertEqual(workbench_page.new_group_name.text, '未分组')

    def test_04_switch_view_list(self):
        """主页网格视图切换列表视图"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.homepage.click()
        sleep(2)
        workbench_page.views_switch.click()
        sleep(1)
        self.assertEqual(workbench_page.file_name_header.text, '文件名称')

    def test_05_switch_view_grid(self):
        """主页列表视图切换网格视图"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.homepage.click()
        sleep(2)
        workbench_page.views_switch.click()
        sleep(1)
        self.assertEqual(workbench_page.recent_open.text, '最近打开')

    def test_06_switch_dark_mode(self):
        """切换为深色模式"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.head_portrait.click()
        sleep(2)
        workbench_page.switch_theme.click()
        sleep(2)
        workbench_page.head_portrait.click()
        sleep(2)

    def test_07_switch_white_mode(self):
        """切换为浅色模式"""
        workbench_page = WorkbenchPage(self.driver)
        self.refresh()
        sleep(7)
        workbench_page.head_portrait.click()
        sleep(2)
        self.assertEqual(workbench_page.switch_theme.text, '切换至浅色模式')
        sleep(2)
        workbench_page.switch_theme.click()
        sleep(2)
        self.assertEqual(workbench_page.switch_theme.text, '切换至深色模式')
        sleep(2)
        workbench_page.head_portrait.click()

    def test_08_team_nick_name(self):
        """新增团队备注名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.my_team.click()
        sleep(2)
        workbench_page.team_member_tab.click()
        sleep(2)
        workbench_page.nick_name_button.click()
        sleep(2)
        workbench_page.input_nick_name.select_all()
        sleep(2)
        workbench_page.input_nick_name.backspace()
        sleep(2)
        workbench_page.input_nick_name.send_keys('自动化备注名')
        sleep(2)
        workbench_page.new_group_confirm_button.click()
        sleep(1)
        self.assertEqual(workbench_page.team_member_name.text, '自动化备注名')

    def test_09_modify_team_nick_name(self):
        """修改团队备注名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.nick_name_button.click()
        sleep(2)
        workbench_page.input_nick_name.select_all()
        sleep(2)
        workbench_page.input_nick_name.backspace()
        sleep(2)
        workbench_page.input_nick_name.send_keys('修改备注名')
        sleep(2)
        workbench_page.new_group_confirm_button.click()
        sleep(1)
        self.assertEqual(workbench_page.team_member_name.text, '修改备注名')

    def test_10_delete_team_nick_name(self):
        """删除团队备注名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.nick_name_button.click()
        sleep(2)
        workbench_page.input_nick_name.select_all()
        sleep(2)
        workbench_page.input_nick_name.backspace()
        sleep(2)
        workbench_page.new_group_confirm_button.click()
        sleep(2)
        self.assertEqual(workbench_page.team_member_name.text, 'e2e')


# @seldom.skip()
class WorkbenchTest07(seldom.TestCase):
    """
    场景：
    二次进入画布页、手动保存历史版本
    """

    def test_01_second_enter_canvas(self):
        """画布页返回工作台，再次点击文件进入文件页"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.my_team_project.click()
        sleep(2)
        workbench_page.project_first_file_name.double_click()
        # file_name = workbench_page.file_name_div.text
        # self.assertEqual(file_name, 'Beats耳机落地页')
        sleep(2)
        workbench_page.left_corner_menu.click()
        sleep(2)
        workbench_page.left_corner_menu_return.click()
        sleep(1)
        self.assertEqual(workbench_page.project_header_title.text, '团队项目')

        workbench_page.project_first_file_name.double_click()
        # file_name = workbench_page.file_name_div.text
        # self.assertEqual(file_name, 'Beats耳机落地页')

    def test_02_save_version(self):
        """手动保存历史版本"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.file_name_right_drop_down_button.click()
        sleep(2)
        workbench_page.add_to_version_history.click()
        sleep(2)
        workbench_page.version_history_title.send_keys('手动保存版本 %s' % datetime.today())
        sleep(2)
        workbench_page.version_history_content.send_keys('%s' % datetime.today())
        sleep(2)
        workbench_page.version_history_save.click()
        sleep(2)
        workbench_page.file_name_right_drop_down_button.click()
        workbench_page.show_version_history.click()
        sleep(1)
        self.assertIn('手动保存版本', workbench_page.recent_history_version_title.text)
        sleep(2)
        workbench_page.return_to_edit.click()

    def test_03_section_views_switch(self):
        """组件面板宫格、列表模式切换"""
        workbench_page = WorkbenchPage(self.driver)
        sleep(2)
        workbench_page.section_tab.click()
        sleep(2)
        for i in range(2):
            workbench_page.section_views_switch.move_to_element()
            sleep(4)
            hover = workbench_page.section_views_switch_hover.text
            if hover == '切换宫格':
                workbench_page.section_views_switch.click()
                sleep(4)
                hover = workbench_page.section_views_switch_hover.text
                self.assertEqual(hover, '切换列表')
            else:
                workbench_page.section_views_switch.click()
                hover = workbench_page.section_views_switch_hover.text
                sleep(4)
                self.assertEqual(hover, '切换宫格')
        workbench_page.layer_tab.click()

    def test_04_rename_left_tree(self):
        """左侧树图层重命名"""
        workbench_page = WorkbenchPage(self.driver)
        workbench_page.first_layer.double_click()
        sleep(2)
        workbench_page.rename_layer_input.send_keys('左侧树图层重命名')
        sleep(2)
        workbench_page.rename_layer_input.enter()
        self.refresh()
        self.sleep(2)
        self.assertEqual(workbench_page.first_layer.text.strip(), '左侧树图层重命名')