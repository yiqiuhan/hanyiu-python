import requests
import pytest
def access_token():
    URL = "https://api.weixin.qq.com/cgi-bin/stable_token?"
    rep = requests.get(URL)
    assert 200 ==rep.status_code

if __name__ == "main":
    pytest.main()