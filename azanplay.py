import pyglet

class AzanPlay(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.azansnd = pyglet.media.load(filepath)

    def stop(self):
        self.player.delete()
        pyglet.app.exit()

    def play(self):
        print('playing')
        media = pyglet.media.load(self.filepath)

        try:
            if self.player :
                print('stoping current player')
                self.player.delete()
                pyglet.app.exit()
        except AttributeError as e:
            print(e)
        
        self.player = pyglet.media.Player() 
        self.player.queue(media) 
        self.player.play()
        pyglet.app.run() 

