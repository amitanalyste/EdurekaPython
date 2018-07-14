#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:56:15 2018

@author: amit
"""
#!/usr/bin/python
hostname = 'localhost'
username = 'root'
password = 'nyk@2010'
database = 'edureka'

        
import pymysql
con = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
cursor = con.cursor()


def createUser():
  name = input("Enter name \n")
  pwd = input("Enter password \n")
  cursor.execute("select max(userId) from user")
  userId = int(cursor.fetchall()[0][0]) + 1
  cursor.execute(f"insert into user values ({userId}, {pwd}, {name})")
  con.commit()
  print(f"User create with userId: {userId}")
def changePassword(userId):
  cursor.execute(f"select userName, password from user where userId = {userId}")
  name, pwd = cursor.fetchall()[0]
  if input("Enter the old password first: \n") == pwd:
    new_password = input("New password: \n")
    cursor.execute(f"update user set password = '{new_password}' where userId = {userId}")
    con.commit()
    print(f"Password reset successful for userId: {userId}")
  else:
    print(f"Password not matching for userId: {userId}")
    
def withdrawMoney(userId, amt, balance):
  if amt > balance:
    print(f"Insufficient balance, {balance}")
  else:
    new_balance = balance - amt
    cursor.execute(f"update account set balance = {new_balance} where userId = {userId}")
    con.commit()
    print(f"New balance: {new_balance}")
    
def depositMoney(userId, amt, balance):
  new_balance = balance + amt
  cursor.execute(f"update account set balance = {new_balance} where userId = {userId}")
  con.commit()
  print(f"New balance: {balance[userId]}")

userId = int(input("Enter the userId: \n"))
cursor.execute(f"select count(*) from user where userId = {userId}") 
if cursor.fetchall()[0][0]:
  selection = int(input("Enter one of the option: \n 1: cash withdrawl. \n 2: cash credit \n 3: change password \n"))
  if selection == 1:
    amt = int(input("Enter Amount to withdraw\n"))
    if(cursor.execute(f"select balance from account where userId = {userId}")):
      balance = cursor.fetchall()[0][0]
      withdrawMoney(userId, amt, balance)
    else:
      input("User doesn't have account created\n press 1 if you want to create new user")
      
  elif selection == 2:
    amt = float(input("Enter Amount to deposit\n"))
    if cursor.execute(f"select balance from account where userId = {userId}"):
      balance = cursor.fetchall()[0][0]
      depositMoney(userId, amt, balance)
    else:
      if int(input("User doesn't have account. \n Enter 1 if want to create account with deposited money")) == 1:
        createUser()
      
  elif selection == 3:
    changePassword(userId)
  else:
    pass
else:
  print(f"{userId} not registered in the system!")
con.close()
pass
    