from tkinter import *
from tkinter import messagebox

page = Tk()
page.title("ScoreScanner")
page.geometry("500x570")
page.resizable(0, 0)
page.iconbitmap("icon-ss.ico")
page.config(bg = "paleturquoise")

#creación de campos
lblinicio = Label(page, text = "Bienvenido a ScoreScanner", bg = "paleturquoise", font = ("Times", 20))
lblinicio.place(x =50 , y =180 , width = 400, height = 60)

#imagen
#logo
logo = PhotoImage(file = "iconhome.gif")
lbllogo = Label(page, image = logo)
lbllogo.place(x = 175, y = 20, width = 150, height = 150)
#partitura
partitura = PhotoImage(file = "partitura.gif")
lblpartitura = Label(page, image = partitura)

#adjuntar partitura luego de darle click al botón
def adjuntar():
    lblpartitura.place(x = 50, y = 290, width = 400, height = 270)

#creación de botones
#adjuntar
btnadjuntar = Button(page, text = "Adjuntar foto", command = adjuntar, bg = "lightseagreen", activebackground = "cadetblue")
btnadjuntar.place(x = 200, y = 250, width = 100, height = 30)

page.mainloop()