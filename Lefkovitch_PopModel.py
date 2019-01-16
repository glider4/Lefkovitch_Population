#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:18:44 2019

@author: Mathemacode

The Lefkovitch model is commonly used 
for population modeling like it is here
(this example has to do with Guppies), where
there are also probabilities given that
the animal/subject will not survive during 
a specific stage so therefore obviously
cannot make it to the next one.  These 
probabilities are called "STAY1" for the 
probability that the subject will survive
in that stage for a full year.

View my "Leslie_PopModel" repository; this
code was adapted based on that project.
"""
import numpy as np

n = 150
Y = np.zeros([3,n])  # open this matrix up after running to see actual population numbers change
lam = np.zeros([3,n])  # lambda result values

# Reproduction Rates
REP1 = 0
REP2 = 0
REP3 = 300  # that's a lot of guppies

# Survival rates
SURV1 = 0.00003
SURV2 = 0.071

# Remain rates (probability of survival within current stage)
STAY1 = 0.777
STAY2 = 0.949

# Initial populations in each stage
Y[0,0] = 30000
Y[1,0] = 4500
Y[2,0] = 800

for i in range(1,n):
    Y[0,i] = REP1*Y[0, i-1] + REP2*Y[1, i-1] + REP3*Y[2, i-1]
    Y[1,i] = SURV1*Y[0, i-1] + STAY1*Y[1, i-1]
    Y[2,i] = SURV2*Y[1, i-1] + STAY2*Y[2, i-1]

for i in range(0,n-1):
    lam[0,i] = Y[0,i+1]/Y[0, i]
    lam[1,i] = Y[1,i+1]/Y[1, i]
    lam[2,i] = Y[2,i+1]/Y[2, i]

        
print("\n Lambda condenses to: ", (lam[1,i]+lam[2,i])/2)
print("\n Remember you can view actual population values change by viewing the full matrix 'Y'")
    
    
    
    
    
