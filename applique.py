def applique(f, t:list):
	new = []
	for i in t:
		new.append(f(i))
	return new

#Fonction qui remplace les nombres impairs en nombres pairs
def new_pair(x):
	if x%2 != 0:
		x+=1
		return x
	return x

def new_maj(x):
	x = x.upper()
	return x

ma_liste = [2,4,105,5,6,8,9,10]
new_liste = ['un', 'deux', 'trois', 'quatre']
print(applique(new_maj, new_liste))
print(applique(new_pair, ma_liste))