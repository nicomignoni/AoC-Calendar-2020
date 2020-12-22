#include <stdlib.h>
#include <stdio.h>
#define LINES 323
#define ROWS 32
#define TREE '#'
#define STEP 3

FILE *file;
int pos = 0;
int counter = 0;
char str[ROWS];

int main() {
    file = fopen("day_3.txt", "r");
    
    // First line is not important
    fgets(str, ROWS + 2, file);

    for (int i = 1; i < LINES + 1; i++) {
        fgets(str, ROWS + 2, file);
        
        pos = (pos + STEP) % (ROWS - 1);
        if (str[pos] == TREE) { counter++; }
        str[pos] = 'X';
    }    
    printf("Counter: %d", counter);;
    return 0;
}
