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

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'Github.com'

    @pytest.mark.http
    def test_status_code_request():
        r = requests.get('http://api.github.com/users/sergii_butenko')
        assert r.status_code == 404

   
