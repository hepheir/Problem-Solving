#include <stdio.h>
#include <stdlib.h>

char* inputFilePath = "/Users/hepheir/_git/Facebook-Hacker-Cup/2020/Qualification Round/D1 - Running on Fumes - Chapter 1/data/sample_input.txt";
char* outputFilePath = "/Users/hepheir/_git/Facebook-Hacker-Cup/2020/Qualification Round/D1 - Running on Fumes - Chapter 1/data/sample_output.txt";

struct Node {
    struct Node* next;
    unsigned int gasCost;
};
typedef struct Node City;


int main() {
    unsigned int T;
    unsigned int N, M;
    char buffer[32];

    City cities[1000000];
    FILE *fi, *fo;

    int i;

    
    fi = fopen(inputFilePath, "r");
    fo = fopen(outputFilePath, "w");

    // Get input
    fgets(buffer, 32, fi); sscanf(buffer, "%d", &T);
    fgets(buffer, 32, fi); sscanf(buffer, "%d %d", &N, &M);
    for (i = 0; i < N; i++) {
        fgets(buffer, 32, fi); sscanf(buffer, "%d", &(cities[i].gasCost));
    }

    fclose(fi);
    fclose(fo);
}