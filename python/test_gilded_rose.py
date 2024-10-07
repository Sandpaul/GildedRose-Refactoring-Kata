# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
# Tests:
# - Normal items:
# -- Sell_in and quantity decrease by 1
# -- Quality doesnt go below 0
# -- Quality goes down by two when sell_in < 0

# - Brie:
# -- While sell_in > 0, quality + 1
# -- While sell_in <= 0, quality + 2
# -- Quality caps at 50

# - Sulfuras:
# -- Quality always at 80

# - Concert:
# -- Goes up by one each day
# -- Unless sell_in < 10, goes up by 2
# -- Unless sell in < 5, goes up by 3
# -- Capped at 50
# -- Goes to zero when sell_in <= 0



        
if __name__ == '__main__':
    unittest.main()
