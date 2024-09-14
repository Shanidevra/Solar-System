import turtle
import time
from math import *

screen = turtle.Screen()
screen.bgcolor("black")#creating the screen
screen.tracer(50)

sun = turtle.Turtle()#turtle object for sun
sun.shape('circle')#shape of sun
sun.color('yellow')#colour of sun
sun.shapesize(5, 5) # Size of the sun


class Planet(turtle.Turtle):
    def __init__(self,name,radius, color):#initialize function
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move(self):
        x = self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle) 

        self.goto(sun.xcor()+x,sun.ycor()+y)

# making plantes
mercury = Planet("Mercury",70, 'grey')
venus = Planet("Venus",90, 'orange')
earth=Planet("Earth",110,'skyblue')
mars = Planet("Mars",130, 'red')
jupiter=Planet("Jupiter",170, 'beige')
saturn=Planet("Saturn",240, 'pink')
uranus=Planet("Uranus",300, 'light blue')
neptune=Planet("Neptune",320, 'green')
jupiter.shapesize(3,3)
saturn.shapesize(3,3)


#adding planets to a list
myList = [ mercury, venus,earth, mars,jupiter,saturn,uranus,neptune]


while True:#while statement
    screen.update()#updating the screen
    for i in myList:
        i.move()#moving the elements of the list

    # Increase the angle by 0.0x radians
    
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007

    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005