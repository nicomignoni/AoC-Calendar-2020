#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define LINES 1000

FILE *file;
char str[40];
char letter; 
char pass[30];
unsigned int min, max, counter; // Min, Max
int occ = 0;

void countOccurrences(char *str, char letter) {
    occ = 0;
    for (int i = 0; i < strlen(str); i++){
        if (str[i] == letter) { occ++; }  
    };
}

int main() {
    file = fopen("day_2.txt", "r");
    for (int i = 0; i < LINES; i++) {
        fgets(str, sizeof str, file);
        char *p = str;
        
        // Take the min 
        min = strtol(str, &p, 10);
        p += 1; // Jump the "-"
        
        // Take the max
        max = strtol(p, &p, 10);
        p += 1; // Jump the "space"
            
        // Take the letter
        letter = *p;
        p += 3; // Jump the ":space"
        
        // Take the password
        int c = 0;
        while (*p != '\0') {
            pass[c] = *p; 
            p++; c++;
        }
        pass[c] = '\0';
        
        printf("%d - Min: %d, Max: %d, Pass: %s\n", i, min, max, pass);

        countOccurrences(pass, letter);
        if (occ >= min && occ <= max) { counter++; }
    }
    fclose(file);
    printf("%d", counter);
    return 0;
}