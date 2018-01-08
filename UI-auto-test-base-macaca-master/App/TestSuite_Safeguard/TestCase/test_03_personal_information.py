# coding:utf-8

import unittest
import time
from Public.Decorator import testcase
from Public.BasePage import BasePage


class HomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BasePage().get_driver()

    @testcase
    def test_01_replaceAvatar(self):  # 更换头像
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_title_menu').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_avatar').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/user_head').click()
        time.sleep(2)
        photo = self.driver.elements('id', 'cn.xq.shareelb:id/iv_thumb')
        photo[3].click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/btn_ok').click()
        time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/iv_avatar'))
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()
        self.driver.back()

    @testcase
    def test_02_replacePhone(self):
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_title_menu').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/iv_avatar').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/user_phone').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/bun_amend_phone').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/et_verify_num').send_keys('2222')
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/btn_verify').click()
        time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/btn_verify'))
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()
        self.driver.back()









