#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:29:17 2022

@author: umair
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def correlation_heatmap_us(data,name):
    '''
    this function show heatmap and thier correaltion between indicators for better understanding
    '''
    
   
        
    # create data frame
    factor_data=pd.DataFrame()
   
    # getting indicator data
    us_data=data[data["Indicator Name"]=="Urban population"]
             # get united states data 
    us_urban=us_data[us_data['Country Name']=="United States"].drop(['Country Name','Indicator Name'],axis=1).T
    # drop nan values
    us_urban=us_urban.dropna().T
        
        # get urban population data
    factor_data["Urban population"]=us_urban.iloc[0]
        
        #  get arable data
    us_data=data[data["Indicator Name"]=='Arable land (% of land area)']
        
        
    us_urban=us_data[us_data['Country Name']=="United States"].drop(['Country Name','Indicator Name'],axis=1).T
        
    us_urban=us_urban.dropna().T
        
    factor_data['Arable land (% of land area)']=us_urban.iloc[0]
        
    #  get cereal data
    us_data=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    us_urban=us_data[us_data['Country Name']=="United States"].drop(['Country Name','Indicator Name'],axis=1).T
        
    us_urban=us_urban.dropna().T
        
    factor_data['Agricultural land (sq. km)']=us_urban.iloc[0]
        
    us_data=data[data["Indicator Name"]=='Forest area (% of land area)']
        
    us_urban=us_data[us_data['Country Name']=="United States"].drop(['Country Name','Indicator Name'],axis=1).T
        
    us_urban=us_urban.dropna().T
        
    factor_data['Forest area (% of land area)']=us_urban.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # plot heatmap
    heatmap = sns.heatmap(factor_data.corr(), cmap="tab10",
                             
            annot=True,ax=ax
                
            )
       # add title
    ax.set_title('United States')
        
    plt.show()
        
   