"""
 Author : Duvan Mejia
 Date : Wednesday, December 17
"""
import tkinter


def ok():
    texto['text'] = "Good Luck!"


principal = tkinter.Tk()
principal.wm_title("Speak 5 lines to YOURSELF Every Morning")
texto = tkinter.Label(principal, text="1. I am the Best.")
texto1 = tkinter.Label(principal, text="2. I Can do it.")
texto2 = tkinter.Label(principal, text="3. God is always with Me.")
texto3 = tkinter.Label(principal, text="4. I am a Winner.")
texto4 = tkinter.Label(principal, text="5. Today is my Day.")

boton_ok = tkinter.Button(principal, text="Ok", command=ok)

texto.pack()
texto1.pack()
texto2.pack()
texto3.pack()
texto4.pack()
boton_ok.pack()

principal.mainloop()
