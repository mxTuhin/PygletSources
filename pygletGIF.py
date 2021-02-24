import pyglet
from time import sleep

animation=pyglet.image.load_animation('eye1.gif')
animSprite=pyglet.sprite.Sprite(animation)

w=animSprite.width
h=animSprite.height

window=pyglet.window.Window(width=w, height=h)

r,g,b,alpha=0.5,0.5,0.8,0.5

pyglet.gl.glClearColor(r,g,b,alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()
    # window.flip()

@window.event
def on_close():
    print("I'm closing now") #<- this never happens



pyglet.app.run()