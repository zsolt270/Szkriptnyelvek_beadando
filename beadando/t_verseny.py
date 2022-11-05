import turtle
import random as r
import osztaly as o
from turtle import Screen

# képernyő beállítás
s = Screen()
s.setup(width=800, height=600)
s.bgpic('road.gif')

# játékosok
yellow = o.Teknosok("yellow")
black = o.Teknosok("black")
blue = o.Teknosok("blue")
red = o.Teknosok("red")
white = o.Teknosok("white")
brown = o.Teknosok("brown")
orange = o.Teknosok("orange")

# teknősök
y_kordinatak = [-260, -172, -85, 2, 85, 172, 260]
colors = ["white", "red", "black", "blue", "brown", "yellow", "orange"]
all_turtle=[]
for i in range(0,7):
   new_turtle = turtle.Turtle(shape="turtle")
   new_turtle.penup()
   new_turtle.color(colors[i])
   new_turtle.shapesize(2)
   new_turtle.goto(x=-350, y=y_kordinatak[i])
   all_turtle.append(new_turtle)

is_on = True
while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 340:
            is_on = False
            winner = turtle.pencolor()
            if winner == "yellow":
                  yellow.pontszerzes()
            elif winner == "brown":
                brown.pontszerzes()
            elif winner == "blue":
                blue.pontszerzes()
            elif winner == "red":
                red.pontszerzes()
            elif winner == "white":
                white.pontszerzes()
            elif winner == "orange":
                orange.pontszerzes()
            else:
                black.pontszerzes()
        random_pace = r.randint(0,7)
        turtle.forward(random_pace)

print(f"Narancs teknős pontjai: ",orange.score)
print(f"Kék teknős pontjai: ",blue.score)
print(f"Fekete teknős pontjai: ",black.score)
print(f"Piros teknős pontjai: ",red.score)
print(f"Sárga teknős pontjai: ",yellow.score)
print(f"Fehér teknős pontjai: ",white.score)
print(f"Barna teknős pontjai: ",brown.score)

s.exitonclick()