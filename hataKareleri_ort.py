i = 5
while(i > 0):	
	a = int(input("Kaç gözlemininz var  ? : "))
	i = 0
	HKO = 0
	Gdeger = 0
	Tdeger = 0
	topla = 0
	mutlak = 0
	mGpT = 0
	mHKO = 0

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
	    if((Gdeger - Tdeger) < 0):	
	    	mGpT = (Gdeger - Tdeger) * -1
	    else:	
	    	mGpT = (Gdeger - Tdeger)

	    mutlak = mutlak + mGpT

	mHKO = 1/i * mutlak
	HKO = 1/i * topla

	print("Hata Karelerinin Ortalaması (MSE) : ", HKO)
	print("\n Hata karelerinin Ortalamasının Kökü (RMSE) : ", HKO**0.5)
	print("\n Ortalama mutlak hata (MAE) : ", mHKO)

	i = i - 1


