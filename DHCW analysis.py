# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 11:51:21 2026

@author: Eben
"""

import pandas as pd

import statsmodels.api as sm

# Read in the data csv into a pandas dataframe
db = pd.read_csv("C:\\Users\\Eben\\Documents\\DHCW Internship\\Data_for_stats.csv")

# Clean data to unify health boards to same formatting
for x in db.index:
    if db.loc[x, 'Health board'] == 'HD':
        db.loc[x, 'Health board'] = 'Hywl Dda'
        print(db.loc[x, 'Health board'])

# Clean data to unify area formatting
for x in db.index:
    if db.loc[x, 'Area'] == 'RURRAL':
        db.loc[x, 'Area'] = 'Rural'
        print(db.loc[x, 'Health board'])
        print(x)

# Perform a linear regression model to predict attendance of the 
model = sm.formula.glm("Attended ~ C(Sex, Appointment type, Location type)",
                       family=sm.families.Binomial(), data=db).fit()

# Print the results of the regression model
print(model.summary())
