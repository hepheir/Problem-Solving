#include <stdio.h>

#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MAX_N 100001

int max_from_array(int *array, int size) {
    int retval = 0;
    for (int i = 0; i < size; i++) {
        if (array[i] > retval)
            retval = array[i];
    }
    return retval;
}

void swap(int **arr1, int **arr2) {
    int *tmp;

    tmp = *arr1;
    *arr1 = *arr2;
    *arr2 = tmp;
    return;
}

int main(void) {
    int N, K;
    int g;
    int ARRAY1[MAX_N] = {0};
    int ARRAY2[MAX_N] = {0};
    int *now = ARRAY1;
    int *next = ARRAY2;

    scanf("%d %d", &N, &K);
    for (int n = 0; n < N; n++) {
        scanf("%d", &g);
        for (int k = 1; k <= K; k++) {
            next[k] = MAX(now[k], now[k-1]+g);
        }
        swap(&now, &next);
    }
    printf("%d\n", max_from_array(now, N));
    return 0;
}
