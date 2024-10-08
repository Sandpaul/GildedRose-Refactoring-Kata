# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        non_depreciating_items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]

        transformed_items = []

        for item in self.items:
            item = NormalItem(item)
            transformed_items.append(item)

        for item in transformed_items:
            if item.item.name not in non_depreciating_items:
                if item.item.quality > 0:
                    item.item.quality = item.item.quality - 1

            else:
                if item.item.quality < 50:
                    item.item.quality = item.item.quality + 1
                    if item.item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.item.sell_in < 11:
                            if item.item.quality < 50:
                                item.item.quality = item.item.quality + 1
                        if item.item.sell_in < 6:
                            if item.item.quality < 50:
                                item.item.quality = item.item.quality + 1
            if item.item.name != "Sulfuras, Hand of Ragnaros":
                item.item.sell_in = item.item.sell_in - 1
            if item.item.sell_in < 0:
                if item.item.name != "Aged Brie":
                    if item.item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.item.quality > 0:
                            if item.item.name != "Sulfuras, Hand of Ragnaros":
                                item.item.quality = item.item.quality - 1
                    else:
                        item.item.quality = item.item.quality - item.item.quality
                else:
                    if item.item.quality < 50:
                        item.item.quality = item.item.quality + 1


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

    def update(self):
        self.decrement_quality(1)
        self.decrement_sell_in()
