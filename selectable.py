from pyglet.sprite import Sprite
from pyglet.window import key, mouse
from general import between

class SelectableSprite(Sprite):
    def __init__(self, image, x, y, batch=None, label=None):
        Sprite.__init__(self, image, x, y, batch=batch)
        self.selected=False
        self.label=label


        print "derived"
        
    def select(self):
        if self.selected:
            self.selected=False
            self.scale=1
        else:
            self.selected=True
            self.scale=2

    def within(self,x,y):
        return between(x, self.x, self.x+self.width) and between(y, self.y, self.y+self.height)

    def on_mouse_press(self,x,y,button,modifiers):
#if press is in unselected image;  select it
#if press is in selected image; unselect it
#if two images selected compare objects; unselect objects
        if button == mouse.LEFT:
            if self.within(x,y):
                self.select()
                
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            if self.within(x,y) and self.selected:
                self.x=x-self.width/2
                self.y=y-self.height/2
                self.label.x=x
                self.label.y=y

    def draw(self):
        Sprite.draw(self)
        self.label.draw()
        #draw border around the image if selected
#        if self.selected:
#            self.drawBorder()
#        print self.selected



    
