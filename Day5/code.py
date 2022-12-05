import queue

def parse_file(file_str):
	crates, instructions = file_str.split('\n\n')
	crates = [x[1::4] for x in crates.split('\n')[:-1]]
	stacks = ["".join([y[x] for y in crates]).strip() for x in range(len(crates[0]))]
	instructions = [x.split()[1::2] for x in instructions.split('\n') if x]
	instructions = [{'count':int(i[0]), 'from':int(i[1])-1, 'to':int(i[2])-1} for i in instructions]
	return stacks, instructions

def convert_stack_to_LiFo(stack):
	stack_queue = queue.LifoQueue()
	for crate in stack[::-1]:
		stack_queue.put(crate)
	return stack_queue

def main():
	with open('input.txt') as file:
	   stacks, instructions = parse_file(file.read())

	#Task 1
	stack_queues = list(map(convert_stack_to_LiFo, stacks))
	for instruction in instructions:
		for i in range(instruction['count']):
			crate = stack_queues[instruction['from']].get()
			stack_queues[instruction['to']].put(crate)

	result1 = "".join([stack.get() for stack in stack_queues])
	print('Task 1:', result1)

	#Task 2
	stack_queues = list(map(convert_stack_to_LiFo, stacks))
	temp_que = queue.LifoQueue()
	for instruction in instructions:
		for i in range(instruction['count']):
			crate = stack_queues[instruction['from']].get()
			temp_que.put(crate)
		for i in range(instruction['count']):
			crate = temp_que.get()
			stack_queues[instruction['to']].put(crate)

	result2 = "".join([stack.get() for stack in stack_queues])
	print('Task 2:', result2)

if __name__ == "__main__":
	main()