import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('http://api.github.com/zen')
    print(r.text)
  
@pytest.mark.http
def test_second_request():
    r = requests.get('http://api.github.com/users/defunct')   
    body = r.json()
    headers = r.headers
    
    assert body['followers'] == 43
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'
    

   
