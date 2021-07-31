# Project Maximus by Alex Arbuckle #


# Import <
import dash
from json import load
from time import sleep
import dash_daq as daq
import RPi.GPIO as GPIO
import dash_html_components as html
from dash.dependencies import Input, Output

# >


# Declaration <
front, rear = False, False
with open('Maximus.json', 'r') as fileVariable:
    
    style = load(fileVariable)

# >


# Display <
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

        html.H1(style = {'marginBottom' : 120}),

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

# >


# Front Function <
@app.callback(Output('booleanSwitchIdA', 'children'),
              Input('booleanSwitchIdA', 'on'))
def booleanSwitchFunctionA(arg):
    '''  '''

    GPIO.output(style['GPIO']['Front'], arg)

# >


# Emergency Front Function <
@app.callback(Output('booleanSwitchIdB', 'children'),
              Input('booleanSwitchIdB', 'on'))
def booleanSwitchFunctionB(arg):
    '''  '''

    global front

    front = arg
    while (front):

        sleep(0.25)
        GPIO.output(style['GPIO']['Front'], True)
        sleep(0.25)
        GPIO.output(style['GPIO']['Front'], False)

    GPIO.output(style['GPIO']['Rear'], False)

# >


# Rear Function <
@app.callback(Output('booleanSwitchIdC', 'children'),
              Input('booleanSwitchIdC', 'on'))
def booleanSwitchFunctionC(arg):
    '''  '''

    GPIO.output(style['GPIO']['Rear'], arg)


# Emergency Rear Function <
@app.callback(Output('booleanSwitchIdD', 'children'),
              Input('booleanSwitchIdD', 'on'))
def booleanSwitchFunctionD(arg):
    '''  '''

    global rear

    rear = arg
    while (rear):

        sleep(0.25)
        GPIO.output(style['GPIO']['Rear'], True)
        sleep(0.25)
        GPIO.output(style['GPIO']['Rear'], False)

    GPIO.output(style['GPIO']['Rear'], False)

# >


# Front booleanSwitch Function <
@app.callback(Output('booleanSwitchIdB', 'disabled'),
              Input('booleanSwitchIdA', 'on'))
def booleanSwitchFunctionA(arg):
    '''  '''
    
    return False if (arg is True) else True

# >


# Rear booleanSwitch Function <
@app.callback(Output('booleanSwitchIdD', 'disabled'),
              Input('booleanSwitchIdC', 'on'))
def booleanSwitchFunctionB(arg):
    '''  '''
    
    return False if (arg is True) else True

# >


# Main <
if (__name__ == '__main__'):

    app.run_server(debug = True)

# >
