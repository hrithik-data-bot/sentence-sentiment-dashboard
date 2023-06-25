"""the graph function modules"""

import numpy as np
import plotly
from plotly import graph_objs as go


def create_gauge(prediction_data: dict) -> plotly.graph_objs._figure.Figure:
    """create a gauge chart"""

    labels = np.array(list(prediction_data.keys()))
    scores = np.array(list(prediction_data.values()))

    gauge_max_values = np.argmax(scores)
    gauge_label, gauge_value = labels[gauge_max_values].upper(), scores[gauge_max_values]

    if gauge_label == 'POSITIVE':
        color = 'green'
    elif gauge_label == 'NEGATIVE':
        color = 'red'
    elif gauge_label == 'NEUTRAL':
        color = 'yellow'

    fig = go.Figure(go.Indicator(mode="gauge+number", value=gauge_value, 
                                 domain={'x': [0, 1], 'y': [0, 1]},
                                 title={'text': gauge_label},
                                 gauge={'axis': {'range': [0, 1]}, 'bar': {'color': color}, 'bgcolor': 'black'}))
    return fig
