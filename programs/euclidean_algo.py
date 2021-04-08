import PySimpleGUI as sg
import time
noon = {'BACKGROUND': '#709053',
                'TEXT': '#fff4c9',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('white', '#709053'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 0.5,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}
sg.theme_add_new('Noon', noon)
sg.theme('Noon')
def nsd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a 
    return a
layout = [
    [sg.Text('НСД('), sg.Input(key = 'a', size = (15, 1)), sg.Text(', '),sg.Input(key = 'b', size = (15, 1)), sg.Text(')')],
    [sg.Button('Знайти НСД'),  sg.Text('НСД:'),sg.Text(size=(15, 1),key='out')],
    [sg.Button('Exit')]
]   

sg.theme('Noon') 
window = sg.Window('Алгоритм Евкліда (НСД)', layout)


while True:                            
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    print(event, values) #debug
    start_time = time.time() 
    window['out'].update(str(nsd(int(values['a']), int(values['b']))))
    times = (time.time() - start_time) #for test
    sg.popup('Times: ', str(times)+ ' c')

  
