class GildedRose:

    def __init__(self, items):
        self.items = items
      
    
    def update_quality(self):
        for item in self.items:
            item.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def _increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
            
    def _decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1
            
    def _pre_action(self):
        self._decrease_quality()
        
    def _sell_in_update(self):
        self.sell_in = self.sell_in - 1
    
    def _post_action(self):
        if self.sell_in < 0:
            self._decrease_quality()
    
    def update(self):
        self._pre_action()
        
        self._sell_in_update()
            
        self._post_action()
    
class AgedBrie(Item):
    def _pre_action(self):
        self._increase_quality()
        
    def _post_action(self):
        if self.sell_in < 0:
            self._increase_quality()
                
class BackstagePassesToATAFKAL80ETCConcert(Item):
    def _pre_action(self):
        self._increase_quality()
        
        if self.quality < 50:
            if self.sell_in < 11:
                self._increase_quality()
            if self.sell_in < 6:
                self._increase_quality()
    
    def _post_action(self):
        if self.sell_in < 0:
            self.quality = 0
        
class SulfurasHandOfRagnaros(Item):
    def _pre_action(self):
        pass
    
    def _post_action(self):
        pass
            
    def _sell_in_update(self):
        pass
