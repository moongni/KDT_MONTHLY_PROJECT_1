from typing import Tuple, Dict
import os

import numpy as np
import pandas as pd
import chart_studio
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs._figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns

from setting import CHART_STUDIO_USERNAME, CHART_STUDIO_API

chart_studio.tools.set_credentials_file(username=CHART_STUDIO_USERNAME, api_key=CHART_STUDIO_API)

path = os.path.dirname(os.path.realpath(__file__))
cat_data = pd.read_csv(os.path.join(path, 'data', 'categorical_data.csv'))
num_data = pd.read_csv(os.path.join(path, 'data', 'numeric_data.csv'))


def get_pie_foundry_dittr() -> Figure:
    values = cat_data['Foundry'].value_counts()
    names = values.index
    fig = px.pie(names=names, values=values, hole=0.2)
    fig.update_layout({
        'title': {
            'text': 'Foundry Distribution',
            'x': 0.5
        }
    })

    return fig


def get_bar_foundry_dittr() -> Figure:
    values = cat_data['Foundry'].value_counts()
    names = values.index
    fig = px.bar(y=names, x=values, color=names)
    fig.update_layout({
        'title': {
            'text': 'foundry_category',
            'x': 0.5
        }
    })

    return fig


def get_corr() -> Figure:
    corr = num_data.corr().round(2)
    fig = px.imshow(corr, text_auto=True)

    return fig


def get_scatter(data:pd.DataFrame, x:str, y:str, **kwargs) -> Figure:
    fig = px.scatter(data_frame=data, y=y, x=x, **kwargs)
    return fig

def return_figures1():
    fig1 = get_pie_foundry_dittr()
    fig2 = get_bar_foundry_dittr()
    fig3 = get_corr()
    fig4 = get_scatter(cat_data, x="Die Size (mm^2)", y="TDP (W)", trendline="ols")
    fig5 = get_scatter(cat_data, x="Die Size (mm^2)", y="Transistors (million)", trendline="ols")
    fig6 = get_scatter(cat_data, x="Release Date", y="Freq (MHz)", color="Type")
    return fig1, fig2, fig3, fig4, fig5, fig6
if __name__ == "__main__":
    # test code
    ## test get_pie_foundry_dittr
    # return_figures1()

    fig1 = get_pie_foundry_dittr()
    print(type(fig1))
    fig1.show()

    ## test get_bar_foundry_dittr
    fig2 = get_bar_foundry_dittr()
    print(type(fig2))
    fig2.show()

    ## test get_corr
    fig3 = get_corr()
    print(type(fig3))
    fig3.show()

    ## test get_scatter
    fig4 = get_scatter(cat_data, x="Die Size (mm^2)", y="TDP (W)", trendline="ols")
    print(type(fig4))
    fig4.show()

    fig5 = get_scatter(cat_data, x="Die Size (mm^2)", y="Transistors (million)", trendline="ols")
    print(type(fig5))
    fig5.show()

    fig6 = get_scatter(cat_data, x="Release Date", y="Freq (MHz)", color="Type")
    print(type(fig6))
    fig6.show()