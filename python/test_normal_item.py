from gilded_rose import NormalItem, BrieItem

def test_normal_item_update():
    test_normal_item = NormalItem("test_normal_item", 5, 5)
    test_normal_item.update()
    assert test_normal_item.get_sell_in() == 4
    assert test_normal_item.get_quality() == 4


def test_normal_item_update_does_not_decrement_quality_past_0():
    test_normal_item = NormalItem("test_item", 1, 0)
    test_normal_item.update()
    assert test_normal_item.get_quality() == 0


def test_normal_item_update_reduces_sell_in_by_1():
    test_normal_item = NormalItem("test_item", 5, 5)
    test_normal_item.update()
    assert test_normal_item.get_sell_in() == 4


def test_brie_item_update_increments_by_1_when_sell_in_greater_than_0():
    test_brie_item = BrieItem("test_brie", 5, 5)
    test_brie_item.update()
    assert test_brie_item.get_quality() == 6


def test_brie_item_update_increments_by_2_when_sell_in_less_than_0():
    test_brie_item = BrieItem("test_brie", -1, 5)
    test_brie_item.update()
    assert test_brie_item.get_quality() == 7


def test_brie_item_update_does_not_increment_quality_above_50():
    test_brie_item = BrieItem("test_brie", -1, 49)
    test_brie_item.update()
    assert test_brie_item.get_quality() == 50
