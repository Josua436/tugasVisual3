import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_colo("#1967D2")
window=sg.Window(title="profile",
                 layout=[[sg.Text("NPM          : 2210010436")],
                         [sg.Text("Nama         : Josua Valentino B")],
                         [sg.Text("Kelas        : 5N Reguler Banjarmasin")],
                         [sg.Text("Matkull      : pempograman Visual 3")]],
                 size=(400,200))
window()
window.close()