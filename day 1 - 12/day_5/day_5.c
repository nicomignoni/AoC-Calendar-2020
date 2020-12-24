#include <stdio.h>
#include <string.h>
#define LINES 933
#define ROWS 7
#define COLS 3

int power(int base, int exp) {
    int res = 1;
    for (int i = 0; i < exp; i++) {
        res *= base;
    }
    return res;
}

void getID(char *str, int *currentRow, int *currentCol, int *currentID) {
    int ID;
    int row = 0;
    int col = 0;
    
    for (int i = strlen(str) - 1; i >= ROWS; i--) {
        if (str[i] == 'R') { col += power(2, strlen(str) - 1 - i); }
    }
    
    for (int i = ROWS - 1; i >= 0; i--) {
        if (str[i] == 'B') { row += power(2, ROWS - 1 - i); }
    }
    *currentID = row * 8 + col;
    *currentRow = row;
    *currentCol = col;
}

int main() {
    int maxID = 0;
    FILE *file;
    
    

    file = fopen("day_5.txt", "r");
    
    for (int i = 0; i < LINES; i++) {
        /* Part 1 */
        int currentID, currentRow, currentCol;
        char str[11];
        fgets(str, sizeof str, file);
        
        getID(str, &currentRow, &currentCol, &currentID);
        if (currentID > maxID) {
            maxID = currentID;
        }
    }
    printf("Max ID: %d\n", maxID);
    
    return 0;
}