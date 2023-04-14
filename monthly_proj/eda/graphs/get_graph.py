from typing import Tuple, Dict
from plotly.graph_objs._figure import Figure
import os

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


path = os.path.dirname(os.path.realpath(__file__))
cat_data = pd.read_csv(os.path.join(path, 'data', 'categorical_data.csv'))
num_data = pd.read_csv(os.path.join(path, 'data', 'numeric_data.csv'))


def fig_layout(fig, l='Legend',                 # figure 객체, 제목, 제목 크기 
               f_s=15, f_c='black',             # 글자 크기, 글자 색깔
               paper_c='', plot_c=''):          # 배경 색깔, 그래프 바탕 색깔
    fig.update_layout(
            legend = {
                'title' : l
            },
            font = {
                'size' : f_s,
                'color' : f_c
            },
            # paper_bgcolor = paper_c,
            # plot_bgcolor = plot_c
        )


def get_pie(names, values, hole, legend="", **kwargs):
    fig = px.pie(names=names, values=values, hole=hole, **kwargs)
    fig_layout(fig, l=legend)
    return fig


def get_bar(x, y, color, legend="", **kwargs):
    fig = px.bar(x=x, y=y, color=color, **kwargs)
    fig_layout(fig, l=legend)
    return fig


def get_scatter(data, x, y, color=None, legend="", **kwargs):
    fig = px.scatter(data_frame=data, x=x, y=y, color=color, **kwargs)
    fig_layout(fig, l=legend)
    return fig    


def get_hist(data, x, legend="", **kwargs):
    fig = px.histogram(data_frame=data, x=x, **kwargs)
    fig_layout(fig, l=legend)
    return fig


def get_box(data, x, color, legend="", **kwargs):
    fig = px.box(data_frame=data, x=x, color=color, **kwargs)
    fig_layout(fig, l=legend)
    return fig


# 프로세서 타입에 따른 그래프
def get_graph_by_type():
    graphs = []
    # title Type Distribution
    graphs.append(get_pie(names=cat_data['Type'].value_counts().index,
                          values=cat_data['Type'].value_counts(),
                          hole=0.3,
                          legend='Type'))
    # title 2 in 1
    graphs.append(get_box(data=cat_data, 
                          x='Process Size (nm)', 
                          color='Vendor', 
                          legend='Vendor', 
                          facet_col='Type'))
    # title Processor Size changes Over Time
    graphs.append(get_scatter(data=cat_data,
                              x='Release Date',
                              y='Process Size (nm)',
                              color='Type',
                              legend='Type'))
    # title TDP Change Over Time By Processor Type
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='TDP (W)', 
                              color='Type', 
                              legend='Type'))
    # title Die Size Change Over Time By Processor Type
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='Die Size (mm^2)', 
                              color='Type', 
                              legend='Type'))
    # title Transistor Change Over Time By Processor Type
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='Transistors (million)', 
                              color='Type', 
                              legend='Type'))
    # title Frequency Change Over Time By Processor Type
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='Freq (MHz)', 
                              color='Type', 
                              legend='Type'))
    # title Processor Data Correlation Coefficient
    graphs.append(px.imshow(num_data.corr().round(2), text_auto=True))
    return graphs


# 공급 업체에 따른 그래프
def get_graph_by_vendor():
    graphs = []
    # title Size Distribution By Vendor
    graphs.append(get_box(data=cat_data, 
                          x='Process Size (nm)', 
                          color='Vendor', 
                          legend='Vendor'))
    # title Processor Size Change By Vendor    
    graphs.append(get_scatter(data=cat_data,
                              x='Release Date',
                              y='Process Size (nm)',
                              color='Vendor',
                              legend='Vendor'))
    # title TDP Change Over Time By Vendor
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='TDP (W)', 
                              color='Vendor', 
                              legend='Vendor'))
    # title Die Size Change Over Time By Vendor
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='Die Size (mm^2)', 
                              color='Vendor', 
                              legend='Vendor'))
    # title Transistor Change Over Time By Vendor
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='Transistors (million)', 
                              color='Vendor', 
                              legend='Vendor'))
    # title Frequency Change Over Time By Vendor
    graphs.append(get_scatter(data=cat_data,
                              x='Release Date',
                              y='Freq (MHz)',
                              legend='Vendor',
                              color='Vendor'))    
    return graphs


# 주조 업체에 따른 그래프
def get_graph_by_foundry():
    graphs = []
    # title Foundry Distribution
    graphs.append(get_pie(names=cat_data['Foundry'].value_counts().index,
                          values=cat_data['Foundry'].value_counts(),
                          hole=0.3,
                          legend='Foundry'))
    # title Processor Size Distribution By Foundry
    graphs.append(get_box(data=cat_data, 
                          x='Process Size (nm)', 
                          color='Foundry', 
                          legend='Foundry'))
    # title Processor Size Change By Foundry    
    graphs.append(get_scatter(data=cat_data,
                              x='Release Date',
                              y='Process Size (nm)',
                              color='Foundry',
                              legend='Foundry'))
    # title TDP Change Over Time By Foundry
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='TDP (W)', 
                              color='Foundry', 
                              legend='Foundry'))
    # title Die Size Change Over Time By Foundry
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='Die Size (mm^2)', 
                              color='Foundry', 
                              legend='Foundry'))
    # title Transistor Change Over Time By Foundry
    graphs.append(get_scatter(data=cat_data, 
                              x='Release Date', 
                              y='Transistors (million)', 
                              color='Foundry', 
                              legend='Foundry'))
    # title Frequency Change Over Time By Foundry
    graphs.append(get_scatter(data=cat_data,
                              x='Release Date',
                              y='Freq (MHz)',
                              legend='Foundry',
                              color='Foundry'))
    return graphs


if __name__ == "__main__":
    # # test code
    graphs = get_graph_by_type()
    for fig in graphs:
        fig.show()


    graphs = get_graph_by_foundry()
    for fig in graphs:
        fig.show()


    graphs = get_graph_by_vendor()
    for fig in graphs:
        fig.show()