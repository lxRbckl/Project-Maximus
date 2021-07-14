# Project Maximus by Alex Arbuckle #


import dash
from json import load
import dash_daq as daq
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


with open('Maximus.json', 'r') as fileVariable:
    
    style = load(fileVariable)


app = dash.Dash(suppress_callback_exceptions = True)
server = app.server
app.layout = html.Div([

    html.Div([
        
        html.H4('All', style = style['h4Style']),
        
        html.Div([
            
            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = False,
                              id = 'booleanSwitchIdA')
            
        ], style = style['divDivDivStyleLeft']),
        
        html.H4('Front', style = style['h4Style']),
        
        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = False,
                              id = 'booleanSwitchIdB')
            
        ], style = style['divDivDivStyleLeft']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = True,
                              id = 'booleanSwitchIdC')

        ], style = style['divDivDivStyleLeft']),
        
        html.H4('Rear', style = style['h4Style']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = False,
                              id = 'booleanSwitchIdD')

        ], style = style['divDivDivStyleLeft']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = True,
                              id = 'booleanSwitchIdE')

        ], style = style['divDivDivStyleLeft']),
        
    ], style = style['divDivStyleLeft']),
    
    html.Div([
        
        html.Div([
            
            dcc.Tabs(id = 'tabsId',
                     value = 'graphValue',
                     children = [
                         
                         dcc.Tab(label = 'Map',
                                 value = 'graphValue',
                                 style = style['tabStyle'],
                                 selected_style = style['tabSelectedStyle']),
                         
                         dcc.Tab(label = 'Camera',
                                 value = 'cameraValue',
                                 style = style['tabStyle'],
                                 selected_style = style['tabSelectedStyle'])
                         
                     ]),
                        
        ], style = style['divDivDivStyleRight']),

        html.Div(id='divDivDivId')

    ], style = style['divDivStyleRight'])
    
])


@app.callback(Output('booleanSwitchIdC', 'disabled'),
              Input('booleanSwitchIdB', 'on'))
def booleanSwitchFunctionA(arg):
    '''  '''
    
    return False if (arg is True) else True


@app.callback(Output('booleanSwitchIdE', 'disabled'),
              Input('booleanSwitchIdD', 'on'))
def booleanSwitchFunctionB(arg):
    '''  '''
    
    return False if (arg is True) else True


@app.callback(Output('divDivDivId', 'children'),
              Input('tabsId', 'value'))
def tabsFunction(arg):
    '''  '''

    dictVariable = {'graphValue' : functionGraph(),
                    'cameraValue' : functionCamera()}

    return dictVariable[arg]


def functionGraph():
    '''  '''

    return html.Div([

        html.Div([

            dcc.Graph(id = 'graphId',
                      style = style['graphStyle'],
                      config = style['graphConfig']),

            dcc.Interval(id = 'intervalId')

        ], style = style['divDivDivStyleRight'])

    ])


@app.callback(Output('graphId', 'figure'),
              Input('intervalId', 'n_intervals'))
def intervalGraph(arg):
    '''  '''

    #global style
    #style['layoutMapbox']['center']['lat'] += 1

    # checkpoint
    # fix redundancy above with a for loop,
    # and a nested data structure.
    # this segment works, we now need to build
    # the GPS algorithm to update the variables.
    # from there we can move to push this offline
    # and hopefully find a dark-theme version.

    return {'data' : [go.Scattermapbox()

    ],

    'layout' : go.Layout(

        uirevision = 'foo',
        margin = style['layoutMargin'],
        mapbox = style['layoutMapbox'],
        mapbox_style = 'open-street-map')

    }


def functionCamera():
    '''  '''

    pass


if (__name__ == '__main__'):

    app.run_server(debug = True)
