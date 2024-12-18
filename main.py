from tkinter import *
from ui import Interface

class App:
    def __init__(self):
        self.window = Tk()
        self.ui = None

    def start_app(self):
        self.ui = Interface(self.window)
        self.window.mainloop()


if __name__ == '__main__':
    app = App()
    app.start_app()
