#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 00:19:21 2018

@author: amit
"""

XYZ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 7
a = XYZ[:]
def loop(ls, item):
  l = len(ls)
  if ls[0] == item or ls[-1] == item:
    return True
  elif l < 3 or item > ls[-1] or item < ls[0]:
    return False
  elif ls[0] < item < ls[-1]:
    m = l//2
    if ls[m] > item:
      return loop(ls[0:m], item)
    elif ls[m] < item:
      return loop(ls[m+1:],item)
    else:
      return True
  else:
    return False
loop(XYZ, 7)
    
        
        

    
  
  


  
