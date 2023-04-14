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
    fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8 = li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7]

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
    graph_div = plotly.offline.plot(fig7, auto_open = False, output_type="div")
    context['grp7']=graph_div
    graph_div = plotly.offline.plot(fig8, auto_open = False, output_type="div")
    context['grp8']=graph_div
    

    return render(request, 'page1.html', context)

def page2_view(request):
    context={}
    li = get_graph_by_vendor()
    fig1, fig2, fig3, fig4, fig5, fig6= li[0], li[1], li[2], li[3], li[4], li[5]

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


    return render(request, 'page2.html', context)

def page3_view(request):
    context={}
    li = get_graph_by_foundry()
    fig1, fig2, fig3, fig4, fig5, fig6, fig7= li[0], li[1], li[2], li[3], li[4], li[5], li[6]
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
    graph_div = plotly.offline.plot(fig7, auto_open = False, output_type="div")
    context['grp7']=graph_div
    return render(request, 'page3.html', context)