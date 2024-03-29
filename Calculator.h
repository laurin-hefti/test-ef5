#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    char* s;
    int len;
    int maxlen;
} String;

String* initString(){
    String* newstr = (String*) malloc(sizeof(String));
    newstr->s = (char*) malloc(20*sizeof(char));
    newstr->len = 0;
    newstr->maxlen = 20;
    return newstr;
}

int lenChar(char* c){
    return strlen(c);
}

int testIfStringFull(String* s, int size){
    if (s->maxlen < s->len + size){
        return 1;
    }else{
        return 0;
    }
}

void createNewString(String* s){
    char* newCharpointer = (char*) malloc(s->maxlen*2);
    s->s = strcpy(newCharpointer, s->s);
    s->maxlen *= 2;
}

void nullString(String* s){
    s->s[0] = '\0';
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

int getIndexOfCharstart(String* s,char* c){ //wierd name
    for (int i = 0; i < s->len; i++){
        if (s->s[i] == *c){
            return i;
        }
    }
    return -1;
}

int getIndexOfChar(String* s, char* c, int offset){
    for (int i = offset; i < s->len; i++){
        if (s->s[i] == *c){
            return i;
        }
    }
    return -1;
}

int cmpCharSeq(String* s, int offset, char* c, int len){
    int r = memcmp(&s->s[offset], c, len);
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

int* getIndexListofChar(String* s, char* c){
    //first element is the len of the listed
    int res = 0;
    int num = 0;
    while(res != -1){
        res = getIndexOfChar(s, c, res); //not good while loop
        if (res == -1){
            break;
        }
        if (res != -1){
            num += 1;
            res += 1;
        }
    }
    int* list = (int*) malloc((num+1)*sizeof(int));
    list[0] = num;
    res = 0;
    for (int i = 0; i < num; i++){
        list[i+1] = getIndexOfChar(s, c, res);
        res = list[i+1]+1; // notlösung
    }
    return list;
}

String** splitString(String* s, int i){
    String* s1 = initString();
    String* s2 = initString();
    String** list = (String**) malloc(2*sizeof(String*));
    
    addStringLen(s1, s, i);
    addStringwithOffset(s2, s, s->len-i, i);
    list[0] = s1;
    list[1] = s2;
    return list;
}

String** splitStringOffset(String* s, int i, int gap){
    String* s1 = initString();
    String* s2 = initString();
    String** list = (String**)malloc(2*sizeof(String*));
    
    addStringLen(s1, s, i);
    addStringwithOffset(s2, s, s->len-i, i+gap);
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

String* getreplaceChar(String* s, char* oldc, int lenold, char* charnew, int lennew){
    int i = getIndexofCharSeq(s, oldc, lenold);
    String** list = splitStringOffset(s, i, lenold);
    addChar(list[0], charnew, lennew);
    addString(list[0], list[1]);
    
    free(list[1]);
    free(s);
    
    return list[0];
}

//improvements
//realoc
//strlen
//strncmp

//first parser: replace sqrt with &
String* formatToMathInput(String* s){
    char* sqrts;
    char* sqrtsnew;
    sqrts = (char*)"sqrt";
    sqrtsnew = (char*)"&";
    int res = 0;
    //res = getIndexofCharSeq(s, sqrts,4);
    while (res != -1){
        res = getIndexofCharSeq(s, sqrts, 4); //not useful while loop
        if (res == -1){
            break;
        }
        s = getreplaceChar(s, sqrts, 4, sqrtsnew, 1);
    }
    return s;
}

char* mul;
char* div_;
char* add;
char* sub;
char* pow_;
char* root;
char* startc;
char* endc;

int* searchNearestIndexDown(int** list, int len, int index, int lenstring){
    int nearestIndex = 0;
    int diverenz = lenstring;
    int listindex = -1;
    for (int i = 0; i < len; i++){
        for (int j = 1; j <= list[i][0]; j++){
            if (abs(list[i][j] - index) < diverenz &&
                list[i][j] != index && list[i][j] < index){
                    //printf("a:%d ",  diverenz);
                    nearestIndex = list[i][j];
                    diverenz = abs(list[i][j] - index);
                    //printf("b: %d ", diverenz);
                    listindex = i;
                }
        }
    }
    int* res = (int*)malloc(sizeof(int)*2);
    res[0] = nearestIndex;
    res[1] = listindex;
    return res;
    //ist int* und int[] in c und cpp das gleiche?
}

int* searchNearestIndexUp(int** list, int len, int index, int lenstring){
    int nearestIndex = 0;
    int diverenz = lenstring;
    int listindex = -1;
    for (int i = 0; i < len; i++){
        for (int j = 1; j <= list[i][0]; j++){
            if (abs(list[i][j] - index) < diverenz &&
                list[i][j] != index && list[i][j] > index){
                    //printf("a:%d ",  diverenz);
                    nearestIndex = list[i][j];
                    diverenz = abs(list[i][j] - index);
                    //printf("b: %d ", diverenz);
                    listindex = i;
                }
        }
    }
    int* res = (int*)malloc(sizeof(int)*2);
    res[0] = nearestIndex;
    res[1] = listindex;
    return res;
    //ist int* und int[] in c und cpp das gleiche?
}
//statemachine reaplace

//testing fuction
void printList(int* list){
    //fisrt element len of list
    printf("list: ");
    for (int i = 0; i <= list[0]; i++){
        printf("%d ", list[i]);
    }
}

String* applyControl(String* s){
    int len = 5; // cono and conc must not be evaluated
    int len2 = 7;
    //idea not all will be evaluated but position will be
    //int* c = searchNearestIndexUp(list, len, 5, s->len);
    //printf("%d ", c[0]);
    //printf("%d ", c[1]);
    
    //return s;
    for (int i = 0; i < len; i++){
        
        int* popm = getIndexListofChar(s, mul);
        int* popd = getIndexListofChar(s, div_);
        int* lopa = getIndexListofChar(s, add);
        int* lops = getIndexListofChar(s, sub);
        int* powopp = getIndexListofChar(s, pow_);
        int* powops = getIndexListofChar(s, root);
        //exeption
        int* cono = getIndexListofChar(s, endc); //not used
        int* conc = getIndexListofChar(s, startc);//not used
    
        int* list[] = {powopp, popm, popd, lopa, lops, cono, conc}; // may alsow root
    
        for (int j = 1; j <= list[i][0]; j++){
         int* downChar = searchNearestIndexDown(list, len2, list[i][j], s->len);
         int* upChar = searchNearestIndexUp(list, len2, list[i][j], s->len);
         
         if (downChar[0] == 0){
             //wenn keine operator sich unten befindet, dann setzte am anfang einen 
             s = getinsertChar(s,startc,1,0);
         }else if (downChar[1] == 5){
             //for case when )<- happend then search corresponding ( or go to end
             int hav_end = 0;
             int end = 0;
             int counter = 0; //must need wenn other braket is open
             for (int k = 1; k <= list[6][0]; k++){
                 //must be list 6
                 /*
                 if (s->s[list[6][k]] == "("){
                     counter += 1;
                 }
                 if (s->s[list[6][k]] == ")"){
                     counter -= 1;
                 }
                 */
                 
                 if (list[6][k] < downChar[0] && counter == 0){
                     hav_end = 1;
                     end = list[6][k];
                     break;
                     
                 }
             }
            if (hav_end){
                //wenn wer ein ) gefunden hat einzsetzten
             s = getinsertChar(s, startc, 1, end+1);
             //myplus one
             //printf("test");
            }else{
                //keine ahnung
                //s = getinsertChar(s, startc, 1, 0);
             }
            //jump to other end of list
         } else if (downChar[1] == 6){
             //wenn anfang control ( dann neues seutzen
             //s = getinsertChar(s, startc,1, *downChar); //my not realy useful
         }else{
            s = getinsertChar(s, startc, 1, downChar[0]+1);
         }
         //printf("%d", downChar[1]);
         if(upChar[0] == 0){
             //fall wenn kein kontroloperator sich oben befindet dann setze oben einen hin
            addChar(s, endc, 1);
         }else if (upChar[1] == 5){
             //s = getinsertChar(s, endc, 1, *upChar+1);
         }else if (upChar[1] == 6){
             int have_end = 0;
             int end = 0;
             for (int k = 1; k <= list[5][0]; k++){
                 if (list[5][k] > upChar[0]){
                     have_end = 1;
                     end = list[5][k];
                     break;
                 }
             }
             if (have_end){
                 //s = getinsertChar(s, endc, 1, end+1);
             }else{
                 //addChar(s, endc, 1);
             }
         }else {
            s = getinsertChar(s, endc, 1, upChar[0]+1);
         }
        }
    }
    
    return s;
}

int main() {
    mul = (char*) "*";
    div_ = (char*)"/";
    add = (char*)"+";
    sub = (char*)"-";
    pow_ = (char*)"^";
    root = (char*)"^";
    endc = (char*)")";
    startc = (char*)"(";

    String* s = initString();
    char* testc = "22b+dab*5b665+2*55";
    addChar(s, testc, lenChar(testc));
    s = applyControl(s);
    printString(s);
    //printf("%d ", lenChar(testc));
    //addChar(s, testc, lenChar(testc));  // -> (2+(3*2)
    //s = formatToMathInput(s);
    //printString(s);
    //char* charr = "8";
    //int* ii = getIndexListofChar(s, charr);
    //printf("%d", ii[0]);
    
    //applyControl(s);
    
    return 0;
}
