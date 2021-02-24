import pyglet

window=pyglet.window.Window()

label=pyglet.text.Label("Hello Pyglet Application", font_name='Times New Roman',
                        font_size=40,
                        x=window.width/2,
                        y=window.height/2,
                        anchor_x='center',
                        anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()



pyglet.app.run()