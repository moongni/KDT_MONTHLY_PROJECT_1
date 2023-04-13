from django.shortcuts import render

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import plotly.graph_objects as go
import plotly
# from io import StringIO

from .graphs.get_graph import return_figures1

def index_view(request):
    context={}

    return render(request, 'index.html', context)


def page1_view(request):
    context={}
    fig1, fig2, fig3, fig4, fig5, fig6 = return_figures1()
    graph_div = plotly.offline.plot(fig1, auto_open = False, output_type="div")
    context['grp1']=graph_div
    graph_div = plotly.offline.plot(fig2, auto_open = False, output_type="div")
    context['grp2']=graph_div
    graph_div = plotly.offline.plot(fig3, auto_open = False, output_type="div")
    context['grp3']=graph_div
    graph_div = plotly.offline.plot(fig4, auto_open = False, output_type="div")
    context['grp4']=graph_div
    graph_div = plotly.offline.plot(fig5, auto_open = False, output_type="div")
    context['grp5']=graph_div
    graph_div = plotly.offline.plot(fig6, auto_open = False, output_type="div")
    context['grp6']=graph_div
    

    return render(request, 'page1.html', context)

def page2_view(request):
    context={}

    return render(request, 'page2.html', context)

def page3_view(request):
    context={}

    return render(request, 'page3.html', context)