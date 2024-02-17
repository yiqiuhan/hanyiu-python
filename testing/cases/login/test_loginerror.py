import pytest
def setup_module():
    print('\n*初始化模块*') 

def teardown_module():
    print('\n*清除模块*') 

class Test_errorpw():
    @pytest.mark.webtest
    def test_c001001(self):
        print('\ncaseC001001')
        assert 1 == 1
    def test_c001002(self):
        print('\ncaseC001002')
        assert 2 == 2
    def test_c001003(self):
        print('\ncaseC001003')
        assert 3 == 2



#a = test_errorpw()
#a.test_c001001()
