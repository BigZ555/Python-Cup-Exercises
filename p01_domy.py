from turtle import *

velkost = 30

def pozicio():
    up()
    setx(-250)
    pd()

def stvorec(d):
    for i in range(4):
        fd(d)
        rt(90)
        
def trojuh(strana):
    for i in range(3):
        fd(strana)
        lt(120)

def dom(velkost):
    stvorec(velkost)
    trojuh(velkost)

def domy9():
    pozicio()
    for i in range(0,9):
        dom(velkost)
        fd(30)
        up()
        fd(30)
        pd()
    
speed(0)
domy9()
ht()
exitonclick()