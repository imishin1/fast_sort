def f_sort(massive):
	if len(massive) < 2:
		return massive #базовый случай: массивы с 0 и 1 элементом уже отсортированы
	else:
		index_pivot = len(massive)//2
		pivot = massive[index_pivot] #рекурсивный случай
		#подмассив всех элементов, меньших опорного
		less = [i for i in massive[:index_pivot] if i <= pivot] + [i for i in massive[index_pivot + 1:] if i <= pivot]
		#подмассив всех элементов, больших опорного
		greater = [i for i in massive [:index_pivot] if i > pivot] + [i for i in massive [index_pivot + 1:] if i > pivot]
		return f_sort(less) + [pivot] + f_sort(greater)
a = [1, -124, -1, 5, 6, 124, 2, 7, 7, 0, -136]
print(f_sort(a))