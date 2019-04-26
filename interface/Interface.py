from tkinter import *
from tkinter import messagebox

page = Tk()
page.title("ScoreScanner")
page.geometry("500x500")
page.resizable(0, 0)
page.iconbitmap("icon-ss.ico")
page.config(bg = "paleturquoise")

#datos de prueba
autores = [["001", "Ludwig Van Beethoven", "138"],
["002", "Wolfang Amadeus Mozart", "626"],
["003", "Johann Sebastian Bach", "1128"]]

#creación de campos
labelautores = Label(page, text = "A U T O R E S", bg = "paleturquoise")
labelautores.place(x =150 , y =50 , width = 200, height = 20)
#id
labelcod = Label(page, text = "ID", bg = "paleturquoise")
labelcod.place(x = 50, y = 90, width = 150, height = 20)
campocod = Entry(page, bg = "whitesmoke", fg = "cadetblue")
campocod.place(x = 170, y = 90, width = 200, height = 20)

#nombre
labelnom = Label(page, text = "Nombre", bg = "paleturquoise")
labelnom.place(x = 50, y = 130, width = 150, height = 20)
camponom = Entry(page, bg = "whitesmoke", fg = "cadetblue")
camponom.place(x = 170, y = 130, width = 200, height = 20)

#obras
labelobras = Label(page, text = "Obras", bg = "paleturquoise")
labelobras.place(x = 50, y = 170, width = 150, height = 20)
campoobras = Entry(page, bg = "whitesmoke", fg = "cadetblue")
campoobras.place(x = 170, y = 170, width = 200, height = 20)

#eventos de botones
#buscar
def btnbuscar():
    for i in range(len(autores)):
        for j in range(len(autores[i])):
            if autores[i][j] == campocod.get():
                busqueda = "ID: " + autores[i][0] + "\nNombre: " + autores[i][1] + "\nObras: " + autores[i][2]
                messagebox.showinfo("Resultado de búsqueda", busqueda)
                break
            else:
                if campocod.get() == "":
                    messagebox.showwarning("Cuidado", "Inserte un código para buscar.")
                    break
                else:
                    messagebox.showerror("Error", "No se encontró el autor.")
                    break
        break

#creacion de botones
botonbuscar = Button(page, text = "Buscar", command = btnbuscar, bg = "lightseagreen", activebackground = "cadetblue")
botonbuscar.place(x = 140, y = 210, width = 100, height = 40)
botonregistrar = Button(page, text = "Registrar", bg = "lightseagreen", activebackground = "cadetblue")
botonregistrar.place(x = 260, y = 210, width = 100, height = 40)

page.mainloop()