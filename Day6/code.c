#include <stdio.h>
#include <stdbool.h>

void push_back(char* arr, int len, char value){
    for (int i = 0; i < len - 1; i++){
        arr[i] = arr[i+1];
    }
    arr[len - 1] = value;
}

bool are_all_unique(char* arr, int len){
    for(int i = 0; i < len - 1; i++){
        for(int j = i + 1; j < len; j++){
            if(arr[i] == arr[j])
                return false;
        }
    }
    return true;
}

int index_x_unique(FILE* file, int length){
    char current_chars[length];
    for (int i = 0; i < length; i++)
        current_chars[i] = fgetc(file);

    int i = length;
    while(1){
        if (are_all_unique(current_chars, length))
            return i;

        char c = fgetc(file);
        if (c == EOF)
            break;
        push_back(current_chars, length, c);
        i++;
    }
    return -1;
}

void exec_task1(){
    FILE* file_pointer = fopen("input.txt", "r");
    int result = index_x_unique(file_pointer, 4);
    fclose(file_pointer);
    printf("Task1 (4 unique): %i\n", result);
}

void exec_task2(){
    FILE* file_pointer = fopen("input.txt", "r");
    int result = index_x_unique(file_pointer, 14);
    fclose(file_pointer);
    printf("Task1 (14 unique): %i\n", result);
}

int main(void){
    exec_task1();
    exec_task2();
    return 0;
}