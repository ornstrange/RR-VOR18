def postfix(s):
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

print("2 3 + 4 * =>"postfix("2 3 + 4 *"))