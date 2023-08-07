from tkinter import*

bigz = Tk()
bigz.title("p02 - Canvas")
bigz.resizable(False, False)

WIDTH = 500
HEIGHT = 500

canvas = Canvas(bigz, width = WIDTH, height = HEIGHT, bg="white")
canvas.pack()

xspeed = 1

# stvorcek
def stvorcek():
    canvas.create_rectangle(10,230, 50, 270, tags="Rectangle")

# pohyb
def move():
    global xspeed
    (left, up, right, down) = canvas.bbox("Rectangle")
    if left <= 0 or right >= WIDTH:
        xspeed = -xspeed
    canvas.move( "Rectangle", xspeed,0)
    canvas.after(10, move)
    
stvorcek()
move()
bigz.mainloop()