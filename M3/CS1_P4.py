#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:04:04 2018

@author: amit
"""
import math
radiusEarth = 6373

point1 = lat1, lon1
point2 = lat2, lon2
  
latitude = lambda: math.radians(point2[0] - point1[0])
longitude = lambda: math.radians(point2[1] - point2[0])
         
a = lambda: pow(math.sin(latitude/2),2) + pow(math.cos(latitude),2) * pow(math.sin(longitude/2),2)

b = lambda: 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

d = lambda: radiusEarth * b
