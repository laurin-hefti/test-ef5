// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    char* s;
    int len;
    int maxlen;
} String;

String* initString(){
    String* newstr = malloc(sizeof(String));
    newstr->s = malloc(20*sizeof(char));
    newstr->len = 0;
    newstr->maxlen = 20;
    return newstr;
}

int testIfStringFull(String* s, int size){
    if (s->maxlen < s->len + size){
        return 1;
    }else{
        return 0;
    }
}

void createNewString(String* s){
    char* newCharpointer = malloc(s->maxlen*2);
    s->s = strcpy(newCharpointer, s->s);
}

void add(String* s, String* s2){
    if (testIfSTringFull(s, s2-len)){
        createNewString();
    }
    strncat(s->s, s2->s, s2->len);
}

int getIndxOfChar(String* s,char c){
    for (int i = 0; i < s->len; i++){
        if (s->s[i] == c){
            return i;
        }
    }
    return -1;
}

int getIndexOfChar(String* s, char c, int index){
    for (int i = index; i < s->len; i++){
        if (s->s[i] == c){
            return i;
        }
    }
    return -1;
}

int[]* getIndexListofChar(String* s, char c){
    int res = 0;
    int num = 0;
    while(res != -1){
        res = getIndexofChar(s, c, res);
        if (res != -1){
            num += 1;
        }
    }
    int[num];
    
}

int main() {
    return 0;
}
