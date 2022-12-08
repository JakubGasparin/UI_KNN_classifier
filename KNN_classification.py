import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.distance = -1


def classifier(x, y, k):
    global number_of_training_data
    global final_data

    for j in range(number_of_training_data):
        training_data[j].distance = math.sqrt((pow((x - training_data[j].x), 2)) + (pow((y - training_data[j].y), 2)))

    sorted_data = sorted(training_data, key=lambda z: z.distance)  # data sorter

    r_counter = 0
    g_counter = 0
    b_counter = 0
    p_counter = 0

    for j in range(k):
        if sorted_data[j].colour == "red":
            r_counter += 1
        elif sorted_data[j].colour == "green":
            g_counter += 1
        elif sorted_data[j].colour == "blue":
            b_counter += 1
        elif sorted_data[j].colour == "purple":
            p_counter += 1

    current_color = max(r_counter, g_counter, b_counter, p_counter)

    if current_color == r_counter:
        final_data.append(Point(x, y, "red"))
        training_data.append(Point(x, y, "red"))
        return "red"

    elif current_color == g_counter:
        final_data.append(Point(x, y, "green"))
        training_data.append(Point(x, y, "green"))
        return "green"

    elif current_color == b_counter:
        final_data.append(Point(x, y, "blue"))
        training_data.append(Point(x, y, "blue"))
        return "blue"

    elif current_color == p_counter:
        final_data.append(Point(x, y, "purple"))
        training_data.append(Point(x, y, "purple"))
        return "purple"


def _generate_red():
    x_corr = random.randint(-5000, 500)
    y_corr = random.randint(-5000, 500)
    return x_corr, y_corr


def _generate_green():
    x_corr = random.randint(-500, 5000)
    y_corr = random.randint(-5000, 500)
    return x_corr, y_corr


def _generate_blue():
    x_corr = random.randint(-5000, 500)
    y_corr = random.randint(-500, 5000)
    return x_corr, y_corr


def _generate_purple():
    x_corr = random.randint(-500, 5000)
    y_corr = random.randint(-500, 5000)
    return x_corr, y_corr


def _generate_red_outside_of_range():
    while True:
        x_corr = random.randint(-5000, 5000)
        y_corr = random.randint(-5000, 5000)
        if x_corr > 500 and y_corr > 500:
            return x_corr, y_corr


def _generate_green_outside_of_range():
    while True:
        x_corr = random.randint(-5000, 5000)
        y_corr = random.randint(-5000, 5000)
        if x_corr < -500 and y_corr > 500:
            return x_corr, y_corr


def _generate_blue_outside_of_range():
    while True:
        x_corr = random.randint(-5000, 5000)
        y_corr = random.randint(-5000, 5000)
        if x_corr > 500 and y_corr < -500:
            return x_corr, y_corr


def _generate_purple_outside_of_range():
    while True:
        x_corr = random.randint(-5000, 5000)
        y_corr = random.randint(-5000, 5000)
        if x_corr > 500 and y_corr > 500:
            return x_corr, y_corr


NUMBER = int(input("Enter the number of points: "))
print(f"Number of points is: {(NUMBER * 4) + 20}")

R1 = Point(-4500, -4400, "red")
R2 = Point(-4100, -3000, "red")
R3 = Point(-1800, -2400, "red")
R4 = Point(-2500, -3400, "red")
R5 = Point(-2000, -1400, "red")

G1 = Point(+4500, -4400, "green")
G2 = Point(+4100, -3000, "green")
G3 = Point(+1800, -2400, "green")
G4 = Point(+2500, -3400, "green")
G5 = Point(+2000, -1400, "green")

B1 = Point(-4500, +4400, "blue")
B2 = Point(-4100, +3000, "blue")
B3 = Point(-1800, +2400, "blue")
B4 = Point(-2500, +3400, "blue")
B5 = Point(-2000, +1400, "blue")

P1 = Point(+4500, +4400, "purple")
P2 = Point(+4100, +3000, "purple")
P3 = Point(+1800, +2400, "purple")
P4 = Point(+2500, +3400, "purple")
P5 = Point(+2000, +1400, "purple")

red = []
green = []
blue = []
purple = []

red_outside_of_the_range = []
green_outside_of_the_range = []
blue_outside_of_the_range = []
purple_outside_of_the_range = []

######## generating correct points ##########

for i in range(NUMBER):
    x, y = _generate_red()
    dot_red = Point(x, y, "red")
    red.append(dot_red)

    x, y = _generate_green()
    dot_green = Point(x, y, "green")
    green.append(dot_green)

    x, y = _generate_blue()
    dot_blue = Point(x, y, "blue")
    blue.append(dot_blue)

    x, y = _generate_purple()
    dot_purple = Point(x, y, "purple")
    purple.append(dot_purple)

######## generating correct points ##########


######## generating points outside of their given range ##########
for i in range(NUMBER):
    x, y = _generate_red_outside_of_range()
    dot_red = Point(x, y, "red")
    red_outside_of_the_range.append(dot_red)

    x, y = _generate_green_outside_of_range()
    dot_green = Point(x, y, "green")
    green_outside_of_the_range.append(dot_red)

    x, y = _generate_blue_outside_of_range()
    dot_blue = Point(x, y, "blue")
    blue_outside_of_the_range.append(dot_red)

    x, y = _generate_purple_outside_of_range()
    dot_purple = Point(x, y, "purple")
    purple_outside_of_the_range.append(dot_red)

######## generating points outside of their given range ##########

######## PLOTTING THE CANVAS #######
plt.xlim(-5000, 5000)
plt.ylim(-5000, 5000)
plt.yticks(np.arange(-5000, 6000, 1000))
plt.yticks(np.arange(-5000, 6000, 1000))
plt.xlabel("X")
plt.ylabel("Y")
fig, axs = plt.subplots(2, 2)
plt.suptitle(f'KNN algorithm for {(NUMBER * 4)+ 20} points')

######## PLOTTING THE CANVAS #######

knn_array = [1, 3, 7, 15]
colour_index = 0
color_counter = 0
for i in range(4):
    color_list = ["red", "green", "blue", "purple"]
    last_colour = ""

    ##### DATA TO SOLVE FOR #####
    number_of_training_data = 20
    training_data = []
    training_data.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
    start = time.time()

    current_colour = 0
    final_data = []
    final_data.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
    error = 0
    ##### DATA TO SOLVE FOR #####

    #### INDEXES ####
    r = 0
    g = 0
    b = 0
    p = 0
    #### INDEXES ####

    #### COUNTERS ####  # once we reach the needed number of points we solve for the cykle ends

    red_counter = 0
    blue_counter = 0
    green_counter = 0
    purple_counter = 0

    #### COUNTERS ####

    while True:
        if red_counter == blue_counter == green_counter == purple_counter == NUMBER:
            break

        color = color_list[
            colour_index]  # traversing the colours in order: red > green > blue > purple > red > green...
        colour_index += 1
        if colour_index == 4:
            colour_index = 0

        while True:
            if color != last_colour:
                break
            if red_counter or blue_counter or green_counter or purple_counter == 10000:
                break

        if color == "red":
            if red_counter != NUMBER:
                x_corr = red[r].x
                y_corr = red[r].y
                red_counter += 1
                r += 1
                current_colour = classifier(x_corr, y_corr, knn_array[i])
                number_of_training_data += 1
        if color == "green":
            if green_counter != NUMBER:
                x_corr = green[g].x
                y_corr = green[g].y
                green_counter += 1
                g += 1
                current_colour = classifier(x_corr, y_corr, knn_array[i])
                number_of_training_data += 1
        if color == "blue":
            if blue_counter != NUMBER:
                x_corr = blue[b].x
                y_corr = blue[b].y
                blue_counter += 1
                b += 1
                current_colour = classifier(x_corr, y_corr, knn_array[i])
                number_of_training_data += 1
        if color == "purple":
            if purple_counter != NUMBER:
                x_corr = purple[p].x
                y_corr = purple[p].y
                purple_counter += 1
                p += 1
                current_colour = classifier(x_corr, y_corr, knn_array[i])
                number_of_training_data += 1

        if current_colour != color:
            error += 1
        last_colour = current_colour

    end = time.time()
    current_set_color = color_list[color_counter]
    color_counter += 1
    print(f"Total elapsed time for colour {current_set_color}: {end - start}")
    print(f"Number of errors found: {error}")

    #### PLOTTING THE GRAPH ####
    for data in final_data:
        if knn_array[i] == 1:
            axs[0, 0].plot(data.x, data.y, marker="o", color=data.colour)
            axs[0, 0].set_title(knn_array[i])
        if knn_array[i] == 3:
            axs[0, 1].plot(data.x, data.y, marker="o", color=data.colour)
            axs[0, 1].set_title(knn_array[i])
        if knn_array[i] == 7:
            axs[1, 0].plot(data.x, data.y, marker="o", color=data.colour)
            axs[1, 0].set_title(knn_array[i])
        if knn_array[i] == 15:
            axs[1, 1].plot(data.x, data.y, marker="o", color=data.colour)
            axs[1, 1].set_title(knn_array[i])
    #### PLOTTING THE GRAPH ####

fig.tight_layout()
print(f"Saving the knn graph...")
plt.savefig("knn")
print("Graph saved.")
