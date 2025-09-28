print("importing tkgui/main")

import tkinter as tk
from tkinter import Menu
from tkgui.pensieve import getConfig, saveFcts


def createGui() -> tk.Tk:
    root = tk.Tk()
    mainMenu = Menu(root)
    fileMenu = Menu(mainMenu, tearoff=0)
    fileMenu.add_command(label="Exit", underline=1, command=root.quit)
    mainMenu.add_cascade(label="File", underline=0, menu=fileMenu)
    root.config(menu=mainMenu)
    cfg = getConfig()
    if hasattr(cfg, "geometry"):
        root.geometry(cfg.geometry)

    def saveFct():
        print("saving geometry")
        cfg.geometry = root.geometry()

    saveFcts.add(saveFct)
    return root
