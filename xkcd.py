import PySimpleGUI as sg

import tkinter
from xkcdpass import xkcd_password as xp

def C(height):
    return [sg.Col(layout=[[]], s=(None, height))]

def W(k, fs=20, w=20, just='left'):
    return [sg.Input(k=f'-{k}-', p=0, s=w, font=f'Courier {fs}', justification=just)],

layout = [
    C(80),
    [sg.Text('XKCD Password Generator', k='-TITLE-', p=0, s=30, font='Courier 20', justification='centre')],
    C(80),
    W(1),
    C(80),
    W(2),
    C(80),
    W(3),
    C(80),
    W(4),
    C(100),
    W('out', fs=18, w=32, just='centre'),
    C(60),
    [sg.Button('Generate', k='-GEN-', p=0, button_color='white on red')]
]

window = sg.Window('XKCD password generator', layout, element_justification='centre', size=(870, 1028), finalize=True)

# Insert background image via tinter
filename = tkinter.PhotoImage(file = "battery.png")
background_label = tkinter.Label(window.TKroot, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lift()

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

window.close()
