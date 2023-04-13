from django.shortcuts import render

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly
from io import StringIO

def index_view(request):
    context={}

    x = np.linspace(0, 10, 100)
    y = x * 2
    fig = go.Figure(data=go.Line(x=x, y=y))

    graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
    context['grp3']=graph_div
    return render(request, 'index.html', context)
