# Algoritmo para optimizar la busqueda
# Es necesario que la lista este ordenada (sorted)
def binary_search(sorted_numbers, number_to_find, low, high):
	if  low > high:
		return False
	mid = (low + high) / 2 # Recordar que al dividir ints no toma decimales

	#Primer caso base
	if sorted_numbers[mid] == number_to_find:
		return True
	#Segundo caso
	elif sorted_numbers[mid] > number_to_find:
		return binary_search(sorted_numbers , number_to_find, low, mid-1)
	#Tercer y ultimo caso
	else:
		return binary_search(sorted_numbers, number_to_find, mid+1, high)

if __name__=='__main__':
	numbers = [23, 1, 23, 25, 16, 12 ,2, 10, 7, 5, 3, 24, 20, 8, 6, 17, 9,
	 15, 14, 19, 4, 21, 11, 22, 18]

	sorted_numbers = sorted(numbers)
	number_to_find = int(input('Ingresa un numero para buscar: '))
	result = binary_search(sorted_numbers , number_to_find, 0, len(numbers)-1)

	if result is True:
		print('El numero {} esta en la lista.'.format(number_to_find))
	else:
		print('El numero {} no esta en la lista.'.format(number_to_find))
