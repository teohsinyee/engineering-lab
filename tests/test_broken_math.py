from src.broken_math import add

def test_addition_should_fail():
    assert add(1, 2) == 99  # failing on purpose
