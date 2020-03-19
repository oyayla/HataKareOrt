i = 5
while(i > 0):	
	a = int(input("Kaç gözlemininz var  ? : "))
	i = 0
	HKO = 0
	Gdeger = 0
	Tdeger = 0
	topla = 0

	while(a > 0):
	    a = a - 1
	    i = i + 1

	say = 0
	while(say < i):
	    say = say + 1


	    Gdeger = float(input(". Gerçek değeri gir : "))
	    Tdeger = float(input(". Tahmin edilmiş olan değeri gir : "))
	    GpT = (Gdeger - Tdeger) * (Gdeger - Tdeger)
	    topla = (topla + GpT)

	HKO = 1/i * topla

	print("Hata Karelerinin Ortalaması : ", HKO)
	print(" Hata karelerinin Ortalamasının Kökü : ", HKO**0.5)

	i = i - 1


