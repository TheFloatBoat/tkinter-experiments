import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Printer')
ttk.Label(window, text = "input text here").pack()#makes and shows label

usersBS = tk.StringVar(window)
stb = ttk.Entry(window, textvariable=usersBS).pack()

ttk.Button(text = "click me to print the text!", command=lambda:print(usersBS.get())).pack()#shows buttoff
window.mainloop()#shows window
