import price_info as info

def test_total_cost_shopping():
    result = info.total_cost_shopping()
    expected_total = sum(info.price_list[key] * info.quantity_list[key] for key in info.price_list if key in info.quantity_list)
    assert result == expected_total

def test_cost_of_fruits():
    expected_cost = info.price_list['apple'] * 10
    result = info.cost_of_fruits('apple', 10)
    assert result == expected_cost