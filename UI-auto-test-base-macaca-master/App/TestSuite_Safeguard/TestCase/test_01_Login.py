# coding:utf-8

import unittest
import time
from App.PageObject import Boss1
from Public import Devices
from Public.Decorator import testcase
from Public.BasePage import BasePage

account = ['17602119990', '17602119991', '17602119992', '17602118393', '17602119993']

device = Devices.Devices()
devices = device.get_devices()


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage().get_driver()
        cls.index = BasePage().get_index()

    @testcase
    def test_01_install(self):  # 适配机型安装APP
        if devices[self.index]['reuse'] == 1:
            # 三星手机安装
            if self.driver.element_if_exists('id', 'com.android.packageinstaller:id/permission_allow_button'):
                self.driver.wait_for_element('id', 'com.android.packageinstaller:id/permission_allow_button').click()
                self.driver.wait_for_element('id', 'com.android.packageinstaller:id/permission_allow_button').click()
                self.driver.wait_for_element('id', 'com.android.packageinstaller:id/permission_allow_button').click()
            # 大米、魅族、Vivo手机安装
            elif self.driver.element_if_exists('id', 'android:id/button1'):
                self.driver.element('id', 'android:id/button1').click()
                time.sleep(1)
                if self.driver.element_if_exists('id', 'android:id/button1'):
                    self.driver.wait_for_element('id', 'android:id/button1').click()
                    time.sleep(1)
                    if self.driver.element_if_exists('id', 'android:id/button1'):
                        self.driver.wait_for_element('id', 'android:id/button1').click()
            time.sleep(5)
            self.driver.touch('drag', {'fromX': 1000, 'fromY': 960, 'toX': 0, 'toY': 960, 'duration': 0.2})
            self.driver.touch('drag', {'fromX': 1000, 'fromY': 960, 'toX': 0, 'toY': 960, 'duration': 0.2})
            self.driver.touch('drag', {'fromX': 1000, 'fromY': 960, 'toX': 0, 'toY': 960, 'duration': 0.2})
            self.driver.touch('tap', {'x': 539, 'y': 960})
            time.sleep(2)
            if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/iv_del'):
                self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_del').click()
                time.sleep(1)  # 引导页点击
                self.driver.touch('tap', {'x': 560, 'y': 950})
                self.driver.touch('tap', {'x': 560, 'y': 950})
                self.driver.touch('tap', {'x': 560, 'y': 950})
            else:
                self.driver.touch('tap', {'x': 560, 'y': 950})
                self.driver.touch('tap', {'x': 560, 'y': 950})
                self.driver.touch('tap', {'x': 560, 'y': 950})
            time.sleep(1)
            self.driver.wait_for_element('id', 'cn.xq.shareelb:id/move_now').click()
            time.sleep(1)
            if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/guide_site'):
                self.driver.touch('tap', {'x': 560, 'y': 950})
            else:
                self.driver.touch('drag', {'fromX': 900, 'fromY': 960, 'toX': 900, 'toY': 900, 'duration': 0.3})
                time.sleep(1)
                if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/guide_site'):
                    self.driver.touch('tap', {'x': 560, 'y': 950})
                else:
                    self.driver.touch('drag', {'fromX': 900, 'fromY': 960, 'toX': 960, 'toY': 960, 'duration': 0.3})
                    time.sleep(1)
                    if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/guide_site'):
                        self.driver.touch('tap', {'x': 560, 'y': 950})
        elif devices[self.index]['reuse'] == 3:
            if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/cancle_act'):
                self.driver.element('id', 'cn.xq.shareelb:id/cancle_act').click()
                time.sleep(2)
        self.assertTrue(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/rent_car'))

    @testcase
    def test_02_login(self):  # app登录测试
        if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/use_instruction'):
            self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_title_menu').click()
            self.driver.wait_for_element('id', 'cn.xq.shareelb:id/input_phone').send_keys(account[self.index])
            self.driver.element('id', 'cn.xq.shareelb:id/input_code').send_keys('2222')
            code = Boss1.Boss1Test()
            code.setUpClass()
            code.test_get_url()
            code.test_search_boss1_01_login()
            code.test_search_boss1_02_create_yzm(account[self.index])
            code.test_search_boss1_close()
            time.sleep(1)
            self.driver.element('id', 'cn.xq.shareelb:id/login_click').click()
            time.sleep(2)
            for i in range(8):
                if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/rent_car'):
                    break
                else:
                    time.sleep(1)
            self.assertFalse(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/login_click'))
        elif self.driver.element_if_exists('id', 'cn.xq.shareelb:id/cancle_act'):
            self.driver.element('id', 'cn.xq.shareelb:id/cancle_act').click()
            self.assertFalse(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/use_instruction'))
        else:
            self.assertFalse(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/use_instruction'))

    @testcase
    def test_03_quit(self):  # 退出测试
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_title_menu').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/ll_nav_set').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/tv_logout').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/rightBtnStr').click()
        time.sleep(2)
        for i in range(5):
            if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/use_instruction'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/use_instruction'))

    @testcase
    def test_04_carProtocol(self):  # 查看用车协议
        self.driver.element('id', 'cn.xq.shareelb:id/iv_title_menu').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/clase_tv').click()
        time.sleep(2)
        for i in range(10):
            if self.driver.element_if_exists('name', '享骑电单车租赁服务协议'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('name', '享骑电单车租赁服务协议'))
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/back').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/close_rl').click()

    @testcase
    def test_05_errorLogin(self):  # 错误的验证码登录测试
        self.driver.element('id', 'cn.xq.shareelb:id/iv_title_menu').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/input_phone').send_keys('17602119997')
        self.driver.element('id', 'cn.xq.shareelb:id/input_code').send_keys('2222')
        self.driver.element('id', 'cn.xq.shareelb:id/login_click').click()  # 点击登录按钮
        time.sleep(2)
        self.assertTrue(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/login_click'))
        self.driver.element('id', 'cn.xq.shareelb:id/close_rl').click()

    @testcase
    def test_06_login2(self):  # app退出后再次登录
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_title_menu').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/input_phone').send_keys(account[self.index])
        self.driver.element('id', 'cn.xq.shareelb:id/input_code').send_keys('2222')
        code = Boss1.Boss1Test()
        code.setUpClass()
        code.test_get_url()
        code.test_search_boss1_01_login()
        code.test_search_boss1_02_create_yzm(account[self.index])
        code.test_search_boss1_close()
        time.sleep(1)
        self.driver.element('id', 'cn.xq.shareelb:id/login_click').click()  # 点击登录按钮
        time.sleep(2)
        for i in range(8):
            if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/use_instruction'):
                time.sleep(1)
            else:
                break
        self.assertFalse(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/use_instruction'))

