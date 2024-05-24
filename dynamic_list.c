//dynamic template list

#include <stdio.h>
#include <stdlib.h>

//external definition
#define data_name d64
#define data_type double

//start file

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

void addObj(data_name* obj, data_type d)
{
    obj->list[obj->len] = d;
    obj->len += 1;
    //def if it is pointer
}

int main(){
    d64 list = newd64();
    addd64(&list, 4);
    addd64(&list, 6);
    printf("%d", list.list[1]);
    return 0;
}
