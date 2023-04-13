"""
본 graphs_1_9.py의 graphs_1_9 리스트 객체를 import,
graphs_1_9[0] ~ graphs_1_9[8] 각각에
<plotly.graph_objs._figure.Figure> 오브젝트가 할당되어 있음

"""

import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

path = os.path.dirname(os.path.realpath(__file__))
cg = pd.read_csv(os.path.join(path, 'data', 'chip_dataset.csv'))

cg["TDP (W)"] = cg["TDP (W)"].fillna(cg["TDP (W)"].mean())
cg["Die Size (mm^2)"] = cg["Die Size (mm^2)"].fillna(cg["Die Size (mm^2)"].mean())
cg["Transistors (million)"] = cg["Transistors (million)"].fillna(cg["Transistors (million)"].mean())

def fig_layout(fig, t, w=600, h=600, l = 'Legend',  # figure 객체, 제목, 제목 크기 
               f_s = 15, f_c = 'black',             # 글자 크기, 글자 색깔
               paper_c = '', plot_c = ''):          # 배경 색깔, 그래프 바탕 색깔
    fig.update_layout(
            title = {
                'font' : {'size' : 24},
                'text' : t,
                'x' : 0.5,
            },
            width = w,
            height = h,
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

def type_distribution_pie():
    fig = px.pie(names = cg.Type.value_counts().index,
                 values = cg.Type.value_counts(),
                 hole=0.3)
    fig_layout(fig, 'Type Distribution - Pie', l = 'Type')
    return fig

def type_distribution_bar():
    fig = px.bar(x = cg.Type.value_counts().index,
                 y = cg.Type.value_counts(),
                 color = cg.Type.value_counts().index)
    fig_layout(fig, 'Type Distribution - Bar', l = 'Type')
    return fig

def process_size_scatter():
    fig = px.scatter(data_frame = cg,
                     y = 'Process Size (nm)',
                     x = 'Release Date',
                     color ='Type')
    fig_layout(fig, 'Process Size Changes Over Time - Scatter', l = 'Type')
    return fig

def count_histogram():
    fig = px.histogram(data_frame = cg,
                       x = 'Process Size (nm)')
    fig_layout(fig, 'Number Distribution By Process Size - Histogram')
    return fig

def process_size_type_box():
    fig = px.box(data_frame = cg,
                 x = 'Process Size (nm)',
                 color = "Type")
    fig_layout(fig, 'Size Distribution By Processor Type - Box')
    return fig

def process_size_vendor_box():
    fig = px.box(data_frame = cg,
                 x = 'Process Size (nm)',
                 color = "Vendor")
    fig_layout(fig, 'Size Distribution By Processor Vendor - Box', l = 'Vendor')
    return fig

def process_size_foundry_box():
    fig = px.box(data_frame = cg ,
                 x = 'Process Size (nm)',
                 color = "Foundry",
                 height=600)
    fig_layout(fig, 'Size Distribution By Processor Foundry - Box', l = 'Foundry')
    return fig

def process_size_foundry_box_together():
    fig = px.box(data_frame = cg,
                 x = 'Process Size (nm)',
                 facet_col = "Type",
                 color = "Vendor")
    fig_layout(fig, '2 in 1 - Box', w = 1100, l = 'Vendor')
    return fig

def tdp_scatter():
    fig = px.scatter(data_frame = cg,
                     y = 'TDP (W)',
                     x = "Release Date",
                     color = "Type")
    fig_layout(fig, 'TDP Distribution Over Time - Scatter', l = 'Type')
    return fig

graphs_1_9 = [type_distribution_pie(),
              type_distribution_bar(),
              process_size_scatter(),
              count_histogram(),
              process_size_type_box(),
              process_size_vendor_box(),
              process_size_foundry_box(),
              process_size_foundry_box_together(),
              tdp_scatter()]

# color_discrete_map={}