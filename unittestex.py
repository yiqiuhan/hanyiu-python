import unittest

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

# 创建测试运行器
runner = unittest.TextTestRunner()
runner.run(suite)