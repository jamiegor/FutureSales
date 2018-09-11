# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from utils import *


# Read the dataset
dataset = pd.read_csv('sales_train.csv')


#Find the item with the most data to analyse first
X = dataset.loc[dataset['item_id'] == dataset.mode()['item_id'][0]]
X = X.loc[X['shop_id'] == X.mode()['shop_id'][0]]

#parse dates
for i in range(X.shape[0]):
    X.iloc[i,0] = parse(X.iloc[i,0])
min_date = X.min()[0]
for i in range(X.shape[0]):
    X.iloc[i,0] = (X.iloc[i,0] - min_date).days
X = X.sort_values(by=['date'])[['date','item_cnt_day']]


#plot this example
X.plot(x='date',y='item_cnt_day')
###############################################################
#Simple models
#################################################################

#Moving Average
##########################
result = pd.DataFrame(columns = ['nb_days','total_distance'])
for i in range(5,50,5):
    result = result.append({'nb_days':i,'total_distance':moving_average(X,i)},ignore_index=True)
best_moving_avg = result.loc[result['total_distance'] == result['total_distance'].min()]


#Exponential Smoothing
##########################
result = pd.DataFrame(columns = ['alpha','total_distance'])
for i in range(1,10):
    alpha = 0.1*i
    result = result.append({'alpha':alpha,'total_distance':exp_smoothing(X,alpha)},ignore_index=True)
best_alpha = result.loc[result['total_distance'] == result['total_distance'].min()]


#Double Exponential Smoothing
#############################
result = pd.DataFrame(columns = ['alpha','beta','total_distance'])
for i in range(1,10):
    for j in range(1,10):
        alpha = 0.1*i
        beta = 0.1*j
        result = result.append({'alpha':alpha,'beta':beta,'total_distance':double_exp_smoothing(X,alpha,beta)},ignore_index=True)
best_alpha_beta = result.loc[result['total_distance'] == result['total_distance'].min()]


#Triple Exponential Smoothing
#############################
result = pd.DataFrame(columns = ['alpha','beta','total_distance'])
for i in range(1,10):
    for j in range(1,10):
        alpha = 0.1*i
        beta = 0.1*j
        result = result.append({'alpha':alpha,'beta':beta,'total_distance':double_exp_smoothing(X,alpha,beta)},ignore_index=True)
best_alpha_beta = result.loc[result['total_distance'] == result['total_distance'].min()]

