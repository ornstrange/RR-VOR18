### 1. Finding the quickest route through a supermarket
# Start with the left- or rightmost aisle
# while item not in aisle and unexplored aisles still remain
# go to next aisle to the right / left


### 2. Generate Fibonacci numbers
# Start with 0 in a list
numbers = [0]
# loop forever
while true:
	# if last number is 0
	if numbers[-1] == 0:
		# add 1 to list
		numbers.append(1)
	# else
	else:
		# add last two numbers to get next number in list
		numbers.append(sum(numbers[-2:]))