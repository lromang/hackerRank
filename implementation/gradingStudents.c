#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int solve(int n, int* grades){
    int i;
    for(i = 0; i < n; i++){
        if(grades[i] >= 38){
            if((grades[i] + 1) % 5 == 0){
                printf("%d\n", grades[i] + 1);
            }else if((grades[i] + 2) % 5 == 0){
                printf("%d\n", grades[i] + 2);
            }else{
                printf("%d\n", grades[i]);
            }
        }else{
            printf("%d\n", grades[i]);
        }
    }
    return 0;
}

int main() {
    int n;
    scanf("%d", &n);
    int *grades = malloc(sizeof(int) * n);
    for(int grades_i = 0; grades_i < n; grades_i++){
       scanf("%d",&grades[grades_i]);
    }
    int result = solve(n, grades);
    return 0;
}
