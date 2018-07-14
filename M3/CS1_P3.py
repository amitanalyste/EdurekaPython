#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:50:55 2018

@author: amit
"""

from datetime import *
import time
t1 = datetime.strptime(time.ctime(),'%a %b %d %H:%M:%S %Y')
if t1.hour >= 19 or t1.hour <= 5:
  print("Night")
else:
  print("Day")