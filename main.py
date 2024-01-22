import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess a State ", prompt="What's another state's name?").capitalize()
print(answer)

screen.exitonclick()
