# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        wrapped_items = [NormalItem(item=item) for item in self.items]

        non_depreciating_items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]

        for item in wrapped_items:
            if item.name not in non_depreciating_items:
                item.update()

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
        
        for original_item, wrapped_item in zip(self.items, wrapped_items):
            original_item.sell_in = wrapped_item.sell_in
            original_item.quality = wrapped_item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem:
    def __init__(self, name=None, sell_in=None, quality=None, item=None):
        if item:
            self.name = item.name
            self.sell_in = item.sell_in
            self.quality = item.quality
        else:
            self.name = name
            self.sell_in = sell_in
            self.quality = quality

    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def decrement_quality(self, amount):
        self.quality -= amount
        if self.quality < self.MIN_QUALITY:
            self.quality = self.MIN_QUALITY

    def increment_quality(self, amount):
        self.quality += amount
        if self.quality > self.MAX_QUALITY:
            self.quality = self.MAX_QUALITY

    def decrement_sell_in(self):
        self.sell_in -= 1

    def update(self):
        self.decrement_quality(1)
        self.decrement_sell_in()
    
    def get_sell_in(self):
        return self.sell_in
    
    def get_quality(self):
        return self.quality
