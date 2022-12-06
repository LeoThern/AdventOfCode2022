def index_x_unique(signal, x):
	curr_values = list(signal[0:x-1])
	for i in range(x-1,len(signal)):
		curr_values.append(signal[i])
		if len(set(curr_values)) == x:
			return i + 1
		curr_values.pop(0)

def main():
	with open('input.txt') as file:
		signal = file.read()
	print(f"Task1 (4 unique): {index_x_unique(signal, 4)}")
	print(f"Task2 (14 unique): {index_x_unique(signal, 14)}")

if __name__ == "__main__":
	main()