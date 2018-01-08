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
    def test_01_homePage_customerService_failureReported(self):  # homePage故障上报
        self.driver.element('id', 'cn.xq.shareelb:id/service').click()
        self.driver.wait_for_element('xpath', '//android.view.View/android.view.View[1]'
                                              '/android.view.View[1]/android.widget.ListView[1]'
                                              '/android.view.View[1]').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/bikecode').click()  # 点击输入车辆编号输入框
        time.sleep(1)
        if self.driver.element_if_exists('id', 'com.android.packageinstaller:id/permission_allow_button'):
            self.driver.element('id', 'com.android.packageinstaller:id/permission_allow_button').click()
            time.sleep(1)
        if self.driver.element_if_exists('xpath', '//android.widget.FrameLayout'
                                                  '/android.view.ViewGroup/android.widget.LinearLayout'):
            self.driver.element('xpath', '//android.widget.FrameLayout'
                                         '/android.view.ViewGroup/android.widget.LinearLayout').click()
            time.sleep(1)
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/input').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/code_Num').send_keys('021062372')
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/confirm_code').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/rightBtnStr').click()
        time.sleep(1)
        self.driver.touch('drag', {'fromX': 500, 'fromY': 1632, 'toX': 500, 'toY': 330, 'duration': 0.1})  # 上滑
        self.driver.touch('drag', {'fromX': 500, 'fromY': 1632, 'toX': 500, 'toY': 330, 'duration': 0.1})  # 上滑
        self.driver.touch('drag', {'fromX': 500, 'fromY': 1632, 'toX': 500, 'toY': 330, 'duration': 0.1})  # 上滑
        fault = self.driver.elements('id', 'cn.xq.shareelb:id/faultBox')
        fault[4].click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/fault_desc').send_keys('测试故障上报哦!!!!')
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/commit').click()  # 提交
        time.sleep(1)
        for i in range(10):
            if self.driver.element_if_exists('name', '在线客服'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('name', '在线客服'))
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()

    @testcase
    def test_02_homePage_customerService_applyForParking(self):  # homePage申请停车点
        self.driver.element('id', 'cn.xq.shareelb:id/service').click()
        self.driver.wait_for_element('xpath', '//android.view.View/android.view.View[1]'
                                              '/android.view.View[1]/android.widget.ListView[2]'
                                              '/android.view.View[1]').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/tv_address').click()  # 点击申请位置
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/search_address').send_keys('鹤沙航城地铁站')
        time.sleep(2)
        self.driver.wait_for_element('xpath', '//android.widget.LinearLayout'
                                              '/android.widget.ListView/android.widget.LinearLayout[1]').click()
        # 点击上传图片按钮
        self.driver.wait_for_element('xpath', '//android.support.v7.widget.RecyclerView'
                                              '/android.widget.LinearLayout').click()
        photo1 = self.driver.elements('id', 'cn.xq.shareelb:id/iv_thumb')
        photo1[3].click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/btn_ok').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/btn_submit').click()
        time.sleep(1)
        for i in range(10):
            if self.driver.element_if_exists('name', '在线客服'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('name', '在线客服'))
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()

    @testcase
    def test_03_homePage_customerService_Report(self):  # homePage举报
        self.driver.element('id', 'cn.xq.shareelb:id/service').click()
        self.driver.wait_for_element('xpath', '//android.view.View/android.view.View[1]'
                                              '/android.view.View[1]/android.widget.ListView[1]'
                                              '/android.view.View[2]').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/bikecode').click()  # 点击输入车辆号码
        time.sleep(1)
        if self.driver.element_if_exists('id', 'com.android.packageinstaller:id/permission_allow_button'):
            self.driver.element('id', 'com.android.packageinstaller:id/permission_allow_button').click()
            time.sleep(1)
        if self.driver.element_if_exists('xpath', '//android.widget.FrameLayout'
                                                  '/android.view.ViewGroup/android.widget.LinearLayout'):
            self.driver.element('id', '//android.widget.FrameLayout'
                                      '/android.view.ViewGroup/android.widget.LinearLayout').click()
            time.sleep(1)
        self.driver.element('id', 'cn.xq.shareelb:id/input').click()  # 点击输入编码
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/code_Num').send_keys('021062374')
        self.driver.element('id', 'cn.xq.shareelb:id/confirm_code').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/rightBtnStr').click()
        time.sleep(2)
        self.driver.touch('drag', {'fromX': 500, 'fromY': 1590, 'toX': 500, 'toY': 300, 'duration': 0.1})  # 上滑
        self.driver.touch('drag', {'fromX': 500, 'fromY': 820, 'toX': 500, 'toY': 300, 'duration': 0.1})
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/fault_desc').send_keys('测试我要举报!!!!')  # 输入
        self.driver.wait_for_element('xpath', '//android.widget.RelativeLayout'
                                              '/android.support.v7.widget.RecyclerView'
                                              '/android.widget.LinearLayout').click()
        time.sleep(1)
        photo1 = self.driver.elements('id', 'cn.xq.shareelb:id/iv_thumb')
        photo1[3].click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/btn_ok').click()  # 点击完成
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/commit').click()  # 点击提交
        time.sleep(1)
        for i in range(10):
            if self.driver.element_if_exists('name', '在线客服'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('name', '在线客服'))
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()

    @testcase
    def test_04_homePage_customerService_serviceArea(self):  # homePage服务区域查看
        self.driver.element('id', 'cn.xq.shareelb:id/service').click()
        self.driver.wait_for_element('xpath', '//android.view.View/android.view.View[1]/android.view.View[1]'
                                              '/android.widget.ListView[2]/android.view.View[2]'
                                              '/android.view.View').click()
        time.sleep(2)
        self.driver.touch('drag', {'fromX': 500, 'fromY': 1900, 'toX': 500, 'toY': 105, 'duration': 0.1})  # 上滑
        time.sleep(1)
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/back').click()  # 返回
        time.sleep(1)
        for i in range(10):
            if self.driver.element_if_exists('name', '在线客服'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('name', '在线客服'))
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()

    @testcase
    def test_05_homePage_customerService_useExplanation(self):  # homePage客服中心使用说明
        self.driver.element('id', 'cn.xq.shareelb:id/service').click()
        self.driver.wait_for_element('name', '享骑使用说明').click()
        time.sleep(2)
        self.driver.touch('drag', {'fromX': 500, 'fromY': 1900, 'toX': 500, 'toY': 105, 'duration': 0.1})  # 上滑
        time.sleep(1)
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/back').click()  # 返回
        time.sleep(1)
        for i in range(10):
            if self.driver.element_if_exists('name', '在线客服'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('name', '在线客服'))
        self.driver.element('id', 'cn.xq.shareelb:id/back').click()

    @testcase
    def test_06_homePage_activity(self):  # homePage活动
        self.driver.element('id', 'cn.xq.shareelb:id/gift_fl').click()
        time.sleep(2)
        for i in range(10):
            if self.driver.element_if_exists('xpath', '//android.widget.ListView/android.view.View[2]'):
                self.driver.element('xpath', '//android.widget.ListView/android.view.View[2]').click()
                break
            else:
                time.sleep(1)
        time.sleep(5)
        self.driver.touch('drag', {'fromX': 500, 'fromY': 1900, 'toX': 500, 'toY': 105, 'duration': 0.1})
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/back').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/back').click()
        time.sleep(1)
        for i in range(10):
            if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/rent_car'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/rent_car'))

    @testcase
    def test_07_homePage_findSite(self):  # homePage查找站点
        self.driver.element('id', 'cn.xq.shareelb:id/search_fl').click()
        self.driver.wait_for_element('id', 'cn.xq.shareelb:id/search_address').send_keys('鹤沙航城地铁站')
        time.sleep(1)
        self.driver.wait_for_element('xpath', '//android.widget.LinearLayout/android.widget.ListView'
                                              '/android.widget.LinearLayout[1]').click()
        time.sleep(1)
        for i in range(10):
            if self.driver.element_if_exists('id', 'cn.xq.shareelb:id/rent_car'):
                break
            else:
                time.sleep(1)
        self.assertTrue(self.driver.element_if_exists('id', 'cn.xq.shareelb:id/rent_car'))
        self.driver.element('id', 'cn.xq.shareelb:id/move_now').click()
        time.sleep(1)






