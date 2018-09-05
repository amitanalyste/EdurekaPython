#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 23:17:16 2018

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
loan = pd.read_csv("/users/amit/data/loan_borowwer_data.csv")

