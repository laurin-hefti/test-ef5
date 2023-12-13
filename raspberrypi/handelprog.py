import time
from threading import Thread

# --------------------------- Handelprog Class -------------------------

# this class handels all subprogramms. It uses multithreading for
# executing different subfunctions.

# you can add a function to the programm. The prgramm will periodicly
# execute the subprogramm.
# Input: handelprog.add_func(name_of_func, own_condition_function, name_for_function, (optional) parameters")
# parameters: MAXITERX, X maximal number of executing, ITERX, X after X iterations it will be executed

#/----------------------------------------------------------------------/
# Attention, the maxIter keyword must be the last properite to specify
# because, the programm checks if all properties are okey, but in the
# check fuction increments the runnummber.
# So if its not the last properties how cheks if the action should be
# executet, it will think it will be oke to increment and a later
# property neglet negate this.
#/----------------------------------------------------------------------/

class HandelProg :

    key_words = ["ITER","MAXITER"]
    
    def run_anyway():
        return True
        
    def if_run(x,i):
        if x%i[0] == 0:
            return True
        return False
            
    def max_run(x,i):
        if i[0] > i[1]:
            print("inc")
            i[1] += 1
            return True
        return False
    
    def reset_number_run(obj,name):
        i = obj.get_index_case(name)
        obj.prop[i][-1][1][1] = 0
    
    def inc_number_run(self,name):
        i = self.get_index_case(name)
        self.prop[i][-1][1][1] += 1
            
    util_f = [if_run, max_run]
    
    def __init__(self,name):
        self.name = name
        self.func = [] #executing function, contains function to exevute
        self.case = [] #case when should executetd, includes a function
        self.enum = [] #enum indentifier for case, includes a string
        self.prop = [] #properties for internal handling, indcludes string for specifying own properties
        self.run = True
        self.runtime = 1
    
    def start(self):
        print("programm is starting up")
        self.run = True
        
        self.main_loop()
        
    def execute(self,i):
        t = Thread(target=self.func[i], args=())
        t.start()
        
    def add_func(self,func, case, name, properties = []):
        self.func.append(func)
        self.case.append(case)
        self.enum.append(name)
        self.set_properties(properties)
        
    def set_properties(self,prop):
        self.prop.append([])
        for i in prop:
            first_n = 0 #first number in prop keyword, is a paramater to te keyword
            ii = 0
            for j in i:
                if j.isnumeric():
                    first_n = ii
                    break
                ii += 1
            word = i[:first_n]  #contains the keyword without parameters
            self.prop[-1].append([word,[int(i[first_n:]),0]])
            
    def use_word(self,data):
        for i in data:
            j = HandelProg.key_words.index(i[0])
            if not HandelProg.util_f[j](self.runtime,i[1]):
                return False
        return True
        
    def execute_prop(self,i):
        data = self.prop[i]
        if self.case[i]() == True:
            if self.use_word(data) == True:
                self.execute(i)
            
    def use_properties(self): #cheks if properties are specified
        ii = 0
        for i in self.prop:
            if i != [] or True:
                self.execute_prop(ii)
            ii += 1
        
    def get_index_case(self,name):
        try:
            return self.enum.index(name)
        except:
            print("error name ist not in list")
        
    def triger_func(self, name):
        index = self.get_index_case(name)
        if self.case[index]() == True:
            self.execute(index)
    
    def main_loop(self):
        while self.run:
            self.use_properties()
            
            print(self.runtime)
            self.runtime += 1
            time.sleep(10)
