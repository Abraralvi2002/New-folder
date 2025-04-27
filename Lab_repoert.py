# f(x) = 2x^3 -2x - 5 (Let us assume the interval between two is [1,2])
import math
a = 1.0
b = 2.0
e = 0.000000001

f_a = 2 * a**3 - 2 * a - 5
f_b = 2 * b**3 - 2 * b - 5

if(f_a * f_b > 0):
    print("Incorrect Guess, Please Try Again")
else:
    while(abs(b-a) > e):
        c = (a + b) / 2
        f_c = 2 * c**3 - 2 * c - 5
        if(f_a * f_c > 0):
            a = c
        else:
            b = c
    print(f"The founded root is: {c}")
