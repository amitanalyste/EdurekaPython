#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:47:44 2018

@author: amit
"""

data_loc = '/Users/amit/Edureka/DS/Python/M3/574_m3_datasets_v3'
file_name = 'bank-data.csv'
fileObject = open(f"{data_loc}/{file_name}", 'r')
fileContent = fileObject.read()
records = fileContent.split('\n')
header = records[0]
records = records[1:-1]
uniqueJobs = {record.split(',')[1] for record in records}
age = {record.split(',')[0] for record in records}
age_loan_eligible = {'min': min(age), 'max': max(age)}
while True:
  profession = input("Enter the profession: \n").lower()
  if profession in uniqueJobs:
    print('Client is eligible')
  elif profession == 'end':
    break
  else:
    print('Client is not eligible')