import turtle

import pandas

screen = turtle.Screen()
img_path = "blank_states_img.gif"
screen.addshape(img_path)
turtle.shape(img_path)
screen.title("U.S. States Game")

# How to get cords:
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)
states = pandas.read_csv("50_states.csv")
correct_guess = []

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    match = states[states.state == answer_state]
    if answer_state == "Exit":
        states_to_learn = [state for state in states.state.to_list() \
                           if state not in correct_guess]
        to_learn = pandas.DataFrame(states_to_learn)
        to_learn.to_csv("to_learn.csv")
        break

    if answer_state and not match.empty and answer_state not in correct_guess:
        correct_guess.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(match.x.item(), match.y.item())
        new_turtle.write(answer_state, True, font=("Arial", 12, "normal"))

# states_to_learn.csv
#states_list = states.state.to_list()



# turtle.mainloop()
#screen.exitonclick()
