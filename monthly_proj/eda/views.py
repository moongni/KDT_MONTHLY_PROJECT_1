from django.shortcuts import render

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly
from io import StringIO
from .test import test_graph
from .graphs.get_graph import get_bar_foundry_dittr

def index_view(request):
    context={}

    # x = np.linspace(0, 10, 100)
    # y = x * 2
    # fig = go.Figure(data=go.Line(x=x, y=y))
    fig = test_graph()
    fig2 = get_bar_foundry_dittr()

    graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
    context['grp3']=graph_div

    graph_div = plotly.offline.plot(fig2, auto_open = False, output_type="div")
    context['grp2']=graph_div



    return render(request, 'index.html', context)
