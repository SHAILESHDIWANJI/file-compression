import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog

def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title="select a dialogue box")
    return filename
def compession(i,o):
    compreess(i,o)


 

window =tk.Tk()
window.title("compession engine")
window.geometry("600x400")

compress_button=tk.Button(window,text="compress",command=lambda:compress(open_file(),"comprees_output.txt()"))



compress_button.grid(row=2,column=1)


window.mainloop()
