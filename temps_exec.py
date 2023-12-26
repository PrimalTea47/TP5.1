import time

def temps_exec(f,x):
	debut = time.time()
	print(f'[*]Comptage jusqu\'à {x} en cours. Veuillez patienter...[*]')
	f(x)
	fin = time.time()
	return f'{x} ==> {int(fin-debut)} secondes d\'exécution'



def useless(nb:int):
	a = 0

	for i in range(nb):
		a+=1
		if a % 10000000 == 0:
			print(f'[*]{a}[*]')
	return a

#Exécution

print(temps_exec(useless, 99999999))