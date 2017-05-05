#include <stdio.h>
#include <stdlib.h>


int main(){
  char *digit;
  int n, k, i;
  // Scan n, k
  scanf("%d %d", &n, &k);
  // Scan digit
  digit = (char*) malloc(n*sizeof(char));
  for(i = 0; i < n; i++){
    scanf("%c", &digit[i]);
  }
  // Print digit
  for(i = 0; i < n; i++){
    printf("%d", digit[i]);
  }
  // Return
  return 0;
}
