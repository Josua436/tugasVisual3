import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#ffff00")
window = sg.Window(title="Profile",
        layout=[[sg.Text("FAKULTAS TEKNOLOGI INFORMASI",size=(25,1),justification="center")],
                [sg.Text("FAKULTAS TEKNOLOGI INFORMASI",size=(25,1),justification="left")],
                [sg.Text("FAKULTAS TEKNOLOGI INFORMASI",size=(25,1),justification="right")],
                [sg.Text("FAKULTAS TEKNOLOGI INFORMASI"+" "* 2,size=(25,2),justification="center")],
                [sg.Text("UNISKA MAB BANJARMASIN",text_color="#FFCC00")]],
        size=(450,250),
        font=("Times",18))
window()
window.close()