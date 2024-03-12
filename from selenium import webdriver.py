from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
import time  
  
# 创建Edge浏览器驱动  
driver = webdriver.Edge()  
  
# 访问51job主页  
driver.get("https://we.51job.com/pc/search")  
  
# 等待页面加载完成，这里使用隐式等待  
driver.implicitly_wait(10)  # 等待10秒，直到元素加载完成  
  
# 定位到搜索框并输入关键词  
search_box = driver.find_element(By.ID, "keywordInput")  # 假设搜索框的ID是"job_query_key"  
search_box.send_keys("软件测试")  
  
# 定位到工作地点并输入上海  
#location_box = driver.find_element(By.ID, "work_place")  # 假设工作地点输入框的ID是"work_place"  
#location_box.send_keys("上海")  
  
# 点击搜索按钮  
#search_button = driver.find_element(By.CSS_SELECTOR, ".search_btn")  # 使用CSS选择器定位搜索按钮  
#search_button.click()  
  
# 等待搜索结果加载完成  
time.sleep(100)  # 等待2秒，这里简单使用sleep，但更好的做法是使用WebDriverWait  
  
# 现在你可以在浏览器中看到上海的软件测试岗位搜索结果了  
# 如果你想进一步操作，比如获取搜索结果中的某个元素，你可以继续编写代码  
  
# 关闭浏览器  
driver.quit()