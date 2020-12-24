import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
tut = turtle.Turtle()
tut.penup()
tut.hideturtle()


# def get_mouse_click(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click)


count = 0
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

while count < 50:
    answer_state = screen.textinput(f"{count}/50 States", prompt="What's another state's name?").title()
    if answer_state in states:
        state = data[data.state == answer_state]
        tut.goto(int(state.x), int(state.y))
        tut.write(answer_state, False, "center")
        count += 1
        states.pop(states.index(answer_state))

    if answer_state == 'Exit':
        break

missing_states = pandas.DataFrame(states)
missing_states.to_csv("Missed_States.csv")
