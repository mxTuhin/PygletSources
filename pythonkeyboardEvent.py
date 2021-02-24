import pyglet
from pyglet.window import key



window=pyglet.window.Window()

label = pyglet.text.Label()
player= pyglet.media.Player()
music = pyglet.resource.media('source/mpThree.mp3', streaming=False)
player.queue(music)


@window.event
def on_key_press(symbol, modifiers):
    if symbol== key.A:
        print("A Key was Pressed")
        label = pyglet.text.Label("Hello Pyglet Application", font_name='Times New Roman',
                                  font_size=40,
                                  x=window.width / 2,
                                  y=window.height / 2,
                                  anchor_x='center',
                                  anchor_y='center')
        player.pause()
        window.clear()
        label.draw()
        player.play()
    elif symbol== key.B:
        print("B Key was pressed")
        label = pyglet.text.Label("Hello Pyglet 2 Application", font_name='Times New Roman',
                                  font_size=40,
                                  x=window.width / 2,
                                  y=window.height / 2,
                                  anchor_x='center',
                                  anchor_y='center')
        player.pause()
        window.clear()
        label.draw()
        music.play()
    elif symbol == key.ENTER:
        print("Enter Key was Pressed")
        label = pyglet.text.Label("Hello Pyglet 3 Application", font_name='Times New Roman',
                                  font_size=40,
                                  x=window.width / 2,
                                  y=window.height / 2,
                                  anchor_x='center',
                                  anchor_y='center')
        window.clear()
        label.draw()
        player.play()


pyglet.app.run()