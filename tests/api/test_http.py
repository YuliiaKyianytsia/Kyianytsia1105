import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('http://api.github.com/zen')
    print(r.text)
  
@pytest.mark.http
def test_second_request():
    
    print(f"Response Headers are {headers}")
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers is {r.headers}")

   
