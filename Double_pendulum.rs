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
    
    impl step(&mut self) {
        
    }
}

const g: f64 = 9.8;
const dt: f64 = 0e-5;

fn main() {
    
}
