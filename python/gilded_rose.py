# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        converted_items = []
        for item in self.items:
            if item.name == "Aged Brie":
                converted_items.append(BrieItem(item=item))
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                converted_items.append(BackstagePassItem(item=item))
            elif item.name == "Sulfuras, Hand of Ragnaros":
                converted_items.append(Sulfuras(item=item))
            else:
                converted_items.append(NormalItem(item=item))

        for item in converted_items:
            item.update()

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1 # this reduces sell_in for all apart from sulfuras
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else: # if item.name is "Aged Brie"
                    if item.quality < 50:
                        item.quality = item.quality + 1

        for original_item, converted_item in zip(self.items, converted_items):
            original_item.sell_in = converted_item.sell_in
            original_item.quality = converted_item.quality


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


class BrieItem(NormalItem):
    def update(self):
        increment_amount = 2 if self.get_sell_in() < 0 else 1
        self.increment_quality(increment_amount)


class BackstagePassItem(NormalItem):
    def update(self):
        increment_amount = 0
        if self.get_sell_in() < 0:
            self.decrement_quality(self.get_quality())
        elif self.get_sell_in() < 6:
            increment_amount = 3
        elif self.get_sell_in() < 11:
            increment_amount = 2
        else:
            increment_amount = 1
        self.increment_quality(increment_amount)


class Sulfuras(NormalItem):
    MIN_QUALITY = 80
    MAX_QUALITY = 80

    def update(self):
        pass
