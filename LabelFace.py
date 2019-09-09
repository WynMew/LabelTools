import numpy as np
import cv2
import os
import os.path as osp
import matplotlib.pyplot as plt
import sys
import time

class click(object):
    def __init__(self):
        self.ax = plt.gca()
        self.LandMarks = []
        self.x = None
        self.y = None
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('key_press_event', self.key_pressC)
    def on_press(self, event):
        self.x = event.xdata
        self.y = event.ydata
        print('press',self.x,self.y)
        #plt.plot(event.xdata, event.ydata, ',')
        tmpp, = plt.plot(event.xdata, event.ydata, 'ro')

        self.LandMarks.append([self.x,self.y])
        self.ax.figure.canvas.draw()
        #time.sleep(1)
        tmpp.remove()
    def key_pressC(self,event):
        print('key press:',event.key)
        sys.stdout.flush()
        if event.key =='c':
            try:
                print('Delete', self.LandMarks[-1])
                self.LandMarks.pop()
                print(len(self.LandMarks), self.LandMarks)
            except:
                print('Delete error')


def add(x, logfile):
    with open(logfile,"a+") as outfile:
        outfile.write(x + "\n")

photolist = '/home/wynmew/data/downloads/danbooru2018/faceDetList'
log = 'faceDetLandmarks'


idx=[]
for line in open(osp.join(photolist)):
    idx.append((os.path.join(line.strip())))

for i in range(210000,len(idx)):
    #i=0
    img = idx[i]
    print(i, img)
    ims = cv2.cvtColor(cv2.imread(img), cv2.COLOR_RGB2BGR)

    plt.imshow(ims)
    a = click()
    plt.show()
    if len(a.LandMarks)==19:
        print(i,len(a.LandMarks),a.LandMarks)
        line = img +' ' + str(a.LandMarks)
        #print(img, int(x1), int(y1), int(x2), int(y2), int(w), int(h))
        add(line,log)
        #print(line)
    else:
        print(img, 'pass')