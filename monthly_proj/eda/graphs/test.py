import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import chart_studio
from chart_studio.plotly import plot, iplot
import plotly.express as px
import plotly.graph_objects as go
from setting import CHART_STUDIO_API_KEY, CHART_STUDIO_USER

chart_studio.tools.set_credentials_file(username=CHART_STUDIO_USER, api_key=CHART_STUDIO_API_KEY)

def test_graph():
    x = np.linspace(0, 10, 100)
    y = x * 2
    fig = go.Figure(data=go.Line(x=x, y=y))

    return fig

if __name__ == '__main__':
    test_graph()