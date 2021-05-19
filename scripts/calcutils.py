# -*- coding: utf-8 -*-
"""
Created on Mon May 17 01:43:45 2021

@author: sandra
"""

from PIL import Image
import os
import numpy as np
from skimage.feature import match_template

def crop(directory,filename,ratio_left,ratio_top,ratio_bottom):
    im = Image.open(filename)
    width, height = im.size
    
    left = ratio_left*width
    right = width
    top = ratio_top*height
    bottom = height*ratio_bottom
    
    os.chdir(directory)
    
    im1 = im.crop((left,top,right,bottom))
    im1.save(filename)
    os.chdir('..')
    return 0

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def check_lock_button(lockbutton,image):
    result = match_template(image,lockbutton)
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]
    height, width = lockbutton.shape    
    identified_img = image[y:y+height,x:x+width]
    m = mse(lockbutton,identified_img)
    return m,x,y

def lock_button_init(lockbutton1,lockbutton2,image):
    m1,x1,y1=check_lock_button(lockbutton1,image)
    m2,x2,y2=check_lock_button(lockbutton2,image)

    lockbutton1_prop = {'error':m1,'x':x1,'y':y1,'data':lockbutton1}
    lockbutton2_prop = {'error':m2,'x':x2,'y':y2,'data':lockbutton2}
    
    return(lockbutton1_prop,lockbutton2_prop)


def check_mse(m1,m2,lockbutton1_prop,lockbutton2_prop):
    if m1 < m2:
        lockbutton_ref = lockbutton1_prop
    else:
        lockbutton_ref = lockbutton2_prop
    return lockbutton_ref

def crop_ref_lock(image,y,add_y1,add_y2,x,add_x1,add_x2):
    cropped = image[y+add_y1:y+add_y2,x+add_x1:x+add_x2]
    return cropped

def baby_image_proc(image_array):
    im = Image.fromarray(image_array)
    source = im.split()

    R, G, B = 0, 1, 2

    # select regions where each colour is less than X
    threshold = 240
    for rgb in range(3):
        blackmask = source[rgb].point(lambda i: i < threshold and 255)
    
        # process the band to be black
        out = source[rgb].point(lambda i: i * 0)
    
        # paste the processed band back, but only where colour was < X
        source[rgb].paste(out, None, blackmask)
    
    newim = Image.merge(im.mode, source)
    return newim