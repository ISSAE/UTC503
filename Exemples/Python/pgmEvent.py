from tkinter import *

def f(ok, pasok):
    screen=Tk()
    screen.geometry("200x200")
    screen.title("Alors ???")
    lbl=Label(screen, text="Hello")
    lbl.pack()
    Button(screen, text="c'est OK", command=ok(lbl)).pack()
    Button(screen, text="c'est pas OK", command=pasok(lbl)).pack()
    screen.mainloop()

f(lambda lbl: lambda : lbl.configure(text="Vous avez cliquer ok"), 
lambda lbl: lambda : lbl.configure(text="Vous avez cliquer pas ok"))