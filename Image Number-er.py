# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:11:56 2022

@author: Hamil Patel

Program will take a folder of pictures and place a number on each image in order in the lower left corner 
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import glob



#Change this to indicate which folder of images to number; 
filepath = "C:/Users/hamil/School Things/Sample Data/Sample Pictures/"


image_list = []


for filename in glob.glob('{0}*.jpg' .format(filepath)): 
    im=Image.open(filename)
    image_list.append(im)
    
    
    
    
font = ImageFont.truetype("calibri.ttf", 20)
i=1;
for file in image_list:
    img= file
    I1= ImageDraw.Draw(img)
    I1.text((25,230),str(i), fill=(255,255,255), font =font)
    img.save('{0}image_{1}.jpg' .format(filepath, str(i)))
    i=i+1
    