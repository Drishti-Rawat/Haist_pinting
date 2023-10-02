# import colorgram
# rgb_color = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
import random
import turtle
color_list = [(253, 252, 241), (238, 251, 245), (188, 19, 46), (244, 233, 61), (252, 230, 236), (217, 238, 244), (195, 76, 34), (218, 66, 106), (15, 142, 89), (196, 176, 19), (21, 125, 173), (108, 182, 209), (18, 167, 213), (209, 153, 90), (26, 40, 75), (36, 43, 110), (79, 175, 96), (181, 44, 65), (235, 231, 5), (216, 67, 48), (217, 129, 153), (125, 185, 119), (238, 161, 180), (8, 61, 38), (148, 209, 221), (9, 92, 53), (6, 87, 109), (160, 30, 27), (237, 169, 162), (159, 212, 183)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.isvisible()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()