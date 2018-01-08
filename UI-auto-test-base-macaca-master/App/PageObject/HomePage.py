from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps


class HomePage(BasePage):
    @teststep
    def wait_page(self, timeout=10000):
        """以“我要用车”的ID为依据"""
        try:
            self.driver.wait_for_element_by_id('cn.xq.shareelb:id/rent_car', timeout=timeout)
            return True
        except WebDriverException:
            return False