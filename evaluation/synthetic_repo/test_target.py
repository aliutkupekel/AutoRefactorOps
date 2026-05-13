import pytest
from target_smelly import get_discount

def test_regular_customer():
    assert get_discount("regular", 0) == 0
    assert get_discount("regular", 2) == 5
    assert get_discount("regular", 5) == 10

def test_premium_customer():
    assert get_discount("premium", 0) == 10
    assert get_discount("premium", 2) == 15
    assert get_discount("premium", 5) == 20

def test_vip_customer():
    assert get_discount("vip", 0) == 20
    assert get_discount("vip", 2) == 25
    assert get_discount("vip", 5) == 30

def test_unknown_customer():
    assert get_discount("unknown", 5) == 0