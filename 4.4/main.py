# twisty square thing

import turtle

# colour options
colours = {
    "rainbow": ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF", "#A0C4FF", "#BDB2FF", "#FFC6FF"],
    "sunset": ["#8C5866", "#312740", "#F29966", "#D97B59", "#8C4F49"],
    "ocean": ["#22577A", "#38A3A5", "#57CC99", "#80ED99", "#C7F9CC"],
    "forest": ["#030D06", "#13260E", "#294012", "#7B8C3B", "#99A637"],
    "softs": ["#FFB6C1", "#FFDAB9", "#E6E6FA", "#B0E0E6"],
    "greys": ["#DCDCDC", "#A9A9A9", "#808080", "#505050", "#2F4F4F"],
    "tropical": ["#8C7C2B", "#D9C5A0", "#F2780C", "#D92D07", "#8C0707"],
    "winter": ["#F0F0F2", "#4B7BA6", "#639CBF", "#A7D5F2", "#BDE3F2"],
    "swamp": ["#8B8D61", "#878878", "#B6BD98", "#D0C792", "#3C743E"],
    "desert": ["#F2C879", "#A66124", "#F29D52", "#8C593B", "#D98C5F"],
}

# user picks colour
print("colour sets:")
for colour in colours:
    print("- " + colour)

colour_choice = input("Pick a colour set: ").lower()
if colour_choice not in colours:
    colour_choice = "rainbow"
colour_list = colours[colour_choice]

# user picks number of levels
levels_input = input("Pick number of levels (10-40): ")
levels = int(levels_input) if levels_input else 30
if levels < 10 or levels > 40:
    levels = 30

# user picks starting square size
size_input = input("Pick starting square size (50-200): ")
size = int(size_input) if size_input else 150
if size < 50 or size > 200:
    size = 150


# recursive function
def draw(levels_remaining, current_size=size, calls=1, colour_index=0):
    if levels_remaining == 0 or current_size < 2:
        return calls

    # reset colour_index at end of list
    if colour_index == len(colour_list) - 1:
        colour_index = 0

    # set colour
    t.pencolor(colour_list[colour_index])

    # draw square
    for _ in range(4):
        t.width(4)
        t.forward(current_size)
        t.right(90)

    # rotate a bit for next square
    t.right(10)

    # recursive call increasing colour_index
    return draw(levels_remaining - 1, current_size * 0.85, calls + 1, colour_index + 1)


# setup turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.penup()
t.goto(-size / 2, size / 2)  # center the square
t.pendown()
t.hideturtle()

# draw squares and get calls
total_calls = draw(levels, size)

# print amount of recursive calls
print("Total recursive calls: " + str(total_calls))