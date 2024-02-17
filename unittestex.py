import unittest

class Unitdemo(unittest.TestCase):
    def test_login(self):
        print('this is log in defitation')
        self.assertEqual('123',"123", msg = "assert fail")


if __name__ == "__main__":
    unittest.main()
