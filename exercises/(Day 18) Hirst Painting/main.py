from turtle import Turtle, Screen
import colorgram
import turtle
import random
turtle.colormode(255)
cevdet = Turtle()
cevdet.shape("turtle")
cevdet.color("red")
cevdet.pencolor("blue")

def dashed_line():
    i = 0
    cevdet.penup()
    cevdet.goto(-300,0)
    while i < 31:
        cevdet.forward(10)
        cevdet.penup()
        cevdet.forward(10)
        cevdet.pendown()
        i += 1

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        cevdet.forward(150)
        cevdet.right(angle)

cevdet.speed("fastest")

# colors = colorgram.extract("image.jpeg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_colors.append((r,g,b))
# print(rgb_colors)

color_list = [(249, 248, 243), (243, 250, 247), (250, 243, 247), (242, 246, 251), (233, 224, 83), (189, 10, 68), (115, 176, 210), (193, 77, 22), (213, 163, 103), (192, 163, 20), (226, 57, 132), (33, 103, 163), (15, 24, 64), (38, 185, 114), (196, 35, 126), (21, 30, 164), (213, 135, 177), (19, 180, 208), (229, 223, 10), (230, 168, 198), (129, 187, 161), (11, 47, 29), (43, 130, 77), (55, 21, 11), (144, 216, 200), (134, 216, 229), (231, 67, 38), (110, 91, 207), (176, 21, 12), (73, 11, 29)]
cevdet.pensize(15)
for i in range(10):
    cevdet.penup()
    cevdet.goto(-250, i * 50- 250)
    for j in range(10):
        cevdet.pendown()
        cevdet.dot(20, random.choice(color_list))
        cevdet.penup()
        cevdet.forward(50)
# for _ in range(72):
#     cevdet.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     cevdet.circle(90)
#     cevdet.right(5)














screen = Screen()
screen.exitonclick()