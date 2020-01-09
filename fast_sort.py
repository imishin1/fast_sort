def f_sort(massive):
	if len(massive) < 2:
		return massive
	else:
		index_pivot = len(massive)//2
		pivot = massive[index_pivot]
		less = [i for i in massive[:index_pivot] if i <= pivot] + [i for i in massive[index_pivot + 1:] if i <= pivot]
		greater = [i for i in massive [:index_pivot] if i > pivot] + [i for i in massive [index_pivot + 1:] if i > pivot]
		return f_sort(less) + [pivot] + f_sort(greater)