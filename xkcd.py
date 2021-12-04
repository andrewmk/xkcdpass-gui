import PySimpleGUI as sg
import tkinter

layout = [
#    [sg.Col(layout=[
    [sg.Input(key='line1', pad=(0, (120, 60)), size=20, font='Courier 20')],
    [sg.Input(key='line1', pad=(0, 60), size=20, font='Courier 20')],
    [sg.Input(key='line1', pad=(0, 60), size=20, font='Courier 20')],
    [sg.Input(key='line1', pad=(0, (60, 120)), size=20, font='Courier 20')],

    [sg.Button('Generate')]
#    ], justification='centre')]
]

window = sg.Window('XKCD password generator', layout, element_justification='centre', size=(880, 1048), finalize=True, resizable=True, transparent_color='red', background_color='red')

filename = tkinter.PhotoImage(file = "battery.png")
background_label = tkinter.Label(window.TKroot, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()


event, values = window.read(close=True)
print(event, values)
