# PURPOSE: Create a colorful pattern using Turtle Graphics.
# INPUT: Number of shapes and size of each shape from the user.
# PROCESS: Draw multiple shapes in different colors at random locations.
# OUTPUT: A colorful pattern displayed on the screen.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

import turtle
import random

def draw_shape(turtle_obj, shape_size):
    """Draw a shape with a specified size at a random location."""
    turtle_obj.penup()
    x = random.randint(-200, 200)  # Random x coordinate
    y = random.randint(-200, 200)  # Random y coordinate
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    
    # Draw a square as an example shape
    for _ in range(4):
        turtle_obj.forward(shape_size)
        turtle_obj.right(90)
    
def main():
    """Main function to create a colorful pattern."""
    screen = turtle.Screen()
    screen.bgcolor("white")

    user_shapes = int(turtle.numinput("Input", "Enter the number of shapes: ", minval=1, maxval=100))
    shape_size = int(turtle.numinput("Input", "Enter the size of each shape: ", minval=10, maxval=200))
    
    # Create a turtle object
    colorful_turtle = turtle.Turtle()
    
    for _ in range(user_shapes):
        color = (random.random(), random.random(), random.random())  # Generate a random color
        colorful_turtle.color(color)
        draw_shape(colorful_turtle, shape_size)

    turtle.done()

if __name__ == "__main__":
    main()
