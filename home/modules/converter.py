import cv2
import os

from cv2 import COLOR_BGR2GRAY

def convert(path, size):
    #n = os.path.splitext(img_name[0])
    #p = os.path.join("C:/Users/Sukhm/Documents/opencv/uploads/", n)
    img = cv2.imread(path)
    sp = int(size)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(gray, (sp, sp))
    cv2.imwrite(path, resize)
