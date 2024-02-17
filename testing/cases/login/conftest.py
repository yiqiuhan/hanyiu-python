# conftest.py  
  
import pytest  
  
@pytest.fixture(scope="package",autouse=True)
def st_emptyEnv():  
    print(f'\n***初始化项目甲')
    yield
    print(f'\n***清除项目甲')