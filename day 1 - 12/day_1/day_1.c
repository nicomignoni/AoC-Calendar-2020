#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 200

FILE *file;
int input[SIZE];
char str[10];
char *ptr;

int main() {
    file = fopen("day_1.txt", "r");
    for (int i = 0; i < SIZE; i++) { 
        fgets(str, sizeof str, file); 
        input[i] = strtol(str, &ptr, 10);
    }
    fclose(file);
    
    for (int i = 0; i < SIZE; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            for (int w = j + 1; w < SIZE; w++)
                if (input[i] + input[j] + input[w] == 2020) {
                    printf("Addendum 1: %d, Addendum 2: %d, Addendum 3: %d", 
                          input[i], input[j], input[w]);
                    break;
                } 
         }
    }
    return 0;
}
