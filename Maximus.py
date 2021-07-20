# Project Maximus by Alex Arbuckle #


import dash
from json import load
from time import sleep
import dash_daq as daq
import RPi.GPIO as GPIO
import dash_html_components as html
from dash.dependencies import Input, Output


front, rear = False, False
with open('Maximus.json', 'r') as fileVariable:
    
    style = load(fileVariable)


app = dash.Dash()
server = app.server
GPIO.setmode(GPIO.BOARD)
GPIO.setup(style['GPIO']['Accessory'], GPIO.OUT)
GPIO.output(style['GPIO']['Accessory'], True)
GPIO.setup(style['GPIO']['Front'], GPIO.OUT)
GPIO.setup(style['GPIO']['Rear'], GPIO.OUT)
app.layout = html.Div([

    html.Div([

        html.Div([

            daq.BooleanSwitch(on = False,
                              disabled = False,
                              id = 'booleanSwitchIdA')
            
        ], style = style['divDivDivStyle']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              disabled = True,
                              id = 'booleanSwitchIdB')

        ], style = style['divDivDivStyle']),

        html.H1(''),

        html.Div([

            daq.BooleanSwitch(on = False,
                              disabled = False,
                              id = 'booleanSwitchIdC')

        ], style = style['divDivDivStyle']),

        html.Div([

            daq.BooleanSwitch(on = False,
                              disabled = True,
                              id = 'booleanSwitchIdD')

        ], style = style['divDivDivStyle']),
        
    ], style = style['divDivStyle']),

])


@app.callback(Output('booleanSwitchIdA', 'children'),
              Input('booleanSwitchIdA', 'on'))
def booleanSwitchFunctionA(arg):
    '''  '''

    GPIO.output(style['GPIO']['Front'], arg)


@app.callback(Output('booleanSwitchIdB', 'children'),
              Input('booleanSwitchIdB', 'on'))
def booleanSwitchFunctionB(arg):
    ''' #GPIO.output(37, True) '''

    global front

    front = arg
    while (front):

        sleep(0.25)
        GPIO.output(style['GPIO']['Front'], True)
        sleep(0.25)
        GPIO.output(style['GPIO']['Front'], False)


@app.callback(Output('booleanSwitchIdC', 'children'),
              Input('booleanSwitchIdC', 'on'))
def booleanSwitchFunctionC(arg):
    '''  '''

    GPIO.output(style['GPIO']['Rear'], arg)


@app.callback(Output('booleanSwitchIdD', 'children'),
              Input('booleanSwitchIdD', 'on'))
def booleanSwitchFunctionD(arg):
    ''' #GPIO.output(38, True) '''

    global rear

    rear = arg
    while (rear):

        sleep(0.25)
        GPIO.output(style['GPIO']['Rear'], True)
        sleep(0.25)
        GPIO.output(style['GPIO']['Rear'], False)


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
