import pyglet

music = pyglet.resource.media('source/mpThree.mp3', streaming=False)
music.play()

pyglet.app.run()