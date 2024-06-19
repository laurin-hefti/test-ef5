struct cord {
    x: f64,
    y: f64,
}

struct Pendel {
    length: f64,
    angle: f64,
    vel: f64,
    acc: f64,
    mass: f64,
}

impl Pendel {
    fn new(l: f64, a: f64, m: f64) -> Pendel {
        return Pendel {length: l, angle: a, vel: 0.0, acc: 0.0, mass: m}
    }
}

struct dPendel {
    p1: Pendel,
    p2: Pendel,
}

impl dPendel {
    fn new(l1: f64, a1: f64, l2: f64, a2: f64, m1: f64, m2: f64) -> dPendel {
        return dPendel {
            p1: Pendel::new(l1, a1, m1),
            p2: Pendel::new(l2, a2, m2),
        }
    }
    
    fn calc_acc(&mut self){
        let p1_acc: f64 = self.p1.acc;
        let p2_acc: f64 = self.p2.acc;
        
        self.p1.acc = - (self.p2.mass) / (self.p1.mass + self.p2.mass) 
                        * (self.p2.length / self.p1.length)
                        * (p2_acc * (self.p1.angle - self.p2.angle).cos()
                            + (self.p2.vel * self.p2.vel * (self.p1.angle - self.p2.angle).sin()))
                        - (g / self.p1.length) * self.p1.angle.sin();
        
        self.p2.acc = - (self.p1.length / self.p2.length)
                        * ((p1_acc * (self.p1.angle - self.p2.angle).cos())
                            - (self.p1.vel * self.p1.vel) * (self.p1.angle - self.p2.angle).sin())
                        - (g / self.p2.length * self.p2.angle.sin());
                        
                        
    }
    
    fn step(&mut self) {
        self.calc_acc();
        
        self.p1.angle += self.p1.vel * dt;
        self.p2.angle += self.p2.vel * dt;
        
        self.p1.vel += self.p1.acc * dt;
        self.p2.vel += self.p2.acc * dt;
    }
    
    fn printSystem(&self) {
        println!("angle 1: {} angle 2: {}", self.p1.angle, self.p2.angle);
    }
    
    fn convto2d_p1(&self) -> cord {
        return cord {x: self.p1.angle.sin() * self.p1.length, y: self.p1.angle.cos() * self.p1.length} 
    }
    
    fn convtod2_p2(&self) -> cord {
        let cord_p1: cord = self.convto2d_p1();
        
        let mut cord_p2: cord = cord {x: self.p2.angle.sin() * self.p2.length, y: self.p2.angle.cos() * self.p2.length};
        
        cord_p2.x += cord_p1.x;
        cord_p2.y += cord_p1.y;
        
        return cord_p2;
    }
}

const g: f64 = 9.8;
const dt: f64 = 0.01;

fn main() {
    let p_len: f64 = 1.0;
    let p_mass: f64 = 1.0;
    
    
    let mut pendel: dPendel = dPendel::new(p_len, 0.1, p_len, 0.1, p_mass, p_mass);
    
    for i in 0..1000 {
        pendel.step();
        pendel.printSystem();
    }
}
