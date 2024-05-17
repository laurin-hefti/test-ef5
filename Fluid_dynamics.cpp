#include <iostream>
#include <math.h>


typedef struct TwoNum{
    double x;
    double y;
};

class Cell {
public:
  int x;
  int y;
  double preasure;
  TwoNum dx; 
  
  double radius = 10;
  
  double getD(int xx, int yy){
      return sqrt(pow(this->x-xx, 2) + pow(this->y-yy, 2));
  }
 
  Cell(int x, int y, int start_p){
      this->x = x;
      this->y = y;
      this->preasure = start_p;
  }
  
   void calculate_d(Cell* store, int len, int self_i){
       double f[2] = {0,0};
       
        for (int i = 0; i < len; i++){
            double d = getD(store[i].x, store[i].y); 
            std::cout << d << " ";
            if (d < radius && i != self_i)
            {
                if (store[i].preasure < this->preasure){
                    TwoNum dir = {0,0};
                    this->dx = dir;
                } //keine saugwirkung der zelle
                
                int d_x = store[i].x - this->x;
                int d_y = store[i].y - this->y;
                double dif = abs(this->preasure-store[i].preasure);
                
                //std::cout << store[i].preasure << " ";
                
                f[0] += d_x * 1/(d*d) * dif;
                f[1] += d_y * 1/(d*d) * dif;
            }
        }
        std::cout << " end" <<std::endl;
        TwoNum dir = {f[0], f[1]};
        this->dx = dir;
  }
  
  void apply_pres(Cell* store, int len, int self_i){
      
      int nearest_cell = 0;
      double dist_to_cell = getD(store[0].x, store[0].y);
      
      for (int i = 0; i < len; i++){
          if (getD(this->dx.x, this->dx.y) < dist_to_cell && i != self_i){
              nearest_cell = i;
              dist_to_cell = getD(this->dx.x, this->dx.y);
          }
      }
      
      double dif = (this->preasure - store[nearest_cell].preasure)/2;
      if (dif > 0){ //my not useful
        store[nearest_cell].preasure += dif;
        this->preasure -= dif;
      }
  }
};

class Field {
    int b;
    int w;
    int grid_s_w;
    int grid_s_b;
    double size;
    Cell* grid;
    int grid_s;
    
public:
    Field(int w, int b, double s){
        this->w = w;
        this->b = b;
        
        int gridsize_w = (int) ((double) w / s);
        int gridsize_b = (int) ((double) b / s);
        grid_s_w = gridsize_w;
        grid_s_b = gridsize_b;
        
        this->grid_s = gridsize_w*gridsize_b;
        
        this->grid = (Cell*)malloc(sizeof(Cell)*grid_s);
        
        for (int i = 0; i < gridsize_w; i++){
            for (int j = 0; j < gridsize_b; j++){
                this->grid[i*j] = Cell{i,j,1};
            }
        }
    }
    
    void all_calc_d(){
        for (int i = 0; i < this->grid_s; i++){
            grid[i].calculate_d(this->grid, this->grid_s, i);
        }
    }
    
    void all_move(){
        for (int i = 0; i < this->grid_s; i++){
            grid[i].apply_pres(this->grid, this->grid_s, i);
        }
    }
    
    void printDensity(){
        for (int i = 0; i < this->grid_s_w; i++){
            for (int j = 0; j < this->grid_s_w; j++){
                std::cout << this->grid[i*j].preasure << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
    
    void printD(){
        for (int i = 0; i < this->grid_s_w; i++){
            for (int j = 0; j < this->grid_s_w; j++){
                std::cout << this->grid[i*j].dx.y << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
};

int main() {
    Field* F = new Field(5,5,1);
    F->all_calc_d();
    F->printDensity();
    F->printD();
    F->all_move();
    F->printDensity();
    //F->all_calc_d();
    //F->all_move();
    //F->printDensity();
    return 0;
}
