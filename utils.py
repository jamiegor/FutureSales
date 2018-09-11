import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#####################################################################
def moving_average(series, n):
    X = series
    prediction = X.head(n)
    for i in range(n,int(X.max()[0])+1):
        average = round(np.average(X.iloc[i-n:i]['item_cnt_day']),2)
        if X.iloc[i][0] - X.iloc[i-1][0] != 1:
            X = X.append({'date':X.iloc[i-1][0]+1,'item_cnt_day':average},ignore_index=True).sort_values(['date'])
        prediction = prediction.append({'date':X.iloc[i][0],'item_cnt_day':average},ignore_index=True)
        X = X.reset_index(drop=True)
        if X.iloc[i][0] >= int(X.max()[0]):
            break
    X['prediction'] = prediction['item_cnt_day']
        
    #plot this example
    plt.plot(X['date'],X['item_cnt_day'],X['prediction'])
    plt.xlabel('Date')
    plt.ylabel('#Item Sold')
    plt.title('Item_cnt_day vs prediction using Moving Average')
    plt.show()  

    #Total distance between valuess predicted and values given
    true_preds = X[X['date'].isin(series['date'])][n:]
    return round(np.linalg.norm(true_preds['item_cnt_day'] - true_preds['prediction']),2)
#############################################################################
def exp_smoothing(series, alpha):
    X = series
    prediction = X.head(1)
    for i in range(1,int(X.max()[0])+1):
        predict_value = alpha*X.iloc[i-1][1]+(1-alpha)*prediction.iloc[i-1][1]
        if X.iloc[i][0] - X.iloc[i-1][0] != 1:
            X = X.append({'date':X.iloc[i-1][0]+1,'item_cnt_day':predict_value},ignore_index=True).sort_values(['date'])
        prediction = prediction.append({'date':X.iloc[i][0],'item_cnt_day':predict_value},ignore_index=True)
        X = X.reset_index(drop=True)
        if X.iloc[i][0] >= int(X.max()[0]):
            break
    X['prediction'] = prediction['item_cnt_day']
        
    #plot this example
    plt.plot(X['date'],X['item_cnt_day'],X['prediction'])
    plt.xlabel('Date')
    plt.ylabel('#Item Sold')
    plt.title('Item_cnt_day vs prediction using Exponential Smoothing with alpha = 0.9')
    plt.savefig('Exponential Smoothing alpha = 0.1.png')
    plt.show()  

    #Total distance between valuess predicted and values given
    true_preds = X[X['date'].isin(series['date'])][:]
    return round(np.linalg.norm(true_preds['item_cnt_day'] - true_preds['prediction']),2)

############################################################################
def double_exp_smoothing(series, alpha,beta):
    X = series
    prediction = X.head(2)
    last_level = X.iloc[0][1]
    last_trend = X.iloc[1][1]-X.iloc[0][1]
    for i in range(2,int(X.max()[0])+1):
        level = alpha*X.iloc[i-1][1]+(1-alpha)*(last_level+last_trend)
        trend=  beta*(level-last_level)+(1-beta)*last_trend
        forecast = max(level+trend,0)
        last_level = level
        last_trend = trend
        if X.iloc[i][0] - X.iloc[i-1][0] != 1:
            X = X.append({'date':X.iloc[i-1][0]+1,'item_cnt_day':forecast},ignore_index=True).sort_values(['date'])
        prediction = prediction.append({'date':X.iloc[i][0],'item_cnt_day':forecast},ignore_index=True)
        X = X.reset_index(drop=True)
        if X.iloc[i][0] >= int(X.max()[0]):
            break
    X['prediction'] = prediction['item_cnt_day']
        
    #plot this example
    plt.plot(X['date'],X['item_cnt_day'],X['prediction'])
    plt.xlabel('Date')
    plt.ylabel('#Item Sold')
    plt.title('Item_cnt_day vs prediction using Exponential Smoothing with alpha = 0.9')
    plt.show()  

    #Total distance between valuess predicted and values given
    true_preds = X[X['date'].isin(series['date'])][:]
    return round(np.linalg.norm(true_preds['item_cnt_day'] - true_preds['prediction']),2)
#######################################################################
def triple_exp_smoothing(series, alpha,beta):
    X = series
    prediction = X.head(2)
    last_level = X.iloc[0][1]
    last_trend = X.iloc[1][1]-X.iloc[0][1]
    for i in range(2,int(X.max()[0])+1):
        level = alpha*X.iloc[i-1][1]+(1-alpha)*(last_level+last_trend)
        trend=  beta*(level-last_level)+(1-beta)*last_trend
        forecast = max(level+trend,0)
        last_level = level
        last_trend = trend
        if X.iloc[i][0] - X.iloc[i-1][0] != 1:
            X = X.append({'date':X.iloc[i-1][0]+1,'item_cnt_day':forecast},ignore_index=True).sort_values(['date'])
        prediction = prediction.append({'date':X.iloc[i][0],'item_cnt_day':forecast},ignore_index=True)
        X = X.reset_index(drop=True)
        if X.iloc[i][0] >= int(X.max()[0]):
            break
    X['prediction'] = prediction['item_cnt_day']
        
    #plot this example
    plt.plot(X['date'],X['item_cnt_day'],X['prediction'])
    plt.xlabel('Date')
    plt.ylabel('#Item Sold')
    plt.title('Item_cnt_day vs prediction using Exponential Smoothing with alpha = 0.9')
    plt.show()  

    #Total distance between valuess predicted and values given
    true_preds = X[X['date'].isin(series['date'])][:]
    return round(np.linalg.norm(true_preds['item_cnt_day'] - true_preds['prediction']),2)
