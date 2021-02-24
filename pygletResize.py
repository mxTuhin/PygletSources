import pyglet
from pyglet import window

window=pyglet.window.Window(1280, 720,
                            "Halum..",
                            resizable=True,
                            style=window.Window.WINDOW_STYLE_BORDERLESS)

window.set_minimum_size(400, 400)
icon=pyglet.image.load('source/icon.png')
window.set_icon(icon)


@window.event
def on_draw():
    window.clear()

pyglet.app.run()