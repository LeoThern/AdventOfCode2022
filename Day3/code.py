items_by_priorities = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def main():
    total_priority = 0
    with open('input.txt') as file:
        for line in file:
            firstcompartment, secondcompartment = line[:len(line)//2], line[len(line)//2:]
            for item in firstcompartment:
                if item in secondcompartment:
                    total_priority += items_by_priorities.index(item)
                    break
    
    print(f"Total: {total_priority}")

if __name__ == '__main__':
    main()