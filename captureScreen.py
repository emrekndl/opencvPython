import  numpy as np
from mss import mss

class captureScreen():
    def __init__(self, bBox = {'top': 100, 'left': 10, 'width': 640, 'height': 400}):
         self.boundingBox = bBox

    def read(self):
        sct = mss()
        sct_img = sct.grab(self.boundingBox)
        frame = np.array(sct_img)

        return frame


