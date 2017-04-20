#include <stdio.h>
#include <stdlib.h>

char* compress(char*, int);
char* rempRep(char*, int, int);
void printString(char*);

int main(){
  char*  string;
  size_t sSize = 101;
  string = (char*)calloc(sSize, sizeof(char));
  fgets(string, sSize, stdin);
  // getline(&string, &sSize, stdin);
  string = compress(string, sSize);
  if(string[1] != '\0'){
    printString(string);
  }else{
    printf("Empty String");
  }
}

char* rempRep(char* string, int index, int n){
  int i, k;
  char* newString = (char*)malloc(n*sizeof(char));
  for(k = i = 0; string[i] != '\0'; i++){
    if(i != index && i != index - 1){
      newString[k] = string[i];
      k++;
    }
  }
  return newString;
}

void printString(char* string){
  int i;
  for(i = 0; string[i] != '\0'; i++){
    printf("%c", string[i]);
  }
}

char* compress(char* string, int n){
  int reps, i;
  char prev;

  for(reps = 1; reps;){
    reps = 0;
    prev = string[0];
    i    = 1;
    if(string == '\0'){
      return '\0';
    }
    while(string[i] != '\0'){
      if(string[i] == prev){
        string = rempRep(string, i, n);
        reps   = 1;
        break;
      }
      prev = string[i];
      i++;
    }
  }
  return string;
}
