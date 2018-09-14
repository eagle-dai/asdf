from threading import *
import map
import aircv as ac
import cv2
from ops_util import *
import ops_util
import logging
import os

class FocusThread(Thread):
    def __init__(self, name, *args):
        super(FocusThread, self).__init__(name=name)
        self.data = args

    def run(self):
        while gcf.Gcfg.running:
            time.sleep(3.1415926*3)
            screen.focus_v2()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')


