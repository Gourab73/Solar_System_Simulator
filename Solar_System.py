import random
import turtle
import math

s = turtle.Screen()
s.title("Solar System Simulation")
s.bgcolor("black")

neptune = turtle.Turtle()
uranus = turtle.Turtle()
saturn = turtle.Turtle()
jupiter = turtle.Turtle()
# asteroids = turtle.Turtle()
# asteroids = []
# for i in range(250):
#     asteroids.append(turtle.Turtle())
mars = turtle.Turtle()
earth = turtle.Turtle()
venus = turtle.Turtle()
mercury = turtle.Turtle()
s.tracer(2)

def way_to_orbit(x,y, object, colors, shapeSize):
    object.dot(90, "yellow")
    object.fillcolor(colors)
    object.shapesize(shapeSize)
    object.shape("circle")
    object.penup()
    object.setposition(x, y)
    object.pendown()
    object.pencolor("white")


def ellipse(object1, object2, object3, object4,object5, object6, object7, object8):

    object8_xvel = 0
    object8_yvel = 1
    object7_xvel = 0
    object7_yvel = 1
    object6_xvel = 0
    object6_yvel = 1
    object5_xvel = 0
    object5_yvel = 1
    # objectIA_xvel = 0
    # objectIA_yvel = 1
    object4_xvel = 0
    object4_yvel = 1
    object3_xvel = 0
    object3_yvel = 1
    object2_xvel = 0
    object2_yvel = 1
    object1_xvel = 0
    object1_yvel = 1

    while True:

        s.update()

        object8_xvel += math.cos(math.radians(object8.towards(0, 0))) * (1000 / (object8.xcor() ** 2 + object8.ycor() ** 2))
        object8_yvel += math.sin(math.radians(object8.towards(0, 0))) * (1000 / (object8.xcor() ** 2 + object8.ycor() ** 2))
        object8.setposition(object8.xcor() + object8_xvel, object8.ycor() + object8_yvel)

        object7_xvel += math.cos(math.radians(object7.towards(0, 0))) * (1000 / (object7.xcor() ** 2 + object7.ycor() ** 2))
        object7_yvel += math.sin(math.radians(object7.towards(0, 0))) * (1000 / (object7.xcor() ** 2 + object7.ycor() ** 2))
        object7.setposition(object7.xcor() + object7_xvel, object7.ycor() + object7_yvel)

        object6_xvel += math.cos(math.radians(object6.towards(0, 0))) * (1000 / (object6.xcor() ** 2 + object6.ycor() ** 2))
        object6_yvel += math.sin(math.radians(object6.towards(0, 0))) * (1000 / (object6.xcor() ** 2 + object6.ycor() ** 2))
        object6.setposition(object6.xcor() + object6_xvel, object6.ycor() + object6_yvel)

        object5_xvel += math.cos(math.radians(object5.towards(0, 0))) * (1000 / (object5.xcor() ** 2 + object5.ycor() ** 2))
        object5_yvel += math.sin(math.radians(object5.towards(0, 0))) * (1000 / (object5.xcor() ** 2 + object5.ycor() ** 2))
        object5.setposition(object5.xcor() + object5_xvel, object5.ycor() + object5_yvel)

        # for iast in asteroids:
        #     objectIA_xvel += math.cos(math.radians(iast.towards(0, 0))) * (1000 / (iast.xcor() ** 2 + iast.ycor() ** 2))
        #     objectIA_yvel += math.sin(math.radians(iast.towards(0, 0))) * (1000 / (iast.xcor() ** 2 + iast.ycor() ** 2))
        #     iast.setposition(iast.xcor() + objectIA_xvel, iast.ycor() + objectIA_yvel)

        object4_xvel += math.cos(math.radians(object4.towards(0, 0))) * (1000 / (object4.xcor() ** 2 + object4.ycor() ** 2))
        object4_yvel += math.sin(math.radians(object4.towards(0, 0))) * (1000 / (object4.xcor() ** 2 + object4.ycor() ** 2))
        object4.setposition(object4.xcor() + object4_xvel, object4.ycor() + object4_yvel)

        object3_xvel += math.cos(math.radians(object3.towards(0, 0))) * (1000 / (object3.xcor() ** 2 + object3.ycor() ** 2))
        object3_yvel += math.sin(math.radians(object3.towards(0, 0))) * (1000 / (object3.xcor() ** 2 + object3.ycor() ** 2))
        object3.setposition(object3.xcor() + object3_xvel, object3.ycor() + object3_yvel)

        object2_xvel += math.cos(math.radians(object2.towards(0, 0))) * (1000 / (object2.xcor() ** 2 + object2.ycor() ** 2))
        object2_yvel += math.sin(math.radians(object2.towards(0, 0))) * (1000 / (object2.xcor() ** 2 + object2.ycor() ** 2))
        object2.setposition(object2.xcor() + object2_xvel, object2.ycor() + object2_yvel)

        object1_xvel += math.cos(math.radians(object1.towards(0, 0))) * (1000 / (object1.xcor() ** 2 + object1.ycor() ** 2))
        object1_yvel += math.sin(math.radians(object1.towards(0, 0))) * (1000 / (object1.xcor() ** 2 + object1.ycor() ** 2))
        object1.setposition(object1.xcor() + object1_xvel, object1.ycor() + object1_yvel)

way_to_orbit(620, 0, neptune, "grey",1.5)
way_to_orbit(590, 0, uranus, "indigo",1.7)
way_to_orbit(540, 0, saturn, "green",2)
way_to_orbit(490, 0, jupiter, "orange",2.5)
way_to_orbit(440, 0, mars, "red",0.6)
way_to_orbit(390, 0, earth, "blue",0.8)
way_to_orbit(330, 0, venus, "pink",0.5)
way_to_orbit(288, 0, mercury, "brown",0.3)

ellipse(mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)


turtle.done()
