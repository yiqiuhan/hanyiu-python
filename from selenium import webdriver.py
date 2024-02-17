from selenium import webdriver  
import unittest  
  
class TestBaiduTitle(unittest.TestCase):  
      
    def setUp(self) -> None:  
        self.driver = webdriver.Edge()  # 或者使用 Chrome，取决于你的浏览器  
        self.driver.get("https://www.baidu.com") 
        self.title = self.driver.title
        print(self.title) 
      
    def test_baidu_title(self):  
        expected_title = "百度一下，你就知道"  
        actual_title = self.driver.title  
        self.assertEqual(actual_title, expected_title)  
      
    def tearDown(self) -> None:  
        self.driver.quit()  
  
if __name__ == "__main__":  
    unittest.main()