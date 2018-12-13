
def sort_array(arraylist):
	array_1 = [5,1,15,0,8,2,-2,1]
	i = None
	for size in range(1,len(array_1)):
		chave = array_1[size]
		i = size - 1
		while i >= 0 and array_1[i] > chave:
			array_1[i + 1] = array_1[i]
			i = i - 1
			array_1[i + 1] = chave
	return array_1

