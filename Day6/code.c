#include <stdio.h>

void push_left(char* arr, int len){
    for (int i = 0; i < len; i++){
        arr[i] = arr[i+1];
    }
}

void print_arr(char* arr, int len){
    printf("[");
    for (int i = 0; i <= len; i++)
        printf("%c,", arr[i]);
    printf("]");
}

int index_x_unique(FILE* file, int x){
    char current_chars[x];
    for (int i = 0; i < x; i++)
        current_chars[i] = fgetc(file);
    
    print_arr(current_chars, x);
    push_left(current_chars, x);
    print_arr(current_chars, x);

    while(1){
        char c = fgetc(file);
        if (c == EOF)
            break;
        //printf("%c",c);
    }
    return 0;
}

int main(void){
    FILE* file_pointer = fopen("input.txt", "r");
    int result = index_x_unique(file_pointer, 5);
    fclose(file_pointer);
    return 0;
}