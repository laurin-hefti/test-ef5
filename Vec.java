//interface Vec;
import Math;

class Vec2{
    private double x;
    private double y;
    
    public Vec2(double x, double y){
        this.x = x;
        this.y = y;
    }
    
    public void setX(double x){
        this.x = x;
    }
    
    public void setY(double y){
        this.y = y;
    }
    
    public double getX(){
        return x; 
    }
    
    public double getY(){
        return y;
    }
    
    public double DotP(Vec2 v){
        return x*v.x + y*v.x;
    }
    
    public void crossP(Vec2 v){
        
    }
    
    public void add(Vec2 v){
        x += v.getX();
        y += v.getY();
    }
    
    public void sub(Vec2 v){
        x -= v.getX();
        y -= v.getY();
    }
    
    public double getLen(){
        return Math.sqrt(x*x + y*y + z*z);
    }
    
    public void skale(double f){
        x *= f;
        y *= f;
    }
    
    public void norm(){
        double len = getLen();
        skale(1.0/len);
    }
}

class Vec3 {
    double x;
    double y;
    double z;
    
    public Vec3(double x, double y, double z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
    
    public void setX(double x){
        this.x = x;
    }
    
    public void setY(double y){
        this.y = y;
    }
    
    public void setZ(double z){
        this.z = z;
    }
    
    public double getX(){
        return x;
    }
    
    public double getY(){
        return y;
    }
    
    public double getZ(){
        return z;
    }
    
    public double dotP(Vec3 v){
        return x*v.x + y*v.y + z*v.z;
    }
    
    public Vec3 crossp(Vec3 v){
        return new Vec3(y*v.getZ() - z*v.getY(),
                        z*v.getX() - x*v.getZ(),
                        x*v.getY() - y*v.getX());
    }
    
    public void add(Vec3 v){
        x += v.getX();
        y += v.getY();
        z += v.getZ();
    }
    
    public void sub(Vec3 v){
        x -= v.getX();
        y -= v.getY();
        z -= v.getZ();
    }
    
    public void skale(double f){
        x *= f;
        y *= f;
        z *= f;
    }
    
    public void getLen(){
        return Math.sqrt(x*x + y*y + z*z);
    }
    
    public void norm(){
        double len = getLen();
        skale(1.0/len);
    }
}

class Polygon{
    
    public Polygon(Vec2 center, Vec2 ... ){
        
    }
}

class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
    }
}
