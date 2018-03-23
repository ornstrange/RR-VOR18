1. græðum ekkert á því afþví hrópmerkt er línulegt
```python
mem = {0:1,1:1}
def memfact(n):
	if n in mem:
		return mem[n]
	else:
		mem[n] = memfact(n-1) * n
		return mem[n]
```

2. 
	a. postfix með list
	```python
	def postfix(s): # þetta virkar fínt
		stack = []
		s = s.split()
		for i in s:
			if i.isdigit():
				stack.append(int(i))
			elif i == "+":
				old = stack.pop()
				stack.append(stack.pop() + old)
			elif i == "-":
				old = stack.pop()
				stack.append(stack.pop() - old)
			elif i == "*":
				old = stack.pop()
				stack.append(stack.pop() * old)
			elif i == "/":
				old = stack.pop()
				stack.append(stack.pop() / old)
		return stack[-1]
	print("2 3 + 4 * =>", postfix("2 3 + 4 *"))
	```
	b. stack class
	```python
	class Stack:
		def __init__(self):
			self.stack = []

		def push(self,x):
			self.stack.append(x)

		def pop(self):
			return self.stack.pop()

		def isempty(self):
			return len(self.stack) == 0
	```

3. queue class
```python
class Queue:
	def __init__(self):
		self.que = []

	def push(self, x):
		self.que.append(x)

	def pop(self):
		return self.que.pop(0)
```

4. ef þú ert að halda utan um gögn sem þú villt að séu í hækkandi röð og þarft að bæta við nýju gildi 
þá er tengdur listi miklu betri O(1), en fylki er O(N)