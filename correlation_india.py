#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:48:44 2022

@author: umair
"""

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
def correlation_heatmap_in(data,name):
    '''
    this function show heatmap and thier correaltion between indicators for better understanding
    '''
    factor_data=pd.DataFrame()
        
        # get urban population
    uk_data=data[data["Indicator Name"]=="Urban population"]
        
        # get UK data
    uk_urban=uk_data[uk_data['Country Name']=="India"].drop(['Country Name','Indicator Name'],axis=1).T
        
        # drop nan value
    uk_urban=uk_urban.dropna().T
        
    factor_data["Urban population"]=uk_urban.iloc[0]
        
    uk_data=data[data["Indicator Name"]=='Arable land (% of land area)']
        
    uk_urban=uk_data[uk_data['Country Name']=="India"].drop(['Country Name','Indicator Name'],axis=1).T
        
    uk_urban=uk_urban.dropna().T
        
    # get arabledata
    factor_data['Arable land (% of land area)']=uk_urban.iloc[0]
        
    # get cereal data
    uk_data=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    uk_urban=uk_data[uk_data['Country Name']=="India"].drop(['Country Name','Indicator Name'],axis=1).T
        
    uk_urban=uk_urban.dropna().T
        
    factor_data['Agricultural land (sq. km)']=uk_urban.iloc[0]
        
    uk_data=data[data["Indicator Name"]=='Forest area (% of land area)']
        
    uk_urban=uk_data[uk_data['Country Name']=="India"].drop(['Country Name','Indicator Name'],axis=1).T
        
    uk_urban=uk_urban.dropna().T
        
    # get total population
    factor_data['Forest area (% of land area)']=uk_urban.iloc[0]
        
    # plot a heatmap with annotation
    ax = plt.axes()
        
    # plot heat map
    heatmap = sns.heatmap(factor_data.corr(), cmap="tab10",
            annot=True,ax=ax
                
            )
        
    # set title
    ax.set_title('India')
        
    plt.show()
        
   