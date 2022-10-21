import math
a = float(input("chieu dai canh a: "))
b = float(input("chieu dai canh b: "))
c = float(input("chieu dai canh c: "))
P = (a + b + c) / 2
dien_tich = math.sqrt( P * ( P-a) * (P-b) * (P-c))
print(" Area of the triangle is: ", dien_tich)
