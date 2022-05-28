import PySimpleGUI as sg

image_col = sg.Column()
info_col = sg.Column([
    [sg.Text('', key = '-LOCATION-', font='Calibri 30', background_color= '#FF0000', pad = 0, visible = False)],
    [sg.Text('', key = '-TIME-', font = 'Calibri 16',  background_color = '#0000', text_color = '#FFFFFF', pad = 0, visible = False)],
    [sg.Text('', key = '-TEMP-', font = 'Calibri 16', pad = (0,10), background_color = '#FFFFFF', text_color="#00000", visible = False)]
])
layout = [
    [sg.Input(expand_x=True, key = 'INPUT'), sg.Button('Enter')],
    [image_col,info_col]
    ]

window = sg.Window('Tempo',  layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()