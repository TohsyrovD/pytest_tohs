import pytest

#TUPLE
tuple1 = (1,2,3)
def test_typle_1():
    assert len(tuple1)==3
    assert tuple1 == (1,2,3)

@pytest.mark.parametrize("a,b",[((1,2,3),(1,2,3))])
def test_typle_2(a,b):
    assert a == b


def test_typle_3():
   try:
       assert tuple1[0] == 2
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
