# Project Maximus by Alex Arbuckle #


import dash
from json import load
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


with open('Maximus.json', 'r') as fileVariable:
    
    style = load(fileVariable)


version = "1.000"
app = dash.Dash()
server = app.server
app.layout = html.Div([
    
    html.Div([
        
        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = False,
                              id = 'booleanSwitchIdA')
            
        ], style = style['divDivDivStyleLeft']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = True,
                              id = 'booleanSwitchIdB')

        ], style = style['divDivDivStyleLeft']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = False,
                              id = 'booleanSwitchIdC')

        ], style = style['divDivDivStyleLeft']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              vertical = True,
                              disabled = True,
                              id = 'booleanSwitchIdD')

        ], style = style['divDivDivStyleLeft']),
        
    ], style = style['divDivStyleLeft']),
    
    html.Div([
        
        html.Div([
            
            dcc.Tabs(id = 'tabsId',
                     value = 'mapValue',
                     children = [
                         
                         dcc.Tab(label = 'Map',
                                 value = 'mapValue',
                                 style = style['tabStyle'],
                                 selected_style = style['tabSelectedStyle']),
                         
                         dcc.Tab(label = 'Camera',
                                 value = 'cameraValue',
                                 style = style['tabStyle'],
                                 selected_style = style['tabSelectedStyle'])
                         
                     ])
            
        ], style = style['divDivDivStyleRight'])
        
    ], style = style['divDivStyleRight'])
    
])


@app.callback(Output('booleanSwitchIdB', 'disabled'),
              Input('booleanSwitchIdA', 'on'))
def booleanSwitchFunctionA(arg):
    '''  '''
    
    return False if (arg is True) else True


@app.callback(Output('booleanSwitchIdD', 'disabled'),
              Input('booleanSwitchIdC', 'on'))
def booleanSwitchFunctionB(arg):
    '''  '''
    
    return False if (arg is True) else True


if (__name__ == '__main__'):

    app.run_server(debug = True)