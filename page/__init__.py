"""以下为设置应用 搜索配置信息"""
from selenium.webdriver.common.by import By
# 点击搜索按钮
setting_search_btn = By.ID, "com.android.settings:id/search"
# 输入搜索内容
setting_value = By.ID, "android:id/search_src_text"
# 点击返回
setting_back = By.CLASS_NAME, "android.widget.ImageButton"
