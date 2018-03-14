from timeit import default_timer as timer

# recursive
def frec(x):
	if x <= 1:
		return x
	return frec(x-2) + frec(x-1)

# iterative
def fit(x):
	a,b = 0,1
	for i in range(x):
		a,b = b, a+b
	return a

print("Recursive")
for i in [1,10,20,30,40,50]:
	start = timer()
	res = frec(i)
	end = timer()
	print("%d = %d og tók %.4f sek" % (i, res, end-start))

print("Iterative")
for i in [1,10,20,30,40,50]:
	start = timer()
	res = fit(i)
	end = timer()
	print("%d = %d og tók %.4f sek" % (i, res, end-start))