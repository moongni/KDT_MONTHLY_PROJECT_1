
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

def test_graph():
    x = np.linspace(0, 10, 100)
    y = x * 2
    fig = go.Figure(data=go.Line(x=x, y=y))

    return fig

if __name__ == '__main__':
    test_graph()
