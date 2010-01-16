import pyglet
import random
from selectable import SelectableSprite
from pyglet.sprite import Sprite
from pyglet.window import key, mouse

####uncomment for debugging
#window.push_handlers(pyglet.window.event.WindowEventLogger())

window=pyglet.window.Window()
label=pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
image=pyglet.image.load('Wizard.gif')
sprite=Sprite(image,60, 60)
ss=SelectableSprite(image,60,60)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print 'A key was pressed'
    elif symbol == key.LEFT:
        print 'left'
    elif symbol == key.ENTER:
        print 'the enter key'

@window.event
def on_mouse_press(x,y,button,modifiers):
#if press is in unselected image;  select it
#if press is in selected image; unselect it
#if two images selected compare objects; unselect objects
    if button == mouse.LEFT:
        if ss.within(x,y):
            print "selected"
            ss.select()



@window.event
def on_draw():
    window.clear()
#    label.draw()
#    sprite.draw()
    ss.draw()
#    image.blit(random.randint(0,200),random.randint(0,200))



pyglet.app.run()
