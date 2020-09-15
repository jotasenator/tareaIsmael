
arr= [1,1,1,6,8,4,4,2,4]

new_arr=sorted(arr)

arr=list(set(arr))

lista_elementos_cantidad=[]
lista_cantidad=[]
lista_parejas=[]
for i in arr:
	contador=0
	for j in new_arr:
		if i==j:
			contador+=1
	valor=int(contador/2)
	if valor>=1:
		lista_cantidad.append({i:valor})
		lista_parejas.append(valor)
	lista_elementos_cantidad.append({i:contador})
	
	
print(f'Esta es la numeros ordenados y las cantidad existentes {lista_elementos_cantidad}.')
print(f'Existen estas relaciones numero:cantidad de parejas: {lista_cantidad}, lo cual da una cantidad de {sum(lista_parejas)} parejas.')

#con esta libreria sale un diccionario con clave numero valor cantidad de numero
from collections import Counter
numero_valor=Counter(arr)
