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
    s->maxlen *= 2;
}

void addString(String* s, String* s2){
    if (testIfStringFull(s, s2->len)){
        createNewString(s);
    }
    strncat(s->s, s2->s, s2->len);
}

void addChar(String* s, char* s2, int len){
    if(testIfStringFull(s, len)){
        createNewString(s);
    }
    strncat(s->s, s2, len);
}

void addStringwithOffset(String* s, String* s2, int len, int offset){
    strncat(s->s, s2-s[offset], len);
}

void printString(String* s){
    printf(s->s);
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

int* getIndexListofChar(String* s, char c){
    //first element is the len of the list
    int res = 0;
    int num = 0;
    while(res != -1){
        res = getIndexOfChar(s, c, res);
        if (res != -1){
            num += 1;
        }
    }
    int* list = malloc((num+1)*sizeof(int));
    list[0] = num;
    res = 0;
    for (int i = 0; i < num; i++){
        list[i+1] = getIndexOfChar(s, c, res);
        res = list[i+1];
    }
    return list;
}

String* splitString(String* s, int i){
    String* s1 = malloc(i*sizeof(char));
    String* s2 = malloc((s-len - i)* sizeof(char));
    String* list = malloc(2*sizeof(String*));
    
    addString(s1, s->s, s->len-i);
    //addStringwithOffset(s2, s->[])
}

 insertChar(String* s, char c){
    
}

int main() {
    String* s = initString();
    char* news = "abc";
    char* news2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    addChar(s, news, 3);
    addChar(s, news2, 30);
    printString(s);
    return 0;
}
