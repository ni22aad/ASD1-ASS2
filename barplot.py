#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:31:24 2022

@author: umair
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
 # plot a bar graoh  
def graph_bar_plot(data,indicator,indicator_name):
    '''
    this function draw bar plot graph for the 4 countries year 1995 to 2020
    '''
    #  creating a data frame
    factor_data=data[data["Indicator Name"]==indicator]
    
    in_data=factor_data[factor_data["Country Name"]=="India"].drop(['Country Name','Indicator Name'],axis=1)

    us_data=factor_data[factor_data["Country Name"]=="United States"]
    
    ca_data=factor_data[factor_data["Country Name"]=="Canada"]
    
    swiz_data=factor_data[factor_data["Country Name"]=="Switzerland"]
    
    index = ['1995', '2000', '2005',
          '2010', '2015', '2020']
    
    df = pd.DataFrame({'Switzerland':  [swiz_data['1995'].iloc[0],swiz_data['2000'].iloc[0],swiz_data['2005'].iloc[0],swiz_data['2010'].iloc[0],swiz_data['2015'].iloc[0],swiz_data['2020'].iloc[0],],
                       'United States': [us_data['1995'].iloc[0],us_data['2000'].iloc[0],us_data['2005'].iloc[0],us_data['2010'].iloc[0],us_data['2015'].iloc[0],us_data['2020'].iloc[0],],
                    'India':  [in_data['1995'].iloc[0],in_data['2000'].iloc[0],in_data['2005'].iloc[0],in_data['2010'].iloc[0],in_data['2015'].iloc[0],in_data['2020'].iloc[0],],
                    'Canada':  [ca_data['1995'].iloc[0],ca_data['2000'].iloc[0],ca_data['2005'].iloc[0],ca_data['2010'].iloc[0],ca_data['2015'].iloc[0],ca_data['2020'].iloc[0],],
                    
                    }, index=index)
    
    # ploting bar graph
    ax = df.plot.barh(title=indicator_name)
    
    plt.show()