#include <stdio.h>
#include <stdlib.h>


int main(){
  int pairs, i;
  char** strings;
  // Read in number of pairs.
  scanf("%d", &pairs);
  // Allocate memory
  strings = (char**)calloc(2*pairs, sizeof(char));
  // Read in pairs
  for(i = 0; i < 2*pairs;i++){
    strings[i] = (char*)calloc()
  }
  return 0;
}
