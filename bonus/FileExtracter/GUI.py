import PySimpleGUI as sg
import time
from zip_extractor import extract_archive

sg.theme("LightBlue7")

clock = sg.Text("", key="clock")
label1 = sg.Text("Select Archives: ")
input1 = sg.Input()
choose_button1 = sg.Button("Choose", key="archive")

label2 = sg.Text("Select destination directory: ")
input2 = sg.Input()
choose_button2 = sg.Button("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")


window = sg.Window("Archive Extractor",
                   layout=[[clock],
                           [label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]
                           ]
                   ,
                    font =("Helvetica", 15))
while True:
    event, values = window.read()
    archivepath= values["archive"]
    dest_dir = values["folder"]
    GUI.extract_archives(archivepath, dest_dir)

window.close()

