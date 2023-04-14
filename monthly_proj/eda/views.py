from django.shortcuts import render

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import plotly.graph_objects as go
import plotly
# from io import StringIO

from .graphs.get_graph import get_graph_by_type, get_graph_by_vendor, get_graph_by_foundry

def index_view(request):
    context={}

    return render(request, 'index.html', context)


# 프로세서 타입에 따른 그래프
def page1_view(request):
    context={}
    li = get_graph_by_type()

    for index, fig in enumerate(li, start=1):
        graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
        context[f'grp{index}'] = graph_div

    return render(request, 'page1.html', context)


# 프로세서 디자인 회사에 따른 그래프
def page2_view(request):
    context={}
    li = get_graph_by_vendor()

    for index, fig in enumerate(li, start=1):
        graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
        context[f'grp{index}'] = graph_div

    return render(request, 'page2.html', context)


# 프로세서 제작 회사에 따른 그래프
def page3_view(request):
    context={}
    li = get_graph_by_foundry()

    for index, fig in enumerate(li, start=1):
        graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
        context[f'grp{index}'] = graph_div

    return render(request, 'page3.html', context)