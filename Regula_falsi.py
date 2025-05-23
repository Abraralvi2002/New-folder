# f(x) = x^3 - 4x - 9
def f(x):
    return x**3 - 4*x - 9

a = 2.0
b = 3.0
e = 0.00001

f_a = f(a)
f_b = f(b)

if f_a * f_b > 0:
    print("Incorrect initial guesses")
else:
    while True:
        c = (a * f_b - b * f_a) / (f_b - f_a)
        f_c = f(c)

        if abs(f_c) < e:
            break

        if f_a * f_c < 0:
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c

print("Root is:", c)
