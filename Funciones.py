def f(x):
	return x ** 2

def g(x):
	return x ** 3 - 2 * x + 1

def h(x):
	return 3 * x

def tabular(fn, inicio, final):
	print(f'|\tx\t|\t{fn.__name__}(x)\t|')
	print(f'|\t-\t|\t----\t|')
	for x in range(inicio, final + 1):
		print(f'|\t{x}\t|\t{fn(x)}\t|')



