import PySimpleGUI as sg
window = sg.Window(title="Latihan Pertama", layout=[[sg.Text("NPM   :2210010436")],
                                                    [sg.Text("NAMA  :Josua Valentino")],
                                                    [sg.Text("KELAS :5N REG PAGI")],
                                                    [sg.Text("MATKUL:PEMROGRAMAN VISUAL 3")]] , size=(400,200))
window()
window.close()