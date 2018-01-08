# coding:utf-8

import unittest
import time
from macaca import WebDriver
from macaca import WebDriverException


desired_caps = {
    'platformName': 'desktop',
    'browserName': 'chrome'
}
server_url = {
    'hostname': 'localhost',
    'port': 3456
}


class Boss1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_url(self):
        # test
        self.driver.get('http://www.t.xqcx.com/xqboss/boss/user/login;jsessionid=C52CE69C4EA6FD01653142A0A56533AD')
        # online
        # self.driver.get('http://www.xqchuxing.com/xqboss/boss/user/login;jsessionid=069EAC3EC1467801EE6388943FEF612F')

    def test_search_boss1_01_login(self):
        try:
            self.driver.maximize_window()
            time.sleep(1)
            # test
            self.driver.element('id', 'mobile').send_keys('18888888888')
            # online
            # self.driver.element('id', 'mobile').send_keys('13764545612')
            self.driver.element('id', 'password').send_keys('123456789')
            self.driver.element('id', 'btn_login').click()
            time.sleep(2)
            self.assertEqual(self.driver.title, u'享骑出行')
        except WebDriverException:
            print("Error: boss1登录错误")

    def test_search_boss1_02_create_yzm(self, account):
        try:
            self.driver.element('xpath', '/html/body/div/aside[1]/section/ul/li[2]/a').click()
            time.sleep(1)
            self.driver.element('xpath', '//*[@id="yanzmshengc"]/a').click()
            time.sleep(2)
            self.driver.element('xpath', '//*[@id="telphone"]').send_keys(account)
            self.driver.element('xpath', '//*[@id="code"]').send_keys('2222')
            self.driver.element('xpath', '//*[@id="btn_update"]').click()
            time.sleep(1)
            self.driver.wait_for_element('xpath', 'html/body/div[1]/div[2]/div/div[2]').click()
        except WebDriverException:
            print("Error: boss1生成验证码错误")

    def test_search_boss1_03_mandatory_car(self):
        try:
            self.driver.wait_for_element('xpath', 'html/body/div[1]/aside[1]/section/ul/li[3]/a').click()
            self.driver.wait_for_element('xpath', './/*[@id="dingdanchaxun"]/a').click()
            self.driver.wait_for_element('xpath', './/*[@id="inputUserMobile"]').send_keys('17602118393')
            self.driver.element('xpath', './/*[@id="searchBtn"]').click()
            time.sleep(2)
            self.driver.wait_for_element('xpath', './/*[@id="example1"]/tbody/tr/td[9]/a[2]').click()
            time.sleep(1)
            js = "var q=document.body.scrollTop=100000"
            self.driver.execute_script(js)
            time.sleep(2)
            self.driver.wait_for_element('xpath', './/*[@id="ui-id-2"]').click()
            self.driver.wait_for_element('xpath', './/*[@id="txta_desc2"]').send_keys('测试强制还车！！')
            self.driver.element('xpath', './/*[@id="trailer-sure"]').click()
            time.sleep(5)
            if self.driver.element_if_exists('xpath', 'html/body/div[1]/div[3]/div/div[2]'):
                self.driver.element('xpath', 'html/body/div[1]/div[3]/div/div[2]').click()
            else:
                print("Boss1强制还车失败")
        except WebDriverException:
            print("Error: boss1生成验证码错误")

    def test_search_boss1_close(self):
        self.driver.close()

    def runTest(self):
        pass


if __name__ == '__main__':
    unittest.main()
