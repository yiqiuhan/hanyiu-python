from selenium import webdriver  
import unittest  
  
class Test(unittest.TestCase):  
  
    def setUp(self) -> None:  
        self.driver = webdriver.Edge()  
        self.driver.get("https://www.baidu.com")  
        self.title = self.driver.title  
        print(self.title)  
  
    def test1(self):  
        self.assertEqual(self.title, "百度一下，你就知道")  
  
    def tearDown(self) -> None:  
        self.driver.quit()  
  
if __name__ == "__main__":  
    unittest.main()