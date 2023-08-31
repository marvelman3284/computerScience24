from turtle import *
from time import sleep


def draw_triangle(side_length):
    # iterate 3 times, each time moving foward side_length 
    # before turning right 120 degrees
    for _ in range(3):
        forward(side_length)
        right(120)


def draw_hexagon(side_length):
    # call the draw_triangle function 6 times
    # but the turtle must turn an extra 60 degrees at the end of each iteration 
    # in order to draw seperate triangles
    for _ in range(6):
        draw_triangle(side_length)
        right(60)


def check_equality(string, number):
    return int(string) == number


def main():
    # read in the user input for the side length
    side_length = int(input("How long should each shape be: "))
    draw_hexagon(side_length)
    sleep(5)

    # collect user input for the check_equality function
    user_string = input("Enter a number: ")
    user_number = int(input("Enter another number: "))
    check_equality(user_string, user_number)

main()
