from pyglet.sprite import Sprite
from general import between

class SelectableSprite(Sprite):
    def __init__(self, image, x, y):
        Sprite.__init__(self, image, x, y)
        self.selected=False
        print "derived"
        
    def select(self):
        if self.selected:
            self.selected=False
            self.scale=1
        else:
            self.selected=True
            self.scale=1.1

    def within(self,x,y):
        return between(x, self.x, self.x+self.width) and between(y, self.y, self.y+self.height)


    def draw(self):
        Sprite.draw(self)
        #draw border around the image if selected
#        if self.selected:
#            self.drawBorder()
        print self.selected



    
