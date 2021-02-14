from ctypes import c_buffer
from random import random
from time import sleep
from sys import getfilesystemencoding

from pprint import pprint
import pyglet


class AzanPlay(object):

    def __init__(self,filepath):
        self.filepath = filepath 
        self.azansnd = pyglet.media.load(filepath)

    def stop(self):
        pyglet.app.exit()

    def play(self):
        
        self.azansnd.play()
        pyglet.app.run()
