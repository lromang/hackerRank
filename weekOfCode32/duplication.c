#include <stdio.h>
#include <math.h>

void printBitNumber(long long a){
  int i = 0;
  while(i < 64){
    printf("%lld", a&1);
    a >>= 1;
    i++;
  }
}

int getBit(long long a, int k){
  return (a & (1 << k)) >> k;
}

int main(){
  long long number;
  int i, times;
  number = 0;
  for(i = 0; i < 11; i++){
    printBitNumber(number);
    printf("\n");
    times  = pow(2, i);
    number = (number<<times) + ((0xffffffff - number) ^ (0xffffffff << times));
  }

  return 0;
}
