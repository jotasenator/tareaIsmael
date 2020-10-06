

'''from itertools import combinations,permutations

arr=[1,2,3,4,5,6]

a=list(combinations(arr,2))

b=list(permutations(arr,2))

print(a)
print(len(a))

print(b)

print(len(b))'''

arr=[1,2,3,4,5,6]
lista=[]

for i in range(len(arr)-1):
	for j in range(i+1,len(arr)):
		lista.append([arr[i],arr[j]])

print(len(lista))
print(lista)

lista1=[[arr[i],arr[j]]  for i in range(len(arr)-1) for j in range(i+1,len(arr))]
print(lista1)






		