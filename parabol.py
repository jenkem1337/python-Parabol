def parabol(a,b,c):
	r1 = -b/2*a
	r2 = a*r1*r1+b*r1+c
	print("T({},{})".format(r1,r2))	

while True:

	print("f(x)=ax^2+bx+c için değer giriniz")

	a = float(input("a için değer giriniz : "))

	b = float(input("b için değer giriniz : "))

	c = float(input("c için değer giriniz : "))

	parabol(a,b,c)

