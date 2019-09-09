import numpy as np
import os
import os.path as osp

labellist = '/home/wynmew/workspace/FaceBoxes.PyTorch/faceboxes'

idx=[]
for line in open(osp.join(labellist)):
    idx.append((os.path.join(line.strip())))

log = 'faceboxesRevised'

def add(x, logfile):
    with open(logfile,"a+") as outfile:
        outfile.write(x + "\n")

for i in range(len(idx)):
    line = idx[i].split(' ')
    img, x1, y1, x2, y2, w, h = line[0],line[1],line[2],line[3],line[4],line[5],line[6]
    if int(y1) <=10:
        h = str(int(h)+int(y1))
        y1 ='0'

    newline =img + ' ' + x1+ ' ' + y1 + ' ' + x2 + ' ' + y2 + ' ' + w + ' ' + h
    add(newline, log)
    print(newline)