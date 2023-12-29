import math
import graphics
from PIL import Image

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
    
    def getValue(self, t : float) -> list:
        return self.v.addV(Vec(self.g.mult(t)))

class Camera :
    def __init__(self,x : float, y : float, z : float , a : float, b : float , c : float):
        self.pos = Vec([x,y,z])
        self.dir = Vec([a,b,c])
        
    def getRay(self,screen): #screencord
        return Line(self.pos,Vec(screen.subV(self.pos)))
        
class Sphere :
    def __init__(self, pos : Vec, r : float, color : list):
        self.pos : Vec= pos
        self.r : float= r
        self.color: list = color
        self.mirror : float= 0.5

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
        return (b**2) -(4*a*c)
    
    def q_f(self,a : float, b : float, c : float ,det : float, v : int)->float:
        try:
            return (-b + v*math.sqrt(det))/(2*a)
        except:
            print("error")
            return 1000
    
    def null_det(self,a : float, b : float, c : float)->float:
        try:
            return -b / (2*a*c)
        except:
            print("error")
            return 1000
        
    def interact(self, line : Line) -> list:
        old_pos = self.pos

        line.v = Vec(line.v.subV(self.pos))
        self.pos = Vec([0,0,0])

        #if line.v.x()**2 + line.v.y()**2 + line.v.z()**2 > self.r**2:
            #return [0.01, self]
        #self.pos = Vec(self.pos.subV(line.v))
        #line.v = Vec([0,0,0])

        c_tt : float = line.g.x()**2 + line.g.y()**2 + line.g.z()**2
        c_t : float = 2*line.v.x()*line.g.x() + 2*line.v.y()*line.g.y() + 2*line.v.z()*line.g.z()
        c : float = line.v.x()**2 + line.v.y()**2 + line.v.z()**2 - self.r**2

        #print(str(c_tt) + " " + str(c_t) + " " + str(c))

        det : float = self.det(c_tt, c_t, c)

        if det < 0:
            self.pos = old_pos
            line.v = Vec(line.v.addV(self.pos))
            return [0,self]
        
        elif det == 0:
            self.pos = old_pos
            line.v = Vec(line.v.addV(self.pos))
            return [self.null_det(c_tt,c_t,c),self]
        
        elif det > 0:
            s1 : float = self.q_f(c_tt,c_t,c,det,1)
            s2 : float = self.q_f(c_tt,c_t,c,det,-1)

            self.pos = old_pos
            line.v = Vec(line.v.addV(self.pos))

            return [s1,s2,self]
        
    def get_mirror_vec(self, line : Line, data : list) -> Line:
        p : Vec = Vec(line.getValue(data[0]))
        n_vec : Vec = Vec(p.subV(self.pos))
        line.g.norm()
        n_vec.norm()

        r_v : Vec = Vec(line.g.subV(n_vec))
        m_vec : Vec = Vec(n_vec.addV(r_v))
        m_vec.norm()

        m_l : Line = Line(p,m_vec)
        return m_l
    
    def get_m_i(self, line : Line, obj : list):
        data : list = self.interact(line)

        if data[0] == 0:
            return [data]
        
        data.remove(data[-1])
        m_d = abs(data[0])
        if len(data) == 2:
            if abs(data[1]) < m_d:
                m_d = abs(data[1])
        data2 = [m_d]
        m_l : Line = self.get_mirror_vec(line, data2)

        interactions = []
        for i in obj:
            interactions.append(i.interact(m_l))
        
        data.append(self)
        interactions.insert(0, data)
        #print("data " + str(interactions))

        return interactions


        
class Plane :
    def __init__(self, v1 : Vec, v2 : Vec, v3 : Vec):
        self.rV : Vec = self.get_rV(v1,v2,v3) #richtungsvector of the plane
        self.d : float = None
        self.eq = self.get_eq(v1) #equation for checking if a point is on the plane, its a lambda and taking the x y z cord of a point
        self.get_t = self.create_get_t() #alsow  a lambda to get the t paramater of a line but its wrong
        self.color : list = [0,0,255]
        self.mirror : float = 0

        if self.d == int(0):
            self.d = 0.01

    def get_rV(self, v1 : Vec, v2 : Vec, v3 : Vec) -> Vec:
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
            #return -self.d / (d2 + v1.v.x() + v1.v.y() + v1.v.z())
            #print (str(self.d + self.rV.x()*v1.v.x() + self.rV.y()*v1.v.y() + self.rV.z()*v1.v.z()) + "/"+ str(d2))
            return -(self.d + self.rV.x()*v1.v.x() + self.rV.y()*v1.v.y() + self.rV.z()*v1.v.z()) / (d2)
        
    #theory
    # e = ax + by + bz + d = 0

    # plugt in the fromula for a line givs : 
    # vs is the stützvector
    # a * (v_x * t + vs_x) + b * (v_y * t + vs_y) + c * (v_z * t + vs_z) + d = 0

    #solved after t
    # t = -(d+vs_x+vs_y+vs_z) / (av+bv+cv)

    def interact(self, line : Line) -> list:
        #this methode does not need a transformation into unitcordinats, the formula is in global space
        t : float = self.get_t_func(line)
        if t == 1000:
            return [0, self]
        elif t > 0: #implies that the plane is in front of the vector
            return [t,self]
        else:
            return [t,self]
        
class Ligth :
    def __init__(self,pos):
        self.pos : Vec = Vec(pos)
        self.color = [255,255,255]
        
class Scene :
    def __init__(self):
        self.len_x = 200
        self.len_y = 200
        self.win = graphics.GraphWin("raytracing",self.len_x, self.len_y)
        self.camera = Camera(0,0,0,0,1,0)
        self.obj = []
        self.ligth_obj = []

    def add_obj(self, obj):
        self.obj.append(obj)
    
    def add_ligth_obj(self, obj):
        self.ligth_obj.append(obj)

    def get_min_obj(self, data):
        min_value = 10e10
        for i in data:
            if abs(i) < abs(min_value):
                min_value = abs(i)
        return min_value
    
    def is_interacting(self, col : list) -> list:
        dis : float = 10e10
        min_obj = None
        for i in range(len(col)):
            obj_store = col[i][-1]
            col[i].remove(col[i][-1])
            if col[i][0] != 0:
                if self.get_min_obj(col[i]) <= dis:
                    dis = self.get_min_obj(col[i]) #achtung kann auch sein es das zweite objekt ist
                    min_obj = obj_store
        if min_obj == None:
            return [False]
        else:
            return [dis, min_obj]

    
    def interact_obj(self, ray : Line) -> list:
        res = []

        for obj in self.obj:
            res.append(obj.interact(ray))

        return res
    
    def interact_mirror_obj(self, ray : Line) -> list:
        res : list = []

        for obj in self.obj:
            if obj.mirror != 0:
                res.append(obj.get_m_i(ray, self.obj))
        
        con : list= []
        #print(res)
        for i in res:
            con.append(self.is_interacting(i))

        return con
        
    
    def interact_ligth(self, line : Line, data : list) -> bool:
        if data[0] == False:
            return False

        interact_pos : Vec = Vec(line.getValue(data[0]))
        ray : Line; 

        interact : int = 0
        ligth_s : int = 0;

        for i in range(len(self.ligth_obj)):
            ray = Line(interact_pos, Vec(self.ligth_obj[i].pos.subV(interact_pos)))
            ray.g.norm()
            nextpos : Vec = Vec(ray.getValue(-0.1))
            ray.v = nextpos

            for j in self.obj:
                inter = j.interact(ray)
                #print(inter)
                if len(inter) == 2: 
                    if inter[0] != 0 and inter[0] > 0:
                        interact += 1
                elif len(inter) > 2:
                    if inter[0] > 0 and inter[1] > 0:
                        interact += 1
                else:
                    ligth_s += 1
    
        if interact >= len(self.ligth_obj):
            return True
        else:
            return False


    def render_scene(self):
        img = Image.open("C:/Users/l.hefti/Desktop/test-ef5/sky.jpg", "r")
        img_size = img.size
        pix =  img.load()
        
        for i in range(self.len_x):
            i /= self.len_x
            i -= 0.5
            for j in range(self.len_y):
                j /= self.len_y
                j -= 0.5

                #vec : Vec = Vec(self.camera.getRay(Vec([i,1,j]))) #richtungsvektor, eig, self.direction von der kamera
                #ray : Line= Line(self.camera.pos, vec)
                #ray : Line = Line(Vec([i,2,j]),Vec(Vec([i,2,j]).subV(self.camera.pos)))
                #ray : Line = Line(Vec([i,0,j]),Vec([0,1,0]))
                
                ray : Line = Line(self.camera.pos,Vec(Vec([i,0.5,j]).subV(self.camera.pos)))
                ray.g.norm()


                res = self.interact_obj(ray)
                #print(res)

                con = self.is_interacting(res)
                #print(con)

                #(self.interact_mirror_obj(ray))

                ligth : bool= self.interact_ligth(ray, con)


                b : float = 1
                if ligth:
                    b = 0.5

                if con[0]:
                    self.win.plot((i+(0.5))*(self.len_x),(j+(0.5))*(self.len_y), graphics.color_rgb(int(con[1].color[0]*b/con[0]),int(con[1].color[1]*b/con[0]),int(con[1].color[2]*b/con[0])))
                
                if con[0] == 0 and False:
                    #shit code for displacing the image
                    nV : Vec = Vec([1,0,0])
                    r : float = (ray.g.dotP(nV) - 1)
                    r = abs(r)/2
                    if ray.g.x() <= 0:
                        r = -r

                    nV_z = Vec([0,0,1])
                    r2 : float = (ray.g.dotP(nV_z)-1)
                    r2 = abs(r2)/2
                    
                    col = pix[(img_size[0]//2)+ img_size[0] * r/2, img_size[1] - img_size[1]*r2/2]
                    self.win.plot((i+(0.5))*(self.len_x),(j+(0.5))*(self.len_y), graphics.color_rgb(int(col[0]), int(col[1]), int(col[2])))

        print("finish")


s = Scene()
s.add_obj(Sphere(Vec([2,8,0]),1, [255,0,0]))
s.add_obj(Sphere(Vec([-2,8,0]),1,[0,255,0]))
s.add_obj(Plane(Vec([0,0,-1]), Vec([1,0,-1]), Vec([0,1,-1])))
s.add_ligth_obj(Ligth([0,20,-8]))
s.render_scene()

s.win.getMouse()
s.win.close()


k = Sphere(Vec([0,0,0]),2)
v = Line(Vec([-3,-3,0]),Vec([1,1,0]))
print(k.interact(v))


        
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
