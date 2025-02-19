from math import *


def main(y):
    try:
        numerator = 46 * y**3 + (log(y)**5/56)
        denominator = 54 * (abs(y**3 + y ** 2))**5 + 23 * y**6
        return (numerator / denominator) - (63 * y + y**7)
    except ArithmeticError:
        return "Error"
