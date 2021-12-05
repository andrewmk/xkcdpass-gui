import PySimpleGUI as sg

import os
import sys
import tkinter

from xkcdpass import xkcd_password as xp

def gen_password():
    # create a wordlist from the default wordfile
    # use words between 5 and 8 letters long
    wordfile = xp.locate_wordfile(resource_path('eff-long'))
    mywords = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)
    passwords = xp.generate_xkcdpassword(mywords, numwords=4)
    password_list = passwords.split(' ')
    window['-out-'].update(''.join(password_list))
    for i in range(4):
        window[f'-{i + 1}-'].update(password_list[i])

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Col to provide vertical space
def C(h=80):
    return [sg.Col(layout=[[]], s=(None, h))]

# Input box for a word or words
def W(k, fs=20, w=20, just='left'):
    return [sg.Input(k=f'-{k}-', p=0, s=w, font=f'Courier {fs}', justification=just)],

layout = [
    C(),
    [sg.Text('XKCD Password Generator', k='-TITLE-', p=0, s=30, font='Courier 20', justification='centre')],
]

for i in (1, 2, 3, 4):
    layout += [C(), W(i)]

layout += [
    C(h=100),
    W('out', fs=18, w=32, just='centre'),
    C(h=60),
    [sg.Button('Generate', k='-GEN-', p=0, button_color='white on red')]
]

window = sg.Window('XKCD password generator', layout, element_justification='centre', size=(870, 1028), finalize=True)

# Insert background image via tinter
filename = tkinter.PhotoImage(file = resource_path('battery.png'))
background_label = tkinter.Label(window.TKroot, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Cover everything with image
background_label.lift()

# Raise UI to be visible again
window['-TITLE-'].ParentRowFrame.lift()
for i in (1, 2, 3, 4):
    window[f'-{i}-'].ParentRowFrame.lift()
window['-out-'].ParentRowFrame.lift()
window['-GEN-'].ParentRowFrame.lift()

gen_password()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-GEN-':
        gen_password()

window.close()
