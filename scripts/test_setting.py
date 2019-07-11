import sys
import os
sys.path.append(os.getcwd())

from page.page_setting import PageSetting
from tool.get_driver import GetDriver


class TestSetting():
    # 初始化
    def setup(self):
        self.driver = GetDriver().get_driver()
        # 获取PageSetting对象
        self.setting = PageSetting(self.driver)

    # 结束
    def teardown(self):
        # 错误写法，千万不能直接关闭，因为driver获取的时候使用时单例模式，而关闭必须置空操作
        # 默认这种关闭方法没有置空操作
        # self.driver.quit()
        # 正确方式
        self.setting.driver.quit()

    # 测试方法
    def test_setting(self,value="123"):
        self.setting.page_setting(value)