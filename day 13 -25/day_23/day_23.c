#include <stdio.h>
#define SIZE 9
#define LOOP_SIZE 10

void printCups(int *cups) {
    for (int i = 0; i < SIZE; i++ ) { printf("%d ", cups[i]); }
    printf("\n");
}

int main() {
    int cups[SIZE] = {3, 8, 9, 1, 2, 5, 4, 6, 7};
    //printCups(cups);

    for (int i = 0; i < LOOP_SIZE; i++) {
        int currentCup = cups[0];
        int nextCurrentCup = cups[4];
        int threeCups[]    = {cups[1], cups[2], cups[3]};
        
        int target = currentCup - 1;
        int j = 1;
        while (j < 4) {
            if (target < 1) { target = SIZE; }
            if (cups[j] == target) { 
                target--; 
                j = 1;
            } else {
                j += 1;
            }
        }
        int h = 4;
        int delay = 4;
        while (h < SIZE) {
            cups[h - delay] = cups[h];
            if (cups[h] == target) {
                cups[h - 3] = threeCups[0];
                cups[h - 2] = threeCups[1];
                cups[h - 1] = threeCups[2];
                delay = 1;
            }
            h += 1;
        }
        cups[SIZE - 1] = currentCup;
        printCups(cups);
    }
    return 0;
}
