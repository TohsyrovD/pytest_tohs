import pytest

#SET
set1 = {'Michelle', 'Nicholas', 'John', 'Mercy'}
def test_set_1():
    assert len(set1)==4
    assert set1 == {'Michelle', 'Nicholas', 'John', 'Mercy'}

@pytest.mark.parametrize("a,b",[({'Michelle', 'Nicholas', 'John', 'Mercy'},{'Michelle', 'Nicholas', 'John', 'Mercy'})])
def test_set_2(a,b):
    assert a == b


def test_set_3():
   try:
       assert set1[0] == 'Nicholas'
   except AssertionError:
       pass


#DICT
dict1=dict(Ivan="manager", Mark="worker")
def test_dict1():
   assert dict1=={'Mark': 'worker', 'Ivan': 'manager'}

@pytest.mark.parametrize("a,b",[({'Mark': 'worker', 'Ivan': 'manager'},{'Mark': 'worker', 'Ivan': 'manager'})])
def test_dict2(a,b):
    assert a == b

def test_dict3():
   try:
       assert dict1 == 2
   except AssertionError:
       pass
