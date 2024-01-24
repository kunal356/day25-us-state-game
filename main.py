# *********My Solution**********:
# import turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# states_data = pandas.read_csv("50_states.csv")
# print(states_data)
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# game_is_on = True
# correct_guesses = 0
# turtle.tracer(0)
# guessed_states = []
# while game_is_on:
#     answer = screen.textinput(title=f"{correct_guesses}/50Guess a State ",
#                               prompt="What's another state's name?").title()
#     match_with_data = states_data[states_data.state == answer]
#
#     if not match_with_data.empty:
#         state_name = match_with_data.state.item()
#         if state_name not in guessed_states:
#             turtle.penup()
#             guessed_states.append(state_name)
#             turtle.goto(x=match_with_data.x.item(), y=match_with_data.y.item())
#             turtle.write(arg=state_name, move=False, align="center", font=("Courier", 8, "normal"))
#             turtle.goto(0, 0)
#             correct_guesses += 1
#             turtle.update()
#     else:
#         print("empty data frame")
#
# turtle.mainloop()

# Angela's Solution

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
turtle.tracer(0)
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50Guess a State ",
                                prompt="What's another state's name?").title()
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
turtle.mainloop()
