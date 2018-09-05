#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:38:47 2018

@author: amit
"""
import re
data_loc = '/Users/amit/Edureka/DS/Python/M3/574_m3_datasets_v3'
file_name = 'FairDealCustomerData.csv'

class CustomerNotAllowedException(Exception):
  pass

class Customer:
  def __init__(self, last_name, title, first_name, blacklisted):
    self.last_name = last_name
    self.title = title
    self.first_name = first_name
    self.blacklisted = blacklisted

fileObject = open(f"{data_loc}/{file_name}", 'r')
fileContent = fileObject.read()
records = fileContent.split('\n')[:-1]
p_ln = re.compile(r'[A-Za-z]+,')
p_ti = re.compile(r',\s[A-Za-z]+\.')
p_fn = re.compile(r'\.[\sA-Za-z/]+\,')
p_fl = re.compile(r'\d')

def createOrder(cust):
  try:
    if cust.blacklisted == 0:
      raise CustomerNotAllowedException(cust.blacklisted)
    else:
      pass
  except CustomerNotAllowedException as err:
    print(f"\033[1;31;47m CustomerNotAllowedException because blacklisted value is {err}")



def customerCreate(a):
  last_name = re.findall(p_ln, a)[0][:-2]
  title = re.findall(p_ti, a)[0][2:-1]
  first_name = re.findall(p_fn, a)[0][2:-2]
  flag = int(re.findall(p_fl,a)[0])
  return Customer(last_name, title, first_name, flag)
  

customerInput = [customerCreate(x) for x in records]

cust = customerCreate(records[5])
createOrder(cust)







