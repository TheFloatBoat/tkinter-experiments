import tkinter as tk
from tkinter import filedialog

def openfile():
  filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
  if not filepath:
    return
  txt_editor.delete("1.0", tk.END)
  with open(filepath, mode="r", encoding="utf-8") as input_file:
    text=input_file.read()
    txt_editor.insert(tk.END, text)
  window.title(f"Text Editor - {filepath}")
def saveAs():
  filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
  if not filepath:
    return
  with open(filepath, mode="w", encoding="utf-8") as output_file:
    text = txt_editor.get("1.0", tk.END)
    output_file.write(text)
  window.title(f"Text Editor - {filepath}")
window = tk.Tk()
window.columnconfigure([0,1],weight=1)
window.rowconfigure([0,1],weight=1)
window.title("Text Editor")

frm_buttons = tk.Frame()
btn_open = tk.Button(text="open", command=openfile, master=frm_buttons)
btn_saveAs = tk.Button(text="save as", command=saveAs, master=frm_buttons)
txt_editor = tk.Text()

btn_open.grid(row=0,column=0,sticky="nsew")
btn_saveAs.grid(row=1, column=0, sticky="nsew")
frm_buttons.grid(row=0,column=0,sticky="nsew")
txt_editor.grid(row=0,column=1,sticky="nsew")

window.mainloop()
