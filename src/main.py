import tkinter as tk
from PIL import Image, ImageTk

class Character:
    def __init__(self, name, actor, charpic, actorpic):
        self.name = name
        self.actor = actor
        self.charpic = Image.open(charpic)
        self.actorpic = Image.open(actorpic).resize(
                            (315,600), Image.ANTIALIAS)

keyleth = Character('Keyleth', 'Marisha Ray',
                        'characters/pc/Keyleth/Keyleth2.png',
                        'characters/pc/Keyleth/Ray.jpg')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.playing = False

        self.initUI()

    def toggle(self):
        if self.playing:
            self.subs['text'] = "paused"
            self.playing = False
        else:
            self.subs['text'] = "playing"
            self.playing = True

    def initUI(self):
        self.master.title("Critrole-Faces - ")

        tkchar = ImageTk.PhotoImage(keyleth.actorpic)
        self.actor = tk.Label(self, image=tkchar)
        self.actor.image = tkchar
        self.actor.grid(column=0, row=0)

        tkchar = ImageTk.PhotoImage(keyleth.charpic)
        self.char = tk.Label(self, image=tkchar)
        self.char.image = tkchar
        self.char.grid(column=1, row=0)

        self.subs = tk.Label(self, text="paused")
        self.subs.grid(column=0, columnspan=2, row=1)

        self.playpause = tk.Button(self, text="play/pause", command=self.toggle)
        self.playpause.grid(column=0, columnspan=2, row=2)

        self.grid()
        

def main():
    root = tk.Tk()
    app = Application()
    root.mainloop()

if __name__ == '__main__':
    main()
