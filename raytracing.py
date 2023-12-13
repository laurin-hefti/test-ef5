import math
import graphics

class Vec :
    def __init__(self, pos):
        self.cord : list = pos

    def x(self, set : bool = False) -> float:
        if set == False:
            return self.cord[0]
        else:
            self.cord[0] = set
            return self.cord[0]
        
    def y(self, set = False) -> float:
        if set == False:
            return self.cord[1]
        else:
            self.cord[1] = set
            return self.cord[1]
    
    def z(self, set = False) -> float:
        if set == False:
            return self.cord[2]
        else:
            self.cord[2] = set
            return self.cord[2]

    def dotP(self, vec) -> float:
        return self.cord[0]*vec.cord[0] + self.cord[1]*vec.cord[1] + self.cord[2]*vec.cord[2]
            
    def crosP(self,vec) -> float:
        return [self.cord[1]*vec.cord[2]-self.cord[2]*vec.cord[1],
            self.cord[2]*vec.cord[0]-self.cord[0]*vec.cord[2],
            self.cord[0]*vec.cord[1]-self.cord[1]*vec.cord[0]]
            
    def addV(self,vec) -> list:
        return [self.cord[0]+vec.cord[0],self.cord[1]+vec.cord[1],self.cord[2]+vec.cord[2]]
    
    def subV(self,vec) -> list:
        return [self.cord[0]-vec.cord[0],self.cord[1]-vec.cord[1],self.cord[2]-vec.cord[2]]
    
    def getLen(self) -> float:
        return (self.cord[0]**2+self.cord[1]**2+self.cord[2]**2)**0.5
        
    def norm(self) -> None:
        l : float= self.getLen()
        self.cord = [self.cord[0]/l,self.cord[1]/l, self.cord[2]/l]
        
    def mult(self,a) -> list:
        return [self.cord[0]*a, self.cord[1]*a, self.cord[2]*a]

class Line :
    def __init__(self, v : Vec, g : Vec):
        self.v : Vec = v              #stützvektor
        self.g : Vec = g              #richtungsvektor
    
    def getValue(self, t : float) -> Vec:
        return self.v.addV(Vec(self.g.mult(t)))

class Camera :
    def __init__(self,x : float, y : float, z : float , a : float, b : float , c : float):
        self.pos = Vec([x,y,z])
        self.dir = Vec([a,b,c])
        
    def getRay(self,screen): #screencord
        return Line(self.pos,Vec(screen.subV(self.pos)))
        
class Sphere :
    def __init__(self, pos : Vec, r : float):
        self.pos : Vec= pos
        self.r : float= r
        self.color: str = "red";

    # quadratic formula
    # -b +/- sqrt(b^2 - 4ac)
    # ----------------------
    #         2ac

    # sphere function
    # x^2 + y^2 + z^2 = r^2

    # line func
    # f(t) = a + bt

    # line in spherefunc
    # (ax + bxt)^2 + (ay + byt)^2 + (az + bzt)^2 - r^2 = 0

    # multiplied out
    # (bx^2+by^2+bz^2)t^2 + (2ax*bx + 2ay*by + 2az*bz)t + (ax^2 + ay^2 + az^2 - r^2) = 0

    #determinante
    def det(self, a : float, b : float, c : float)->float:  
        return b**2 -4*a*c
    
    def q_f(self,a : float, b : float, c : float ,det : float, v : int)->float:
        try:
            return (-b + v*math.sqrt(det))/(2*a*c)
        except:
            print("error")
            return 1000
    
    def null_det(self,a : float, b : float, c : float)->float:
        try:
            return -b / (2*a*c)
        except:
            print("error")
            return 1000
        
    def interact(self, line : Line):
        #line = Line(Vec(line.v.subV(self.pos)),line.g)
        old_pos = self.pos

        line.v = Vec(line.v.subV(self.pos))
        #print(line.v.cord)
        self.pos = Vec([0,0,0])
        #self.pos = Vec(self.pos.subV(line.v))
        #print("int " + str(line.v.cord))
        #line.v = Vec([0,0,0])
        #print("int " + str(line.g.cord))

        c_tt : float = line.g.x()**2 + line.g.y()**2 + line.g.z()**2
        c_t : float = 2*line.v.x()*line.g.x() + 2*line.v.y()*line.g.y() + 2*line.v.z()*line.g.z()
        c : float = line.v.x()**2 + line.v.y()**2 + line.v.z()**2 - self.r**2

        #print(str(c_tt) + " " + str(c_t) + " " + str(c))

        det : float = self.det(c_tt, c_t, c)

        if det < 0:
            self.pos = old_pos
            return [0]
        
        elif det == 0:
            self.pos = old_pos
            return [self.null_det(c_tt,c_t,c)]
        
        elif det > 0:
            s1 : float = self.q_f(c_tt,c_t,c,det,1)
            s2 : float = self.q_f(c_tt,c_t,c,det,-1)

            self.pos = old_pos

            return [s1,s2]
        
class Plane :
    def __init__(self, v1 : Vec, v2 : Vec, v3 : Vec):
        self.rV : Vec = self.get_rV(v1,v2,v3) #richtungsvector of the plane
        self.d : float = None
        self.eq = self.get_eq(v1) #equation for checking if a point is on the plane, its a lambda and taking the x y z cord of a point
        self.get_t = self.create_get_t() #alsow  a lambda to get the t paramater of a line but its wrong

    def get_rV(self, v1 : Vec, v2 : Vec, v3 : Vec):
        n_v1 : Vec = Vec(v2.subV(v1))
        n_v2 : Vec = Vec(v3.subV(v1))

        cp : Vec = Vec(n_v1.crosP(n_v2))

        return cp
    
    def get_eq(self, v1 : Vec):
        d : float = -(self.rV.x() * v1.x() + self.rV.y() * v1.y() + self.rV.z() * v1.z())
        self.d = d
        return lambda x, y, z : self.rv.x() * x + self.rv.y() * y + self.rv.z() * z - d
    
    def create_get_t(self): #not correct the stützvector is missing
        return lambda x, y, z : -self.d / (self.rV.x() * x + self.rV.y() * y + self.rV * z)
    
    def get_t_func(self, v1 : Line) -> float:
        #v = stützvekotr, g = richtugnsvektor
        d2 = self.rV.x() * v1.g.x() + self.rV.y() * v1.g.y() +self.rV.z() * v1.g.z() # this is like the determinant of the quadratic formula
        if d2 < 10e-5:
            return 1000
        else:
            return -self.d / (d2 + v1.v.x() + v1.v.y() + v1.v.z())
    
    #theory
    # e = ax + by + bz + d = 0

    # plugt in the fromula for a line givs : 
    # vs is the stützvector
    # a * v_x * t + vs_x + b * v_y * t + vs_y + c * v_z * t + vs_z + d = 0

    #solved after t
    # t = -d / (av+bv+cv)

    def interact(self, line : Line) -> list:
        #this methode does not need a transformation into unitcordinats, the formula is in global space
        t : float = self.get_t_func(line)
        if t == 1000:
            return [0]
        if t > 0: #implies that the plane is in front of the vector
            return [t]

        
class Scene :
    def __init__(self):
        self.len_x = 100
        self.len_y = 100
        self.win = graphics.GraphWin("raytracing",self.len_x, self.len_y)
        self.camera = Camera(0,0,0,0,1,0)
        self.obj = []

    def add_obj(self, obj):
        self.obj.append(obj)

    def find_min_dist(self,res)->list:
        i : int = 0
        min_i : int = 0
        minn : float= abs(res[0][0])
        for obj in res:
            if min(obj) < minn:
                minn = abs(min(obj))
                min_i += i
            i += 1
        return [minn, min_i]

    def render_scene(self):
        for i in range(self.len_x):
            i /= self.len_x
            i -= 0.5
            for j in range(self.len_y):
                j /= self.len_y
                j -= 0.5

                #vec : Vec = Vec(self.camera.getRay(Vec([i,1,j]))) #richtungsvektor, eig, self.direction von der kamera
                #ray : Line= Line(self.camera.pos, vec)
                #ray : Line = Line(Vec([i,2,j]),Vec(Vec([i,2,j]).subV(self.camera.pos)))
                ray : Line = Line(self.camera.pos,Vec(Vec([i,1,j]).subV(self.camera.pos)))
                ray.g.norm()
                #print(ray.g.cord)
                #ray : Line = Line(Vec([i,0,j]),Vec([0,1,0]))
                #print(vec.cord)
                res = []

                for obj in self.obj:
                    res.append(obj.interact(ray))

                #print(res)
                con : bool = False
                for ii in res:
                    if ii != [0]:
                        con = True
                        break
                    
                if con == True:
                    #print(res)
                    pt  = graphics.Point((i+(0.5))*(self.len_x),(j+(0.5))*(self.len_y))
                    pt.draw(self.win)

                #min_dist = self.find_min_dist(res)


        print("finish")


s = Scene()
s.add_obj(Sphere(Vec([0,10,-2]),1))
s.add_obj(Plane(Vec([0,0,0]), Vec([1,0,0]), Vec([0,1,0])))
s.render_scene()

s.win.getMouse()
s.win.close()

        
#win = graphics.GraphWin("test",100,100)
#for i in range(100):
    #for j in range(100):
        #pt = graphics.Point(i,j)
        #pt.draw(win)
#pt = graphics.Point(50,50)
#win.getMouse()
#win.close()
#line = Line(Vec([-20,0,0]), Vec([1,0,0]))
#s = Sphere(Vec([0,0,0]), 2)
#sp = s.interact(line)
#print(sp)
#print(line.getValue(sp[0]))
