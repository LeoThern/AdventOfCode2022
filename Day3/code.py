items_by_priorities = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def common_item_TASK1(line):
    total_priority = 0
    firstcompartment, secondcompartment = line[:len(line)//2], line[len(line)//2:]
    for item in firstcompartment:
        if item in secondcompartment:
            return items_by_priorities.index(item)

def main():
    with open('input.txt') as file:
        lines = list(file)
    i = 0
    #Task 1
    total_priority = 0
    for line in lines:
        total_priority += common_item_TASK1(line)
    print(f"Total Task1: {total_priority}")

    #Task 2
    total_priority = 0
    while i < len(lines):
        line1 = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        for item in line1:
            if (item in line2) and (item in line3):
                total_priority += items_by_priorities.index(item)
                break
        i += 3
    print(f"Total Task2: {total_priority}")

if __name__ == '__main__':
    main()