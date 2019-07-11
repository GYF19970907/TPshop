from appium import webdriver
class GetDriver:
    driver = None
    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            desired_caps['appPackage'] = 'com.android.settings'
            desired_caps['appActivity'] = '.Settings'
            # 获取driver
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None

# if __name__ == '__main__':
#     print(GetDriver().get_driver())
#     GetDriver().quit_driver()
#     print(GetDriver().get_driver())