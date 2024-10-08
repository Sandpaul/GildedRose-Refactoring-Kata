# -*- coding: utf-8 -*-

# class ItemUpdater():
#     MIN_QUALITY = 0
#     MAX_QUALITY = 50

#     def decrement_quality(self, item, amount):
#         item.quality -= amount
#         if item.quality < self.MIN_QUALITY:
#             item.quality = self.MIN_QUALITY

#     def increment_quality(self, item, amount):
#         item.quality += amount
#         if item.quality > self.MAX_QUALITY:
#             item.quality = self.MAX_QUALITY

#     def normal_item(self, item):
#         pass

#     def brie(self, item):
#         pass

#     def ragnaros(self, item):
#         pass

#     def backstage_pass(self, item):
#         pass





class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem:
    def __init__(self, item):
        self.item = item

    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def decrement_quality(self, amount):
        self.item.quality -= amount
        if self.item.quality < self.MIN_QUALITY:
            self.item.quality = self.MIN_QUALITY

    def increment_quality(self, amount):
        self.item.quality += amount
        if self.item.quality > self.MAX_QUALITY:
            self.item.quality = self.MAX_QUALITY

    def decrement_sell_in(self):
        self.item.sell_in -= 1
