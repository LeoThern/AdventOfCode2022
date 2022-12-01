max_calories = []
curr_calories = 0
with open('input.txt') as file:
    for line in file:
        if line != '\n':
            curr_calories += int(line)
        else:
            max_calories.append(curr_calories)
            max_calories.sort(reverse=True)
            if len(max_calories) > 3:
                max_calories = max_calories[:3]
            curr_calories = 0
print('Task1:', max_calories[0])
print('Task2:', sum(max_calories))