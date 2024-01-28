import tkinter as tk
import tkinter.ttk as ttk
from dispatcher import dispatcher
from frames import *


root = tk.Tk()
root.title = "Catman Sys"


root.geometry("960x640")
root.minsize(width=960, height=640)
# root.attributes('-fullscreen', True)

ttk.Style().configure('TButton', font=("Arial", 14))
ttk.Style().configure('TLabel', font=("Arial", 24))
ttk.Style().configure("Treeview", font=("Arial", 12), relief="solid", borderwidth=1)
ttk.Style().configure("Treeview.Heading", font=("Arial", 12))

dispatcher(root, "/login")

root.mainloop()
