import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("SELAMAT DATANG DI KELAS",font=("Arial",25))],
                            [sg.Text("NPM   : 2210010436 ")],
                            [sg.Text("Nama  : Josua Valentino B ")],
                            [sg.Text("Kelas : 5N Regular Banjarmasin ")]],
                    size=(500,200),
                    font=("Times", 18))
window()
window.close()