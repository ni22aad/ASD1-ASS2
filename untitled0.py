

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from read_file import reading_data
from lineplot import graph_line_plot
from barplot import graph_bar_plot
from correlation import correlation_heatmap_us
from correlation_india import correlation_heatmap_in
from correlation_tur import correlation_heatmap_can
from correlation_s import correlation_heatmap_swiz
    
    # main function
if __name__ == "__main__":
    
    country_data,year_data,original_data=reading_data("data.csv")
    
    graph_bar_plot(original_data,'Urban population','Urban population')
    
    graph_bar_plot(original_data,'Arable land (% of land area)','Arable land (% of land area)')
    
    graph_line_plot(original_data, 'Agricultural land (sq. km)','Agricultural land (sq. km)',60)
    
    graph_line_plot(original_data, 'Forest area (% of land area)','Forest area (% of land area)',31)
    
    correlation_heatmap_us(original_data,"us")
    
    correlation_heatmap_in(original_data,"in")
    
    correlation_heatmap_can(original_data,"Canada")
    
    correlation_heatmap_swiz(original_data,"Switzerland")
