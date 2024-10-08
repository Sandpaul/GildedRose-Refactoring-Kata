from gilded_rose import NormalItem

def test_normal_item_update():
    test_normal_item = NormalItem("test_normal_item", 5, 5)
    test_normal_item.update()
    assert test_normal_item.get_sell_in() == 4
    assert test_normal_item.get_quality() == 4


def test_decrement_quality_does_not_decrement_past_0():
    test_normal_item = NormalItem("test_item", 1, 0)
    test_normal_item.update()
    assert test_normal_item.get_quality() == 0


def test_decrement_sell_in_reduces_by_1():
    test_normal_item = NormalItem("test_item", 5, 5)
    test_normal_item.update()
    assert test_normal_item.get_sell_in() == 4
