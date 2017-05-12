#include <stdio.h>
#include <stdlib.h>




int main(){
  char *str1, *str2;
  size_t size = 10000;
  int i;
  // Allocate space
  str1 = (char*)malloc(size*sizeof(char));
  // str2 = (char*)calloc(size, sizeof(char));
  // Scan line
  fgets(str1, size, stdin);
  // Print lines
  i = 0;
  while(str1[i] != '\0'){
    printf('%c', str1[i]);
  }
  return 0;
}
