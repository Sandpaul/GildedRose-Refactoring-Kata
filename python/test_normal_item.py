from gilded_rose import NormalItem, BrieItem, BackstagePassItem, Sulfuras

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


def test_backstage_pass_quality_increments_by_1_when_sell_in_above_10():
    test_backstage_pass_item = BackstagePassItem("test_item", 11, 2)
    test_backstage_pass_item.update()
    assert test_backstage_pass_item.get_quality() == 3


def test_backstage_pass_quality_increments_by_2_when_sell_in_between_10_and_6():
    test_backstage_pass_item = BackstagePassItem("test_item", 10, 2)
    test_backstage_pass_item_2 = BackstagePassItem("test_item", 6, 2)

    test_backstage_pass_item.update()
    test_backstage_pass_item_2.update()

    assert test_backstage_pass_item.get_quality() == 4
    assert test_backstage_pass_item_2.get_quality() == 4


def test_backstage_pass_quality_increments_by_3_when_sell_in_between_5_and_1():
    test_backstage_pass_item = BackstagePassItem("test_item", 5, 2)
    test_backstage_pass_item_2 = BackstagePassItem("test_item", 1, 2)

    test_backstage_pass_item.update()
    test_backstage_pass_item_2.update()

    assert test_backstage_pass_item.get_quality() == 5
    assert test_backstage_pass_item_2.get_quality() == 5


def test_backstage_pass_quality_capped_at_50():
    test_backstage_pass_item = BackstagePassItem("test_item", 5, 49)
    test_backstage_pass_item.update()
    assert test_backstage_pass_item.get_quality() == 50


def test_backstageg_pass_quality_resets_to_0_when_sell_in_is_less_than_0():
    test_backstage_pass_item = BackstagePassItem("test_item", -1, 50)
    test_backstage_pass_item.update()
    assert test_backstage_pass_item.get_quality() == 0


def test_sulfuras_item_quality_always_80():
    test_sulfuras = Sulfuras("test_item", 0, 80)
    test_sulfuras.update()
    assert test_sulfuras.get_quality() == 80
