import tkinter as tk
from PIL import Image, ImageTk

class Character:
    def __init__(self, name, actor, charpic, actorpic):
        self.name = name
        self.actor = actor
        self.charpic = Image.open(charpic)
        self.actorpic = Image.open(actorpic)

keyleth = Character('Keyleth', 'Marisha Ray',
                        'characters/pc/Keyleth/Keyleth2.png',
                        'characters/pc/Keyleth/Ray.jpg')

print(keyleth.actorpic.size)
print(keyleth.charpic.size)

master = tk.Tk()

char = tk.Label(master, image=ImageTk.PhotoImage(keyleth.charpic))
char.pack()

master.mainloop()
exit()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.initUI()

    def initUI(self):
        self.master.title("Critrole-Faces - ")

        char = tk.Label(self, image=ImageTk.PhotoImage(keyleth.charpic))
        char.image = keyleth.charpic #necessary?

        char.pack()
        self.pack()

    def setgeometry(self):
        w, h = keyleth.charpic.size
        self.master.geometry("{}x{}+300+300".format(w, h))
        

def main():
    root = tk.Tk()
    app = Application()
    app.setgeometry()
    root.mainloop()

if __name__ == '__main__':
    main()
