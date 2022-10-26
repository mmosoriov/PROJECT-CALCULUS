import numpy as np

# trying out numerical derivatives


def function(x):
    return x ** 2


def derivative(x):
    dx = 1 / 100
    dy = function(x + dx) - function(x)
    yprime = dy / dx
    return yprime


# trying out symbolic derivatives


def start_application():

    y = input("Insert the function to evaluate: ")
    print("The function to evaluate is: f(x)= " + y)

    print("To calculate derivative of " + y + ", type 'derivative(n)")

    def function(y):
        return y

    def derivative(y):
        dx = 1 / 100
        dy = function(y + dx) - function(y)
        yprime = dy / dx
        return yprime


start_application()
