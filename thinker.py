import tkinter
def saludar():
    texto['text'] = "Hola Amigo"

def despedir():
    texto['text'] = "Hasta La vista"

principal = tkinter.Tk()
principal.wm_title("programilla")
texto = tkinter.Label(principal, text="saludar")

boton_saluda = tkinter.Button(principal, text="Hola", command=saludar)
boton_despide = tkinter.Button(principal, text="Adios", command=despedir)

texto.pack()
boton_saluda.pack()
boton_despide.pack()

principal.mainloop()
