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

void nullString(String* s){
    //s->s[s->len] = "11"; //not 0
    s->len = 0;
}

void addString(String* s, String* s2){
    if (testIfStringFull(s, s2->len)){
        createNewString(s);
    }
    strncat(s->s, s2->s, s2->len);
    s->len += s2->len;
}

void addStringLen(String* s, String* s2, int len){
    if (testIfStringFull(s, len)){
        createNewString(s);
    }
    strncat(s->s, s2->s, len);
    s->len += len;
}

void addChar(String* s, char* s2, int len){
    if(testIfStringFull(s, len)){
        createNewString(s);
    }
    strncat(s->s, s2, len);
    s->len += len;
}

void addStringwithOffset(String* s, String* s2, int len, int offset){
    if (testIfStringFull(s, len)){
        createNewString(s);
    }
    strncat(s->s, &s2->s[offset], len);
    s->len += len;
}

void addCharwithOffset(String* s, char* c, int len, int offset){
    if (testIfStringFull(s, len)){
        createNewString(s);
    }
    strncat(s->s, &c[offset], len);
    s->len += len;
}

void printString(String* s){
    printf(s->s);
}

int getIndexOfCharstart(String* s,char c){ //wierd name
    for (int i = 0; i < s->len; i++){
        if (s->s[i] == c){
            return i;
        }
    }
    return -1;
}

int getIndexOfChar(String* s, char c, int offset){
    for (int i = offset; i < s->len; i++){
        if (s->s[i] == c){
            return i;
        }
    }
    return -1;
}

int cmpCharSeq(String* s, int offset, char* c, int len){
    int r = memcmp(&s->s[offset], c, len);
    printf("%d\n",r);
    if (r == 0){
        return 1;
    } else{
        return 0;
    }
}

int getIndexofCharSeq(String* s, char* c, int len){
    for (int i = 0; i < s->len; i++){
        if (cmpCharSeq(s,i,c,len)){
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

String** splitString(String* s, int i){
    String* s1 = initString();
    String* s2 = initString();
    String** list = malloc(2*sizeof(String*));
    
    addStringLen(s1, s, i);
    addStringwithOffset(s2, s, s->len-i, i);
    list[0] = s1;
    list[1] = s2;
    return list;
}

String* getinsertChar(String* s, char* c, int len, int i){
    String** list = splitString(s, i);
    addChar(list[0], c, len);
    addString(list[0], list[1]);
    //memory
    free(list[1]);
    free(s);
    
    return list[0];
}

//imporvements
//realoc
//strncmp
int main() {
    String* s = initString();
    String* s2 = initString();
    char* news = "ababcd";
    char* news2 = "abc";
    addChar(s, news, 5);
    addChar(s2, news2, 3);
    //int r = cmpCharSeq(s,0, news2, 3);
    int r = getIndexofCharSeq(s,news2, 3);
    printf("%d", r);
    return 0;
}
