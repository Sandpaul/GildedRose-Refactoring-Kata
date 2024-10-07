# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


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

# - Brie:
# -- While sell_in > 0, quality + 1
# -- While sell_in <= 0, quality + 2
# -- Quality caps at 50

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

# - Concert:
# -- Goes up by one each day
# -- Unless sell_in < 10, goes up by 2
# -- Unless sell in < 5, goes up by 3
# -- Capped at 50
# -- Goes to zero when sell_in <= 0



        
if __name__ == '__main__':
    unittest.main()
