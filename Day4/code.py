def is_inside(rangeA, rangeB):
	if rangeA[0] >= rangeB[0] and rangeA[1] <= rangeB[1]:
		return True
	return False

def is_overlap(rangeA, rangeB):
	if rangeA[1] < rangeB[0] or rangeB[1] < rangeA[0]:
		return False
	return True

def main():
	contain_count = 0
	overlap_count = 0
	with open('input.txt') as file:
		for line in file:
			line = line.strip().split(',')
			firstRange = [int(i) for i in line[0].split('-')]
			secondRange = [int(i) for i in line[1].split('-')]
			if is_inside(firstRange, secondRange) or is_inside(secondRange, firstRange):
				contain_count += 1
			if is_overlap(firstRange, secondRange):
				overlap_count += 1
	print(f"Total Task1: {contain_count}")
	print(f"Total Task2: {overlap_count}")

if __name__ == "__main__":
	main()