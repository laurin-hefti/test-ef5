//dynamic template list

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

#define createList connect(createList,data_name)

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

data_name connect(new,data_name)()
{
    data_type* list = createList(20);
    data_name obj = {list,0,20};
    return obj;
}

int main(){
    d64 o = newdata_name();
    return 0;
}
