import PySimpleGUI as sg

import tkinter
from xkcdpass import xkcd_password as xp

layout = [
    [sg.Col(layout=[[]], s=(None, 80))],
    [sg.Text('XKCD Password Generator', k='-TITLE-', p=0, s=30, font='Courier 20', justification='centre')],
    [sg.Col(layout=[[]], s=(None, 80))],
    [sg.Input(k='-1-', p=0, s=20, font='Courier 20')],
    [sg.Col(layout=[[]], s=(None, 80))],
    [sg.Input(k='-2-', p=0, s=20, font='Courier 20')],
    [sg.Col(layout=[[]], s=(None, 80))],
    [sg.Input(k='-3-', p=0, s=20, font='Courier 20')],
    [sg.Col(layout=[[]], s=(None, 80))],
    [sg.Input(k='-4-', p=0, s=20, font='Courier 20')],
    [sg.Col(layout=[[]], s=(None, 100))],
    [sg.Input(k='-out-', p=0, s=40, font='Courier 16', justification='centre')],
    [sg.Col(layout=[[]], s=(None, 60))],

    [sg.Button('Generate', k='-GEN-', p=0, button_color='white on red')]
]

window = sg.Window('XKCD password generator', layout, element_justification='centre', size=(870, 1028), finalize=True)

# Insert background image via tinter
filename = tkinter.PhotoImage(file = "battery.png")
background_label = tkinter.Label(window.TKroot, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Cover everything with image
background_label.lift()
# Make UI visible again above image
window['-TITLE-'].ParentRowFrame.lift()
window['-1-'].ParentRowFrame.lift()
window['-2-'].ParentRowFrame.lift()
window['-3-'].ParentRowFrame.lift()
window['-4-'].ParentRowFrame.lift()
window['-out-'].ParentRowFrame.lift()
window['-GEN-'].ParentRowFrame.lift()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-GEN-':
        # create a wordlist from the default wordfile
        # use words between 5 and 8 letters long
        wordfile = xp.locate_wordfile()
        mywords = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)
        passwords = xp.generate_xkcdpassword(mywords, numwords=4)
        password_list = passwords.split(' ')
        window['-out-'].update(''.join(password_list))
        for i in range(4):
            window[f'-{i + 1}-'].update(password_list[i])
