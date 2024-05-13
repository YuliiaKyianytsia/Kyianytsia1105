import pytest


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Sergii"
        self.second_name = "Butenko"

    def remove(self):
        self.name = ""
        self.second_name = ""

@pytet_fixture
def user():
    user = User()
    user.create()

    yeld user
    
def test_change_name():
    assert user.name == 'Sergii'  

def test_change_second_name():
    assert user.second_name == 'Butenko' 
    
