import tkinter as tk

import main
from main import *

#main = Tk()


window = tk.Tk()
window.geometry("900x550")
window.title("Progetto Python")
window.grid_columnconfigure(0, weight=1)

#window.mainloop()

def print():
    if text_imput_start.get() and text_imput_end.get():
        user_input_start = text_imput_start.get()
        user_input_end = text_imput_end.get()

        text_response = main.avvia(user_input_start, user_input_end)
    else:
        text_response = "Completa i campi"

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=6, column=0, sticky="WE")

    credits_label = tk.Label(window, text="Progetto Python by Salvatore La Rosa and Matteo Tiboldo")
    credits_label.grid(row=9, column=0, sticky="S", pady=10)

welcome_label = tk.Label(window,text = "Inserisci laaa parola con cui vuoi iniziare e quella con cui vuoi terminare",pady=10,font=("Helvetica", 15))
welcome_label.grid(row=0, column=1, sticky="N", padx=20, pady=10)

text_parola1 = tk.Label(window,text = "Parola1",pady=10,font=("Helvetica", 15))
text_parola1.grid(row=1, column=1, sticky="WE", padx=20, pady=20)

text_imput_start = tk.Entry()
text_imput_start.grid(row=1, column=2, sticky="WE", padx=20,pady=20)

text_imput_end = tk.Entry()
text_imput_end.grid(row=2, column=1, sticky="WE", padx=20,pady=20)

button = tk.Button(text="Avvia", command=print)
button.grid(row=4, column=1, sticky="WE", pady=10, padx=20)

window.mainloop()

