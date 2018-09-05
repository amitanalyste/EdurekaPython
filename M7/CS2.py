#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 14:37:06 2018

@author: amit
"""

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
# to make this notebook's output stable across runs
np.random.seed(42)


# Loading dataset
horseDf = pd.read_csv("/users/amit/data/horse.csv")

#Q1 - Check for NUll Values
np.sum(horseDf.isnull())
incomplete_rows = horseDf[horseDf.isnull().any(axis=1)]

df = horseDf.copy()
#Q2 - Label Encoding for Categorical feature
categorical_columns = list(df.select_dtypes(include='object').columns)
'''
for column in categorical_columns:
  df[column] = df[column].astype('category')'''

y = df['cp_data']
df.drop(['cp_data'], axis = 1, inplace = True)
from sklearn.preprocessing import LabelEncoder

categorical_columns_indexes = [df.columns.get_loc(column) for column in categorical_columns[:-1]]
for index in categorical_columns_indexes:
  label_encoder = LabelEncoder()
  df.iloc[:, index] = label_encoder.fit_transform(df.iloc[:, index].astype(str))


from sklearn.preprocessing import Imputer
imputer = Imputer(strategy= "most_frequent")
X = imputer.fit_transform(df)
df = pd.DataFrame(X, columns = df.columns, index = list(df.index.values))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size = 0.33, random_state = 42)

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
tree.score(X_test, y_test)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf.score(X_test, y_test)



