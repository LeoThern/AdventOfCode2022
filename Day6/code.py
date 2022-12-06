def index_four_different(signal):
	curr_values = list(signal[0:3])
	for i in range(3,len(signal)):
		curr_values.append(signal[i])
		if len(set(curr_values)) == 4:
			return i + 1
		curr_values.pop(0)

def main():
	with open('input.txt') as file:
		index_1 = index_four_different(file.read())
	print(f"Index Task1: {index_1}")

if __name__ == "__main__":
	main()