# f(x) = 3*x^2 + 2*x + 4

a = 1.0
b = 16.0
e = 0.000001

f_a = (a**2) - 2*a - 140
f_b = (b**2) - 2*b - 140 

if(f_a * f_b > 0):
    print("Incorrect Initial Guess")
else:
    c = (a*f_b - b*f_a) / (f_b - f_a)
    f_c = 3*(c**2) + 2*c + 4
    while(abs(f_c) > e):
        c = (a*f_b - b*f_a) / (f_b - f_a)
        f_c = 3*(c**2) + 2*c + 4
        if(f_a * f_c > 0):
            a = c
            f_a = f_c
        else:
            b = c
            f_b = f_c
    print(c)
