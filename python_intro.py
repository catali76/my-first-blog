dziewczyny=['Kasia','Dorota','Malwina']
def hi(name):
	print('Hej '+ name)
for imie in dziewczyny:	
	hi(imie)
	print('Kolejna dziewczyna')		
for i in range(1,2000000):
	pass
print(i)


def dodawanie(liczba):
	if not liczba.isdigit():
		print('to nie jest liczba')
	else:
		print(int(liczba) + 2)

dodawanie('asdf')


