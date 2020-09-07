def f(x):
	return x ** 2

def g(x):
	return x ** 3 - 2 * x ** 2 + 3 * x - 4

def h(x):
	return 3 * x

def tabular(inicio, final):
	print(f'|\tx\t|\tf(x)\t|\tg(x)\t|')
	print(f'|\t-\t|\t----\t|\t----\t|')
	for x in range(inicio, final + 1):
		print(f'|\t{x}\t|\t{f(x)}\t|\t{g(x)}\t|')


