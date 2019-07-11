from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找 方法
    def base_find(self,loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击 方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入 方法
    def base_input(self, loc, value):
        el=self.base_find(loc)
        el.clear()
        el.send_keys(value)