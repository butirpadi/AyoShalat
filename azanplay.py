import pyglet


class AzanPlay(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.azansnd = pyglet.media.load(filepath)

    def stop(self):
        self.player.pause()
        pyglet.app.exit()

    def play(self):
        if self.azansnd.is_queued:
            self.player.seek(0.0)
            self.player.play()
        else:
            self.player = self.azansnd.play()
        
        pyglet.app.run()
