# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose, NormalItem


# @pytest.fixture
# def item_updater():
#     return ItemUpdater()


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


def test_sulfuras_quality_always_eighty():
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80

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
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_decrement_quality_decrements_by_passed_amount():
    test_item = Item("test_item", 5, 5)
    test_normal_item = NormalItem(test_item)
    test_normal_item.decrement_quality(1)
    assert test_normal_item.item.quality == 4
    test_normal_item.decrement_quality(2)
    assert test_normal_item.item.quality == 2


def test_decrement_quality_does_not_decrement_past_0():
    test_item = Item("test_item", 1, 0)
    test_normal_item = NormalItem(test_item)
    test_normal_item.decrement_quality(1)
    assert test_normal_item.item.quality == 0


def test_increment_quality_increments_by_passed_amount():
    test_item = Item("test_item", 1, 0)
    test_normal_item = NormalItem(test_item)
    test_normal_item.increment_quality(1)
    assert test_normal_item.item.quality == 1
    test_normal_item.increment_quality(2)
    assert test_normal_item.item.quality == 3


def test_increment_quality_caps_at_50():
    test_item = Item("test_item", 1, 49)
    test_normal_item = NormalItem(test_item)
    test_normal_item.increment_quality(3)
    assert test_normal_item.item.quality == 50
