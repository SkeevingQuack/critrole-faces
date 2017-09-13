import tkinter as tk
from PIL import Image, ImageTk

class CritroleFaces(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.init()

    def init(self):
        self.master.title("Critrole-Faces - ")
        self.pack(fill=tk.BOTH, expand=1)
        

def main():
    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = CritroleFaces()
    root.mainloop()

if __name__ == '__main__':
    main()
