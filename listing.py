# -*- coding: utf-8 -*-

# finding the area of a right triangle by the given cathetus
def gipotenuza():
    x = int(input("Write a number: "))
    y = int(input("Write a number: "))
    return print (x*y/2)

gipotenuza()

# solution of standard quadratic equations
import cmath
def uravnenie():
    a = int(input("Write a: "))
    b = int(input("Write b: "))
    c = int(input("Write c: "))
    print (((-b+cmath.sqrt(b*b-4*a*c))/2))
    print (((-b-cmath.sqrt(b*b-4*a*c))/2))

uravnenie()


# multiplication table M from a to b
def mul():
    a = int(input("Write a: "))
    b = int(input("Write b: "))
    M = int(input("Write b: "))
    for x in range(a,b+1,1):
        print(M, ' * ', x, ' = ', M*x)
    return 2

mul()


# lessons from loftblog: work with file
f = open('D:/test.txt', 'w')
f.write('str \r\n')
f.close()

f = open('D:/test.txt', 'r')
print (f.read(2))
print(f.read())

f = open('D:/test.txt', 'w')
f.write('abcdf')

f.seek(3)
f.write('CD')
f.close()

f = open('D:/test.txt', 'r')
print(f.readline())
print(f.readlines())
f.close()
f = open('D:/test.txt', 'r')
strings = f.readlines()
f.close()
strings[0] = 'qwerty'
f = open('D:/test.txt', 'w')
f.writelines(strings)
f.close()
