import pyglet
import os

class AzanPlay(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.azansnd = pyglet.media.load(filepath)

    def stop(self):
        self.player.pause()
        pyglet.app.exit()

    def play(self):
        if os.name == "nt" :
            self.player = self.azansnd.play()
            
            try:
                pyglet.app.run()
            except RuntimeError:
                print('error')
        else:
            if self.azansnd.is_queued:
                self.player.seek(0.0)
                self.player.play()
            else:
                self.player = self.azansnd.play()
            
            pyglet.app.run()
