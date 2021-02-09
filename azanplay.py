from gi.repository import Gst
from ctypes import c_buffer
from random import random
from time import sleep
from sys import getfilesystemencoding

from playsound import PlaysoundException
import os
gi.require_version('Gst', '1.0')
import gi
from pprint import pprint


class AzanPlay(object):

    def __init__(self):
        Gst.init(None)
        self._playbin = Gst.ElementFactory.make('playbin', 'playbin')
        print('inside init ')

    def stop(self):
        # del self._playbin
        self._playbin.set_state(Gst.State.NULL)

    def play(self, sound):
        try:
            from urllib.request import pathname2url
        except ImportError:
            # python 2
            from urllib import pathname2url

        if sound.startswith(('http://', 'https://')):
            self._playbin.props.uri = sound
        else:
            self._playbin.props.uri = 'file://' + \
                pathname2url(os.path.abspath(sound))

        set_result = self._playbin.set_state(Gst.State.PLAYING)
        if set_result != Gst.StateChangeReturn.ASYNC:
            raise PlaysoundException(
                "self._playbin.set_state returned " + repr(set_result))

        # FIXME: use some other bus method than poll() with block=False
        # https://lazka.github.io/pgi-docs/#Gst-1.0/classes/Bus.html
        bus = self._playbin.get_bus()
        bus.poll(Gst.MessageType.EOS, Gst.CLOCK_TIME_NONE)
        self._playbin.set_state(Gst.State.NULL)
