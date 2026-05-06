from app import add

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
