import pyglet

window=pyglet.window.Window()

image=pyglet.resource.image('source/imgOne.jpg')

@window.event
def on_draw():
    window.clear()
    image.blit(50,50)


pyglet.app.run()