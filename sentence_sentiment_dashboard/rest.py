"""dashboard api"""

import dash
from dash import html, dcc
import numpy as np
from plotly import graph_objs as go

app = dash.Dash()

app.layout = html.Div(id='outer-div', children=[], style={'border':'solid 5px black'})

if __name__ == "__main__":
    app.run_server(debug=True)
