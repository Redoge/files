import PySimpleGUI as sg
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


layout = [
    [sg.Text('Введіть числа: '), sg.Input(key='first',size=(15,1)), sg.Input(key='second',size=(15,1)), sg.Button('Рахувати')],
    [sg.Text('_'  * 100, size=(50, 1))], 
    [sg.Text('a + b ', size=(25,1), key = "plus"), sg.Text('a - b ',size=(25,1), key = "minus")],
    [sg.Text('_'  * 100, size=(50, 1))], 
    [sg.Text('a * b ',size=(25,1), key = "mn"), sg.Text('a / b ',size=(25,1), key = "dil")],
    [sg.Text('_'  * 100, size=(50, 1))], 
    [sg.Text('sqrt(a) ',size=(25,1), key = "sqra"), sg.Text('sqrt(b) ',size=(25,1), key = "sqrb")],
    [sg.Text('_'  * 100, size=(50, 1))], 
    [sg.Text('a**2 ',size=(25,1), key = "a**2"), sg.Text('b**2 ',size=(25,1), key = "b**2")],
    [sg.Text('_'  * 100, size=(50, 1))], 
    [sg.Button('Exit')],
]   

sg.theme('Noon') 
window = sg.Window('Calculator', layout)


while True:                         
    event, values = window.read()
    if event in (None, 'Exit'):
        break   
    print(event, values) #debug
    window['plus'].update(f"a + b = {float(values['first']) + float(values['second'])}")
    window['minus'].update(f"a - b = {float(values['first']) - float(values['second'])}")
    window['mn'].update(f"a * b = {float(values['first']) * float(values['second'])}")
    if values['second'] != '0': window['dil'].update(f"a / b = {float(values['first']) / float(values['second'])}")
    else: window['dil'].update(f"a / b => Error (b = 0)")
    window['sqra'].update(f"sqrt(a) = {float(values['first'])**(1/2)}")
    window['sqrb'].update(f"sqrt(a) = {float(values['second'])**(1/2)}")
    window['a**2'].update(f"a^2 = {float(values['first'])**2}")
    window['b**2'].update(f"b^2 = {float(values['second'])**2}")
