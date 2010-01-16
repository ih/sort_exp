import pyglet
from pyglet.window import key, mouse

window=pyglet.window.Window()
label=pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
image=pyglet.resource.image('Wizard.gif')

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
    if button == mouse.LEFT:
        print 'left'

@window.event
def on_draw():
    window.clear()
#    label.draw()
    image.blit(0,0)

window.push_handlers(pyglet.window.event.WindowEventLogger())

pyglet.app.run()
