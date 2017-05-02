#include <stdio.h>
#include <stdlib.h>


int   lenMaxAlter(char *, int);
char* delChar(char* , int*, char);

int main(){
  char *s, *new_s;
  int i, n;
  // Scan size
  scanf("%d", &n);
  n++;
  // Allocate space
  s = (char*)malloc(n * sizeof(char));
  // Scan string
  for(i = 0; i < n; i++){
    scanf("%c", &s[i]);
  }
  // Delet character
  new_s = delChar(s, &n, 'h');
  // Print string
  for(i = 0; i < n; i++){
    printf("%c", new_s[i]);
  }
  return 0;
}


// int lenMaxAlter(char * s, int n);

char* delChar(char* s, int *n, char c){
  char* new_s;
  int i, instances, k;
  // Count instances
  for(instances = i = 0; i < *n; i ++){
    if(s[i] == c) instances++;
  }
  // Allocate space
  new_s = (char*) malloc((*n - instances) * sizeof(char));
  // Copy array
  for(k = i = 0; i < *n; i++){
    if(s[i] != c){
      new_s[k] = s[i];
      k++;
    }
  }
  // Update length
  *n = *n - instances;
  // Return array
  return s;
};
