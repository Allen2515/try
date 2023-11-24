from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建Chrome浏览器实例
driver = webdriver.Chrome()

# 打开Google网站
driver.get("https://www.google.com/")

# 通过name属性查找搜索框
search_box = driver.find_element("name", "q")

# 在搜索框中输入查询词
search_box.send_keys("rickroll")

# 提交表单（按Enter键）
search_box.send_keys(Keys.RETURN)

# 等待几秒钟以查看搜索结果
time.sleep(5)

# 打印当前页面的标题
print("页面标题:", driver.title)

# 关闭浏览器窗口
driver.quit()

