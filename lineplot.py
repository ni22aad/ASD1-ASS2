#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:27:05 2022

@author: umair
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def graph_line_plot(data,indicator,indicator_name,length):
    '''
    this function plot graph line plot of specific country 
    '''
    # create a dataframe
    factor_data=data[data["Indicator Name"]==indicator]
    
    in_data=factor_data[factor_data["Country Name"]=="India"].drop(['Country Name','Indicator Name'],axis=1)

    us_data=factor_data[factor_data["Country Name"]=="United States"].drop(['Country Name','Indicator Name'],axis=1)
    
    ca_data=factor_data[factor_data["Country Name"]=="Canada"].drop(['Country Name','Indicator Name'],axis=1)
    
    swiz_data=factor_data[factor_data["Country Name"]=="Switzerland"].drop(['Country Name','Indicator Name'],axis=1)
  
    # get year data from data frame
    year=data.drop(['Country Name','Indicator Name'],axis=1).T.index
    
    print(year)
    
    # plotting the points 
    plt.plot(pd.to_numeric(year[0:length].to_numpy()),in_data.iloc[0].dropna().to_numpy() , label = "India",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:length].to_numpy()),us_data.iloc[0].dropna().to_numpy() , label = "United States",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:length].to_numpy()),ca_data.iloc[0].dropna().to_numpy() , label = "Canada",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:length].to_numpy()),swiz_data.iloc[0].dropna().to_numpy() , label = "Switzerland",linestyle="-.")
    
      
    # naming the x axis
    plt.xlabel('year')
    # naming the y axis
    plt.ylabel('data')
    plt.legend()
    # giving a title to my graph
    plt.title(indicator_name)
      
    # function to show the plot
    plt.show()