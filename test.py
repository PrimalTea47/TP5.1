def trouve(p,t:list):
	for i in t:
		if p(i):
			return True


#ma fonction p trouve le si un nombre est impair
def impair(x):
	if x%2 != 0:
		return True
	return False

#Éxécution du programme
ma_liste = [2,4,6,8,9,10]
if trouve(impair, ma_liste):
	print(f'Un nombre est impair dans la liste {ma_liste}')
else:
	print(f'Aucun nombre impair dans la liste {ma_liste}')
