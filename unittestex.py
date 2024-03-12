import unittest  
import os
from HTMLTestRunner import HTMLTestRunner  # 导入HTMLTestRunner  
  
class TestMath(unittest.TestCase):  
    # 测试用例  
    def test_add(self):  
        self.assertEqual(1 + 1, 2)  
  
    def test_subtract(self):  
        self.assertEqual(3 - 2, 1)  
  
# 创建测试套件  
suite = unittest.TestSuite()  
suite.addTest(TestMath('test_add'))  
suite.addTest(TestMath('test_subtract'))  
  
# 指定输出文件夹  
output_folder = 'output'  

# 确保输出文件夹存在  
if not os.path.exists(output_folder):  
    os.makedirs(output_folder)  

# 指定测试报告存放的完整路径  
output_file = os.path.join(output_folder, 'test_report.html') 
  
# 创建测试运行器并指定输出格式  
with open(output_file, 'wb') as f:  
    runner = HTMLTestRunner(stream=f,  
                             title='Math Function Test Report',  
                             description='Test cases for math functions',  
                             verbosity=2)  
    # 运行测试套件  
    runner.run(suite)  
  
print(f"Test report generated in {output_file}")