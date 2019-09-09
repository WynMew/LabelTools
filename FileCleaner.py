import os
import os.path as osp
from PIL import Image

photolist = '/home/wynmew/data/downloads/danbooru2018/outlist'

idx=[]
for line in open(osp.join(photolist)):
    idx.append((os.path.join(line.strip())))

for i in range(0,len(idx)):
    img = idx[i]
    #print(i, img)
    try:
        a=Image.open(img)
        a.load()
        #print(img, 'processed')
    except:
        print(i,img, 'error')
        os.remove(img)


