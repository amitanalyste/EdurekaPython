#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 23:14:04 2018

@author: amit
"""

class Robot:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    
  def up(self, n):
    self.y += n
  def down(self, n):
    self.y -= n
  def left(self, n):
    self.x -= n
  def right(self, n):
    self.x += n
  def __str__(self):
    return f"Robot is at ({self.x},{self.y})."
  def instruction(self, direction, step):
    if direction == 'UP':
      self.up(step)
    elif direction == 'DOWN':
      self.down(step)
    elif direction == 'LEFT':
      self.left(step)
    else:
      self.right(step)
  
r = Robot()
print(r)
direction = ['UP', 'DOWN', 'LEFT', 'RIGHT']
flag = True
while flag:
  instruction = input("Enter the instruction for Robot: ").split()
  if len(instruction) == 2 and instruction[0] in direction and instruction[1].isdigit():
    r.instruction(instruction[0], int(instruction[1]))
    print(r)
  else:
    flag = False
    print(f"Incorrect entry! {r}\n Exiting now!")
  
  



