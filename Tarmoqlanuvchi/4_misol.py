import math
x=float(input("x ga qiymat bering: "))
if x<0:
	u=0
	print("u=", u)
elif 0<x<1:
	u=x**2-x
	print("u=", u)
else:
	u=x**4-math.sin(x**2)
	print("u=", u)

print("Tarmoqlanuvchi algoritmlar (B)", "muallif: Odiljonov")
input ("dasturdan chiqish uchun ENTER tugmasini bosing! ")