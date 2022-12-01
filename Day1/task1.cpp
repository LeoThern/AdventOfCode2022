#include <iostream>
#include <string>

int main() {
    int max_calories = 0;
    int curr_calories = 0;
    for (std::string line; std::getline(std::cin, line);) {
        if (!line.empty()){
            curr_calories += stoi(line);
        } else {
            if (curr_calories > max_calories)
                max_calories = curr_calories;
            curr_calories = 0;
        }
    }
    std::cout << max_calories << std::endl;
    return 0;
}