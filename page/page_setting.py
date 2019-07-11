import page
from base.base import Base


class PageSetting(Base):
    # 点击搜索按钮
    def page_click_search(self):
        self.base_click(page.setting_search_btn)

    # 输入内容
    def page_input_value(self, value):
        self.base_input(page.setting_value, value)

    # 点击返回
    def page_click_back(self):
        self.base_click(page.setting_back)

    # 组合业务方法
    def page_setting(self, value):
        self.page_click_search()
        self.page_input_value(value)
        self.page_click_back()