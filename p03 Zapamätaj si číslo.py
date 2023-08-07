from tkinter import*
from tkinter import messagebox
from random import*

bigz = Tk()
bigz.title("Zapamätaj si číslo")
bigz.geometry("500x500")

WIDTH = 200
HEIGHT = 200

num = randint(10000, 100000)

canvas = Canvas(width = WIDTH, height = HEIGHT)

def yournum():
    global tlac
    win1 = Tk()
    win1.title("Moje číslo")
    win1.geometry("300x200")
    canvas2 = Canvas(win1, width = 300, height = 200)
    canvas2.pack()
    canvas2.create_text(155, 40, text="Moje číslo je:", font='Arial 25 bold')
    canvas2.create_text(155, 100, text=num, font='Arial 35 bold')
    canvas2.after(360, win1.destroy())
    tlac.destroy()
    textinput()
    win1.mainloop()
    
def esteraz():
    frame.destroy()
    tlacidlo()

frame = Frame(bigz,width=500, height=500)

def textinput():
    cislo_label = Label(frame, text="Aké bolo moje číslo?:", font=("Arial", 30))
    cislo_entry = Entry(frame, font=("Arial", 30))
    def cislo_control():
        if int(cislo_entry.get())==num:
            messagebox.showinfo(title="číslo feedback", message="           SUPER         ")
            canvas.after(600, bigz.destroy())
        else:
            messagebox.showinfo(title="číslo? feedback", message="Zadané číslo je sensprávne")
            canvas.after(300, esteraz)
    control_button = Button(frame, text="Control", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=cislo_control)
    cislo_label.grid(row=1, column=1)
    cislo_entry.grid(row=2, column=1)
    control_button.grid(row=4, column=1)

frame.place(x=25, y=80)   

def tlacidlo():
    global tlac
    tlac = Button(bigz, text="START", font='Arial 35 bold', height= 5, width=10, background="#009999",command = yournum) 
    tlac.pack(pady= 80)


tlacidlo()
bigz.mainloop()