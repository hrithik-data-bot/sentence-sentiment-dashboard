"""dashboard api"""

# pylint: disable=import-error

import dash
from dash import html, dcc, Input, Output, State
import numpy as np
from plotly import graph_objs as go
from model_utils_nltk import prediction_pipeline

GAUGE_STYLE = {'float':'left', 'align':'left', 'width':'48%',
               'border':'Solid 5px Black', 'border-radius':'5px'}
BAR_STYLE = {'float':'right', 'align':'right', 'width':'48%',
             'border':'Solid 5px Black', 'border-radius':'5px'}

app = dash.Dash()

app.layout = html.Div(id='outer-div', children=[html.H2('Please Enter the Sentence here: ',
                                                        style={'color': 'red',
                                                               'font-family': 'tahoma'}),
                                                dcc.Input(id='text-input',
                                                          value='I love this movie..!',
                                                          style={'height': '30px',
                                                                 'width': '50%',
                                                                 'border': 'Solid 5px Black',
                                                                 'border-radius': '5px'}),
                                                html.Hr(),
                                                html.Button('PREDICT', id='predict-button'),
                                                html.Hr(),
                                                html.Div(id='graphs-div',
                                                         children=[dcc.Graph(id='gauge',
                                                                             style=GAUGE_STYLE),
                                                                    dcc.Graph(id='bar',
                                                                              style=BAR_STYLE)
                                                                                    ])
                                                ])


@app.callback(Output('gauge', 'figure'),
              Input('predict-button', 'n_clicks'),
              State('text-input', 'value'))
def create_gauge(n_clicks, sentence: str): # pylint: disable=unused-argument

    """create a gauge chart"""

    prediction_data = prediction_pipeline(text=sentence)
    labels = np.array(list(prediction_data.keys()))
    scores = np.array(list(prediction_data.values()))
    gauge_max_values = np.argmax(scores)
    gauge_label, gauge_value = labels[gauge_max_values].upper(), scores[gauge_max_values]
    if gauge_label == 'POS':
        color = 'green'
    elif gauge_label == 'NEG':
        color = 'red'
    elif gauge_label == 'NEU':
        color = 'yellow'
    fig = go.Figure(go.Indicator(mode="gauge+number",
                                 value=gauge_value,
                                 domain={'x': [0, 1], 'y': [0, 1]},
                                 title = {'text': gauge_label},
                                 gauge={'axis': {'range': [0, 1]},
                                        'bar': {'color': color},
                                        'bgcolor':'black'}))
    return fig


@app.callback(Output('bar', 'figure'),
              Input('predict-button', 'n_clicks'),
              State('text-input', 'value'))
def create_bar(n_clicks, sentence: str): # pylint: disable=unused-argument
    """create a bar chart"""

    prediction_data = prediction_pipeline(text=sentence)
    labels = np.array(list(prediction_data.keys()))
    scores = np.array(list(prediction_data.values()))

    data = go.Bar(x=labels, y=scores)
    layout = go.Layout(title='Sentiment Score Bar Plot',
                       xaxis=dict(title='Sentiment'),
                       yaxis=dict(title='Score'))
    fig = go.Figure(data=[data], layout=layout)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
