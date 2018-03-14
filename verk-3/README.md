1.
	* O(n)
	```python
	def on(x):
		return True if x in range(100) else False
	```

	* O(n log(n))
	```python
	def onlogn(list):
		return sort(list)
	```

	* O(n^2)
	```python
	def n2(list):
		for i in range(len(list)):
			for j in range(len(list)):
				if i != j:
					return True if list[i] == list[j]
		return False
	```

	* O(2^n)
	```python
	def fibonacci(x):
		if x <=
			return x
		return fibonacci(x-2) + fibonacci(x-1)
	```
2. 