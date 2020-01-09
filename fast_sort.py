def f_sort(massive):
	if len(massive) < 2:
		return massive #базовый случай: массивы с 0 и 1 элементом уже отсортированы
	else:
		pivot = massive[0] #рекурсивный случай
		less = [i for i in massive[1:] if i <= pivot] #подмассив всех элементов, меньших опорного
		greater = [i for i in massive [1:] if i > pivot] #подмассив всех элементов, больших опорного
		return f_sort(less) + [pivot] + f_sort(greater)
a = [1, -124124, -1, 124, 5, 0, 0, 0, 2,14,124,2,1,4,12,4,65,1,25,8,872,36,2,63,236,-124124124124]
print(f_sort(a))