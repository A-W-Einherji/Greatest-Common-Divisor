# This program runes the Euclidean Algorithm to find the GCD, greatest common divisor of two numbers (a,b).


def maximum(x, y):
    if x >= y:
        return x
    if x < y:
        return y


def minimum(x, y):
    if x >= y:
        return y
    if x < y:
        return x


def gcd(m, n):
    a0 = m
    b0 = n
    ai = maximum(a0, b0) - minimum(a0, b0)
    bi = minimum(a0, b0)
    while maximum(ai, bi) - minimum(ai, bi) > 0:
        ai2 = maximum(ai, bi) - minimum(ai, bi)
        bi2 = minimum(ai, bi)
        ai = ai2
        bi = bi2
    return ai

a = int(input("Please enter the first number you would like to find the greatest common divisor of: "))
b = int(input("Please enter the second number you would like to find the greatest common divisor of: "))

print("The greatest common divisor is: " + str(gcd(a, b)))
