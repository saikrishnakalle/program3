from app import add

def test_add_positive_numbers():
    assert add(10, 5) == 15

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5
