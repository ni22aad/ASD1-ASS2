import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def reading_data(name):
    '''
    this function read data and return in the required form
    '''
    # read data
    df = pd.read_csv(name,skiprows=4)
    
    original_data=df.drop(['Country Code', 'Indicator Code'],axis=1)
    
    countries_data=df.drop(['Country Code', 'Indicator Name', 'Indicator Code'],axis=1)
    
    year_data= df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',],axis=1).T
    
    year_data.index.name='Years'
    
    # print header data
    print(year_data.head)
    print(countries_data.head)
    print(original_data.head)
    print(original_data.T)
    
    # return data transpose and original data with year as column and country as column
    return countries_data,year_data,original_data