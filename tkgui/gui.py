import tkinter as tk
from tkinter import Menu

# import pensieve

print("importing tkgui/main")


def createGui() -> tk.Tk:
    root = tk.Tk()
    mainMenu = Menu(root)
    fileMenu = Menu(mainMenu, tearoff=0)
    fileMenu.add_command(label="Exit", underline=1, command=root.quit)
    mainMenu.add_cascade(label="File", underline=0, menu=fileMenu)
    root.config(menu=mainMenu)
    return root
