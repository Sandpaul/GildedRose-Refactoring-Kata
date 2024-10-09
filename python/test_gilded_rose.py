# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose, Conjured


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"


def test_normal_items_reduce_quality_by_one():
    items = [Item("normal_item", 2, 2)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1


def test_normal_items_quality_never_negative():
    items = [Item("normal_item", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_normal_items_quality_reduces_by_two_when_sell_in_is_zero():
    items = [Item("normal_item", 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 8


def test_normal_items_sell_in_decrements_by_one():
    items = [Item("normal_item", 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1


def test_brie_quality_appreciates():
    items = [Item("Aged Brie", 5, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 11


def test_brie_quality_appreciates_by_two_when_sell_in_below_zero():
    items = [Item("Aged Brie", 1, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 11
    gilded_rose.update_quality()
    assert items[0].quality == 13


def test_brie_quality_capped_at_fifty():
    items = [Item("Aged Brie", 1, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


def test_brie_sell_in_deprecates():
    items = [Item("Aged Brie", 1, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 0


def test_sulfuras_quality_always_eighty():
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80


def test_sulfuras_sell_in_does_not_deprecate():
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 0


def test_concert_quality_increments_by_one():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 30, 25)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 26


def test_concert_quality_increments_by_two_when_sell_in_between_ten_and_six():
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 10, 25),
        Item("Backstage passes to a TAFKAL80ETC concert", 6, 25),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 27
    assert items[1].quality == 27


def test_concert_quality_increments_by_three_when_sell_in_between_five_and_one():
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 5, 25),
        Item("Backstage passes to a TAFKAL80ETC concert", 1, 25),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 28
    assert items[1].quality == 28


def test_concert_quality_capped_at_50():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 49)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


def test_concert_quality_resets_to_zero_when_sell_in_reaches_less_than_0():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 25)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_concert_sell_in_deprecates():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 25)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -2


def test_gilded_rose_update_quality_reduces_conjured_quality_by_2_when_sell_in_0_or_greater():
    items = [Item("Conjured item", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 8
