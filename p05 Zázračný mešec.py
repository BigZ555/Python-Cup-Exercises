from tkinter import*
from random import*

bigz = Tk()
bigz.title('Zázračný mešec')
bigz.geometry("500x500")
WIDTH = 500
HEIGHT = 500

mesecobr = PhotoImage(file="mesec.png")
mincaobr = PhotoImage(file="minca.png")

canvas = Canvas(bigz, width = WIDTH, height = HEIGHT, bg="#99FFFF")
canvas.pack()

canvas.create_image(225, 420 ,image=mesecobr)
mnozstvo = int(input('Koľko mincí chceťe?'))

def mince():
    for i in range(0,mnozstvo):
        xpos = randint(18,482)
        ypos = randint(18,370)
        canvas.create_image(xpos, ypos ,image=mincaobr)
mince()
bigz.mainloop()
