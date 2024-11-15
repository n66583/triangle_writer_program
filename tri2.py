from math import acos, asin, degrees, sqrt
import turtle as t


while True:
    a = int(input("Enter side1 of a triangle: "))
    b = int(input("Enter side2 of a triangle: "))
    c = int(input("Enter side3 of a triangle: "))

    if a+b > c and a+c > b and b+c > a:
        print("I will write the triangle...")
        break
    else:
        print(
            "I can't write a triangle with these numbers. please enter the numbers again.")
        continue

a *= 30
b *= 30
c *= 30

x = (a**2 - b**2 + c**2) / (2*c)
y = c-x
h = sqrt(b**2 - y**2)

A = degrees(asin(h/b))
C1 = degrees(acos(h/b))
C2 = degrees(acos(h/a))

t.speed(1)

t.lt(A)
t.fd(b)

t.rt(180 - (C1 + C2))
t.fd(a)

t.home()
