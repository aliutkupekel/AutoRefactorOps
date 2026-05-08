import pytest
from target_smelly import calculate_discounted_prices

def test_gold_customer_discounts():
    items = [
        {"type": "electronics", "price": 100},
        {"type": "clothing", "price": 100},
        {"type": "groceries", "price": 100}
    ]
    result = calculate_discounted_prices(items, "GOLD")
    assert result == [80.0, 85.0, 90.0], "Semantic Drift: GOLD tier discount logic altered!"

def test_silver_customer_discounts():
    items = [
        {"type": "electronics", "price": 100},
        {"type": "clothing", "price": 100},
        {"type": "groceries", "price": 100}
    ]
    result = calculate_discounted_prices(items, "SILVER")
    assert result == [90.0, 95.0, 98.0], "Semantic Drift: SILVER tier discount logic altered!"

def test_standard_customer_discounts():
    items = [
        {"type": "electronics", "price": 100},
        {"type": "clothing", "price": 100},
        {"type": "groceries", "price": 100}
    ]
    result = calculate_discounted_prices(items, "STANDARD")
    assert result == [100.0, 100.0, 100.0], "Semantic Drift: STANDARD tier logic altered!"

def test_empty_or_none_cart():
    assert calculate_discounted_prices([], "GOLD") == [], "Semantic Drift: Empty list logic failed!"
    assert calculate_discounted_prices(None, "GOLD") == [], "Semantic Drift: None-type logic failed!"