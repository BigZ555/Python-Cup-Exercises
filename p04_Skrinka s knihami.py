from turtle import*
from random import*

window = Screen()
window.setup(500,500)
window.title("Skrinka s knihami")


farba = ["red", "blue", "green", "orange", "purple", "cyan", "brown"]

def skrinka():
    y = -150
    up()
    setx(-80)
    sety(-150)
    pd()
    lt(90)
    fd(300)
    up()
    setx(80)
    pd()
    back(300)
    lt(90)
    for i in range(0, 5):
        sety(y+50)
        fd(160)
        back(160)
        y = y+50
    up()
    
def rady():
    ypos = -100
    rt(90)
    for r in range(0,5):
        up()
        setx(-75)
        sety(ypos)
        pd()
        for i in range(0, randint(8,13)):
            if xcor() <= 67:
                vyska = randint(25, 45)
                sirka = randint(10, 15)
                fillcolor(choice(farba))
                begin_fill()
                fd(vyska)
                rt(90)
                fd(sirka)
                rt(90)
                fd(vyska)
                rt(90)
                fd(sirka)
                end_fill()
                up()
                back(sirka)
                rt(90)
                pd()
        ypos = ypos + 50        
        
skrinka()
rady()
exitonclick()
