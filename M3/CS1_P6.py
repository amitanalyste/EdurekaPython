#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:00:51 2018

@author: amit
"""
def problem6(start: int, end:int) -> str:
  '''
  program which will find all such numbers which are divisible by 7 but are not a multiple of 5
  >>> problem6(2000, 3000)
  '2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996'
  '''
  return ','.join(str(i) for i in range(start, end+1) if i % 7 == 0 and i % 5 != 0)

def problem7(n: int) -> int:
  '''
  function to compute factorial
  >>> problem7(8)
  40320
  '''
  def loop(acc: int, n: int) -> int:
    if n <= 1:
      return acc
    else:
      return loop(acc*n, n-1)
  return loop(1, n)
from math import sqrt

def calculation(D, C=50, H=30):
  return int(sqrt(2*C*D/H))
def problem8(Ds: str)-> str:
  '''
  >>> problem8('100,150,180')
  '18,22,24'
  '''
  d = Ds.split(',')
  return ','.join(str(calculation(int(x))) for x in d)


import numpy as np


def problem9(X: int, Y: int) -> list:
  '''
  >>> problem9(3,5)
  [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
  '''
  x,y = np.array(range(X)), np.array(range(Y))
  return [list(item * y) for item in x]

def problem10(sentence: str)-> str:
  '''
  >>> problem10('without,hello,bag,world')
  'bag,hello,without,world'
  '''
  
  return ','.join(sorted(sentence.split(',')))

def problem11():
  lines = []
  while True:
    l = input()
    if l:
      lines.append(l.upper())
    else:
      break
  for l in lines:
    print(l)
    
def problem12():
  line = input("Enter a sentence- \n")
  return ' '.join(sorted(list(set(line.split(' ')))))

def binaryToDidgitap1(bn: str)-> int:
  acc = 0
  i = 0 
  rev_bn = bn[::-1]
  for x in rev_bn:
    if int(x):
      acc += pow(2,i)
    i += 1
  return acc

def binaryToDidgitap2(bn: str)-> int:
  def loop(acc, bn, offset):
    if offset < len(bn): 
      if int(bn[offset]):
        acc += pow(2,offset)
      offset += 1
      return loop(acc, bn, offset)
    else:
      return acc
  return loop(0, bn[::-1], 0)
      


def problem13():
  binums = input("Enter a sequence of 4 digit binary numbers separated by comma: \n").split(',')
  return ','.join(bnum for bnum in binums if binaryToDidgitap2(bnum) % 5 == 0)
  
def problem14():

  sentence = input("Enter a sentence \n ")
  u,l = 0,0
  for char in sentence:
    if char.isupper():
      u += 1
    elif char.islower():
      l += 1
    else:
      pass
  print(f"UPPER CASE {u}\nLOWER CASE {l}")
  

def problem14_recursive():
  sentence = input("Enter a sentence \n ")
  def loop(u, l, i):
    if i < len(sentence):
      if sentence[i].islower():
        l += 1
      elif sentence[i].isupper():
        u += 1
      i += 1
      return loop(u, l, i)
    else:
      return (u,l)
  return loop(0, 0, 0)

a = [sqrt(x) for x in range(3,30,2)]
b = [int(pow(x,2)) for x in range(1,20,2)]
print(f"Example of sum: {sum(a)}\nExample of fsum: {fsum(a)}")
print(f"Example of sum: {sum(b,10)}\nExample of fsum: {fsum(b)}") 
      
  



if __name__ == '__main__':
  import doctest
  print(doctest.testmod())
