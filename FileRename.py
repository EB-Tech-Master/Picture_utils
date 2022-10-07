# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:24:48 2020

@author: User
"""

import os
os.chdir("C:/Users/User/Documents/EBTECH/dataset/cannon/train2")
i=1881
for file in os.listdir():
      src=file
      dst="Pic_"+str(i)+".jpg"
      os.rename(src,dst)
      i+=1