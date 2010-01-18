import pyglet
import time
import textinput
from random import randint,shuffle
from itertools import permutations
from selectable import SelectableSprite
from pyglet.sprite import Sprite
from pyglet.window import key, mouse

####uncomment for debugging
#window.push_handlers(pyglet.window.event.WindowEventLogger())

batch=pyglet.graphics.Batch()
display=False
num_stim=10
selected=[]
stim=[]
labels=[]
#maybe make this a shape with random color
image=pyglet.image.load('ball.gif')
window=pyglet.window.Window()
#window=textinput.Window()

#temporary solution for displaying 


#generate the stimulus
for i in range(num_stim):
    #need to add overlap detection?
    x,y=randint(0,window.width-image.width),randint(0,window.height-image.height)
    stim.append(SelectableSprite(image,x,y,batch=batch))
    #generate labels for stimuli
    labels.append(pyglet.text.Label(str(i), font_name='Times New Roman', font_size=36, x=x, y=y, anchor_x='center', anchor_y='center', batch=batch))

#assign an order to the stimuli
stim_order=range(num_stim)
shuffle(stim_order)

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
        for ss in stim:
            if ss.within(x,y):
                ss.select()



@window.event
def on_draw():
    global display
    if display:
        time.sleep(3)
        display=False
    window.clear()
#    label.draw()

    batch.draw()

    #add pause?
    #if two things are selected display the comparison of the two 
    [selected.append(s) for s in stim if s.selected and not s in selected]
    print stim_order
    if len(selected)==2:
        pyglet.text.Label(compare(), font_name='Times New Roman', font_size=36, x=10, y=10).draw()
        [s.select() for s in selected]
        display=True

    del selected[:]


def compare():
    """compares items in selected and returns a string 'a<b' """
    i1=stim.index(selected[0])
    i2=stim.index(selected[1])
    if stim_order.index(i1) < stim_order.index(i2):
        return str(i1)+"<"+str(i2)
    else:
        return str(i2)+"<"+str(i1)

pyglet.app.run()
