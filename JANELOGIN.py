from tkinter import *

loginWindow = Tk()
loginWindow.title("LOGIN USUÁRIO")
loginWindow["bg"] = "#c9f0c0"
loginWindow.geometry("640x480+363+144")

lb = Label(loginWindow, text = "MINILAB NORDESTE - CADASTRO DE CLIENTES E EQUIPAMENTOS", font = 1)
lb.place(x = 55, y = 40)
lb["bg"] = "#c9f0c0"

USLAbel = Label(loginWindow, text = "USUÁRIO", font = 1)
USLAbel.place(x = 280,y = 100)
USLAbel["bg"] = "#c9f0c0"

PWLAbel = Label(loginWindow, text = "SENHA", font = 1)
PWLAbel.place(x = 290,y = 240)
PWLAbel["bg"] = "#c9f0c0"

bt = Button(loginWindow, width = 20, height = 2, text = "ENTRAR")
bt.place(x = 225, y = 385)

loginWindow.mainloop()
