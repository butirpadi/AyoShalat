import multiprocessing
from playsound import playsound

class AzanPlay(object):
    def __init__(self, filepath):
        self.filepath = filepath
        # self.azansnd = pyglet.media.load(filepath)
        self.player = multiprocessing.Process(target=playsound, args=(filepath,))

    def stop(self):
        # using playsound
        self.player.terminate()

    def play(self):
        #using playsound
        self.player.start()

