# PROGRAM: Simple Shape and Colorful Pattern Drawing with Turtle Graphics
# PURPOSE: Draws a specified shape, creates a colorful pattern, and generates a spiral design.
# INPUT: User specifies shape type (square, triangle, rectangle), size, number of shapes, and spiral parameters.
# PROCESS: Uses Turtle Graphics to draw shapes and patterns based on user input.
# OUTPUT: Visual output of shapes and patterns on the screen.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

import turtle
import random

def draw_shape(shape_type, size):
    """Draws a specified shape with the given size."""
    if shape_type == "square":
        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)
    elif shape_type == "triangle":
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    elif shape_type == "rectangle":
        for _ in range(2):
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size / 2)  # Rectangle height is half the width
            turtle.right(90)
    else:
        print("Invalid shape type")

def draw_colorful_pattern(num_shapes, size):
    """Draws a specified number of colorful shapes at random locations."""
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for _ in range(num_shapes):
        turtle.penup()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random.choice(colors))
        draw_shape(random.choice(["square", "triangle", "rectangle"]), size)

def draw_spiral(turns, distance):
    """Draws a spiral design with varying colors."""
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for i in range(turns):
        turtle.color(random.choice(colors))
        turtle.forward(distance)
        turtle.right(30)  # Change angle for the spiral effect
        distance += 5  # Increase distance for each turn

def main():
    """Main module to control the flow of the program."""
    turtle.speed(0)  # Set turtle speed to maximum

    # Simple Shape Drawing
    shape_type = input("Enter shape type (square, triangle, rectangle): ").lower()
    size = int(input("Enter size of the shape: "))
    draw_shape(shape_type, size)

    # Colorful Pattern
    num_shapes = int(input("\nEnter the number of shapes for the colorful pattern: "))
    size = int(input("Enter the size of each shape: "))
    draw_colorful_pattern(num_shapes, size)

    # Spiral Design
    turns = int(input("\nEnter the number of turns for the spiral design: "))
    distance = int(input("Enter the starting distance for the spiral: "))
    draw_spiral(turns, distance)

    turtle.done()  # Finish the turtle graphics drawing

if __name__ == "__main__":
    main()
