import tkgui.gui
import tkgui.logging
import logging


def main():
    rw = tkgui.gui.createGui()
    rw.mainloop()


if __name__ == "__main__":
    tkgui.logging.configureLogging()
    main()
    logging.debug("exiting")
