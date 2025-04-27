#f(x) = tan(x) + x
import math

a = 2.0
b = 2.1
e = 0.00000000001


f_a = math.tan(a) + a
f_b = math.tan(b) + b

if f_a * f_b > 0:
    print("Incorrect Guess")
else:
    while(abs(b-a) > e):
        c = (a + b) / 2
        f_c = math.tan(c) + c
        if f_a * f_c > 0:
            a = c
        else:
            b = c
print(c)