import PySimpleGUI as sg
from functions import *

layoutPrincipal = [
    [sg.Text('Matriz de intensidades'), sg.Text('I1    '), sg.Text('I2      '), sg.Text('V')],
    [sg.Text('Valores ecuacion 1'), (sg.Input(size=5)), sg.Input(size=5), sg.Input(size=10)],
    [sg.Text('Valores ecuacion 2'), sg.Input(size=5), sg.Input(size=5), sg.Input(size=10)],
    [sg.Button('Calcular'), sg.Button('Cancelar')]
]

window = sg.Window('Calculadora 2x2', layoutPrincipal)

while True:
    event, values = window.read()
    if event in (None, 'Cancelar'):
        break
    if event == 'Calcular':
        IntensityPolar, IntensityComplex = CalcularMatriz(values)
        modal = sg.Window('Resultado',
                          [[sg.Text('Intensidad Compleja 1: '), sg.Text(IntensityComplex[0])],
                           [sg.Text('Intensidad Compleja 2: '), sg.Text(IntensityComplex[1])],
                           [sg.Text('Intensidad Compleja B: '), sg.Text(IntensityComplex[2])],
                           [sg.Text('Intensidad Compleja C: '), sg.Text(IntensityComplex[3])],
                           [sg.Text('Intensidad Compleja N: '), sg.Text(IntensityComplex[4])],
                           [sg.Text('Intensidad a:'), sg.Text(IntensityPolar[0]['Intensidad']), sg.Text('Angulo a:'),
                            sg.Text(IntensityPolar[0]['Angulo'])],
                           [sg.Text('Intensidad b:'), sg.Text(IntensityPolar[2]['Intensidad']), sg.Text('Angulo b:'),
                            sg.Text(IntensityPolar[2]['Angulo'])],
                           [sg.Text('Intensidad c:'), sg.Text(IntensityPolar[3]['Intensidad']), sg.Text('Angulo c:'),
                            sg.Text(IntensityPolar[3]['Angulo'])],
                           [sg.Text('Intensidad n:'), sg.Text(IntensityPolar[4]['Intensidad']), sg.Text('Angulo n:'),
                            sg.Text(IntensityPolar[4]['Angulo'])],
                           [sg.Button('Ok')]])
        event, values = modal.read()
        if event in (None, 'Ok'):
            modal.close()
            break

window.close()
