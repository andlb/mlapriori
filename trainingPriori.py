# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:20:29 2017

@author: aborges
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
qtdcolumns = len(dataset.columns)
transaction = []
for i in range(0,len(dataset)):
    transaction.append([str(dataset.values[i,j]) for j in range(0,qtdcolumns )] )


from apyori import apriori
rules=apriori(transaction,min_support=0.003,min_confidence=0.2,min_lift=3,max_length=2)

results = list(rules)