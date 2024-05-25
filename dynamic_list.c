//dynamic template list

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//external definition
#define data_name i64
#define data_type int

//start file

//usefule print not finish
#define print(cont) printf(#cont)
//default better error
#ifndef data_name
#define data_name d64
#endif
#ifndef data_type
#define data_type double
#endif

//#undef for more
#define connect(x,y) x##y
#define comcon(x,y) connect(x,y)

#define createList connect(createList,data_name)
#define newObj comcon(new, comcon(,data_name)) // auch connect
#define addObj comcon(add, comcon(,data_name))

typedef struct data_name {
    data_type* list;
    int len;
    int size;
} data_name;

data_type* createList(int mult)
{
    data_type* list_ptr = malloc(sizeof(data_type)*mult);
    return list_ptr;
}

data_name newObj()
{
    data_type* list = createList(20);
    data_name obj = {list,0,20};
    return obj;
}

int checkIfFull(data_name* obj)
{
    if (obj->len + 1 >= obj->size){
        return 1;
    }
    return 0;
}

void copyContent(data_name* obj)
{
    data_type* list = createList(obj->size*2);
    memcpy(list, obj->list, obj->size*sizeof(data_type));
    free(obj->list);
    obj->list = list;
    obj->size *= 2;
}

void addObj(data_name* obj, data_type d)
{
    if (checkIfFull(obj))
    {
        copyContent(obj);
    }
    obj->list[obj->len] = d;
    obj->len += 1;
    //def if it is pointer
}


int main(){
    i64 list = newi64();
    for (int i = 0; i < 30; i++){
        addi64(&list, i);
    }
    printf("%i ", list.list[24]);
    return 0;
}
