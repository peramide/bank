import pytest
from bank import cost

def main():
    test_cost()


def test_cost():
    assert cost("hello") == 0
    assert cost("h") == 20
    assert cost("abc") == 100

if __name__ == "__main__":
    main()