import pyglet
from pyglet.window import mouse

window=pyglet.window.Window()
window.push_handlers(pyglet.window.event.WindowEventLogger())


@window.event
def on_mouse_press(x, y, button, modifier):
    if button == mouse.LEFT:
        print("The Left")
    elif button ==mouse.RIGHT:
        print("The Right")
    elif button ==mouse.MIDDLE:
        print("The middle")


@window.event
def on_draw():
    window.clear()


pyglet.app.run()