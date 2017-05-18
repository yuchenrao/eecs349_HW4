import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob
from random import shuffle


def getlabel(name):

    if name == 'data/Ace':
        im_label = '1'
    elif name == 'data/2':
        im_label = '2'
    elif name == 'data/3':
        im_label = '3'
    elif name == 'data/4':
        im_label = '4'
    elif name == 'data/5':
        im_label = '5'
    elif name == 'data/6':
        im_label = '6'
    elif name == 'data/7':
        im_label = '7'
    elif name == 'data/8':
        im_label = '8'
    elif name == 'data/9':
        im_label = '9'
    elif name == 'data/10':
        im_label = '10'
    elif name == 'data/Jack':
        im_label = '11'
    elif name == 'data/Queen':
        im_label = '12'
    elif name == 'data/King':
        im_label = '13'

    return im_label

# get features based on SIFT features
def getSIFTfeatures(input_img):

    # gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT()
    step_size = 20
    newimg = input_img
    # newimg = zoom(gray, (200. / gray.shape[0], 200. / gray.shape[1]))
    kp = [cv2.KeyPoint(x, y, step_size) for y in range(0, newimg.shape[0], step_size)
                                        for x in range(0, newimg.shape[1], step_size)]
    kp, dense = sift.compute(newimg, kp)
    im_mat = dense

    return im_mat

def main():
    f = open('data.csv', 'w')
    for filename in glob.glob('data/*.jpg'):
        name = filename.split("_")
        label = getlabel(name[0])
        input_img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
        data = cv2.resize(input_img, (30, 30))
        imgArray = ','.join(str(x) for x in np.array(data).flatten())
        f.write(imgArray + '\n')
    f.close()


if __name__ == "__main__":
    main()
