import math

def find_roots(a, b, c):
    r1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)
    r2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)


    return (r1,r2)

print(find_roots(1, 6, 9));