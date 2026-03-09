# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral', 'yellow')
# timmy.forward(100)
# timmy.circle(300)
# timmy.penup()
# timmy.forward(50)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# my_screen.title("My Favorite Game")
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
print(table)