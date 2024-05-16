import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = request.get('http://api.github.com/zen')
    print(r.text)
  
