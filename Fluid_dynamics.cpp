#include <iostream>
#include <math.h>


typedef struct TwoNum{
    double x;
    double y;
};

class Cell {
  int x;
  int y;
  double preasure;
  
  double radius = 10;
  
  double getD(int x, int y){
      return sqrt((this->x-x)*(this->x-x) + (this->y-y)*(this->y-y));
  }
  
public:
 
  Cell(int x, int y, int start_p){
      this->x = x;
      this->y = y;
      this->preasure = start_p;
  }
  
   TwoNum calculate_d(Cell* store, int len){
       double f[2] = {0,0};
       
        for (int i = 0; i < len; i++){
            double d = getD(store[i].x, store[i].y); 
            if (d < radius)
            {
                if (store[i].preasure < this->preasure){
                    TwoNum dir = {0,0};
                    return dir;
                } //keine saugwirkung der zelle
                
                int d_x = store[i].x - this->x;
                int d_y = store[i].y - this->y;
                double dif = abs(this->preasure-store[i].preasure);
                
                f[0] += d_x * 1/(d*d) * dif;
                f[1] += d_y * 1/(d*d) * dif;
            }
        }
        TwoNum dir = {f[0], f[1]};
        return dir;
  }
};

int main() {
    
    return 0;
}
