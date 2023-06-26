"""dashboard api"""

import dash
from dash import html, dcc
import numpy as np
from plotly import graph_objs as go

app = dash.Dash()

app.layout = html.Div(id='outer-div', children=[html.H2('Please Enter the Sentence here: ',
                                                        style={'color': 'red',
                                                               'font-family': 'tahoma'}),
                                                dcc.Input(id='text-input', style={'height': '30px', 'width': '50%',
                                                                                  'border': 'Solid 5px Black',
                                                                                  'border-radius': '5px'}),
                                                html.Hr(),
                                                html.Button('PREDICT', id='btn-nclicks-1'),
                                                html.Hr(),
                                                html.Div(id='graphs-div', children=[dcc.Graph(id='gauge',
                                                                                              style={'float': 'left',
                                                                                                     'align': 'left',
                                                                                                     'width': '48%',
                                                                                                     'border': 'Solid 5px Black',
                                                                                                     'border-radius': '5px'}),
                                                                                    dcc.Graph(id='bar',
                                                                                              style={'float': 'right',
                                                                                                     'align': 'right',
                                                                                                     'width': '48%',
                                                                                                     'border': 'Solid 5px Black',
                                                                                                     'border-radius': '5px'})
                                                                                    ])
                                                ])

if __name__ == "__main__":
    app.run_server(debug=True)
