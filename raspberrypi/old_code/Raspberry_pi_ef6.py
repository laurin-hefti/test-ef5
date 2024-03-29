import time
from threading import Thread
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, datetime
import grovepi

#grovepi.set_ubs("RPI_1")

def set_button(port):
    grovepi.pinMode(port, "INTPUT")

def check_button_port():
    port = 0
    return grovepi.digitalRead(port)

def get_data_from_api():
    url = "https://api.polygon.io/v2/aggs/ticker/SMI/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&limit=120&apiKey=HNRmV2qK0iESHmTb_ikYsresXkZAS1ph"
    r = requests.get(url)
    data = r.json()
    #print(data)
    return data

#print(get_data_from_api())
    
class HandelFile :
    
    def __init__(self, name):
        self.name = name + ".txt"
        self.n_registers = 0;
        
    def write_file(self,context):
        f = open(self.name, "w+")
        old_context = f.read()
        new_context = old_context + "\n" + context
        f.write(new_context)
        self.n_registers += 1
        f.close()
        
    def get_context(self):
        f = open(self.name, "r")
        context = f.read()
        f.close()
        return context
        
    def get_context_line(self,n):
        if n < 0:
            n = self.n_registers + n
        f = open(self.name, "r")
        context = f.read(n)
        f.close()
        return context
    
class Send_email :

    def __init__(self):
        self.my_addres = "stockanalyser@web.de"
        self.passwort = "testemailstockapi"

        self.name = "laurin.heft"
        self.email = "laurin.hefti@icloud.com"
        #self.email = "lars.hoesli2@stud.schulegl.ch"
        self.messageTemplate = ""

        self.host = "smtp.web.de"
        self.port = 587

    def server_conection(self):
        s = smtplib.SMTP(self.host, self.port)
        s.starttls()
        s.login(self.my_addres,self.passwort)
        return s

    def create_email(self, msg):
        email = MIMEMultipart()

        email["From"] = self.my_addres
        email["To"] = self.email
        email["Subject"] = "Daily report"

        email.attach(MIMEText(msg,"plain"))

        return email
    
    def send_email(self, msg, form):
        s = self.server_conection()
        msg = self.use_form(form)(msg)
        email = self.create_email(msg)

        s.send_message(email)
        s.quit()

    def form_data(self,data):
        out_str = ""
        out_order = ["Open:     ", 
                     "Close:    ", 
                     "higth:    ",
                     "low:      ",
                     "dif:      ",
                     "p:        "]
        out_str += "End day report\n"
        day = date.today()
        out_str += "at: " + str(day) + "\n"

        for i in range(len(data)):
            out_str += out_order[i] + str(data[i]) + "\n"
        
        out_str += "end"
        
        return out_str
    
    def use_form(self, name):
        forms = [self.form_data]
        forms_name = ["end_day"]

        i = 0

        if name in forms_name:
            i = forms_name.index(name)
        else:
            print("error form not in list")

        return forms[i]



class Analyser :
    
    def __init__(self, data):
        self.data = data
        self.comp = []
        self.usfull_data = []

        
    def get_components(self):
        for i in self.data:
            self.comp.append(i)
            
    def store_data(self, manager, data):
        manager.write_file(data) 
            
            
    #not modular
    
    def end_day_routine(self):
        new_values = []
        open = int(self.data["results"][0]["o"])
        close = (self.data["results"][0]["c"])
        higth = (self.data["results"][0]["h"])
        low = (self.data["results"][0]["l"])
        dif = close - open
        p = dif / close

        new_values.append(open)
        new_values.append(close)
        new_values.append(higth)
        new_values.append(low)
        new_values.append(dif)
        new_values.append(p)
        #print(self.data["results"][0]["v"])
        return new_values

def end_day_routine():
    analyse = Analyser(get_data_from_api())
    email = Send_email()
    data = analyse.end_day_routine()
    email.send_email(data, "end_day")
    print("finsish")

#end_day_routine();


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
            i[1] += 1
            return True
        return False
    
    def reset_number_run(obj,name):
        i = obj.get_index_case(name)
        obj.prop[i][-1][1][1] = 0
            
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
            #value = int(i[len(i)-1])
            #self.prop[-1].append([word,[int(k) for k in i[first_n:]]])
            self.prop[-1].append([word,[int(i[first_n:]),0]])
            #self.prop[-1].append([int(k) for k in i[first_n:]])
        #print(self.prop)
            
    def use_word(self,data):
        for i in data:
            j = HandelProg.key_words.index(i[0])
            if not HandelProg.util_f[j](self.runtime,i[1]):
                return False
        return True
        
    def execute_prop(self,i):
        data = self.prop[i]
        if self.use_word(data):
            if self.case[i]() == True:
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
        
    #def check_case(self,name)
    
    def main_loop(self):
        while self.run:
            self.use_properties()
            
            print(self.runtime)
            self.runtime += 1
            time.sleep(10)
                    

def get_time():
    time = datetime.now()
    return time

def call_interval(t,t2):
    time = str(get_time().time())
    time = time[0:2]
    if int(time) >= t and int(time) < t2:
        return True
    else:
        return False

def call_20():
    return call_interval(20,21)

def call_23():
    return call_interval(23,24)

def call_15():
    return call_interval(15,16)

prog = HandelProg("test2")

def test_f():
    HandelProg.reset_number_run(prog,"TEST")

def reset_day_fuc():
    HandelProg.reset_number_run(prog,"END_DAY")

prog.add_func(end_day_routine,call_15, "END_DAY",["MAXITER1"])
prog.add_func(end_day_routine, check_button_port,"BUTTON_PRESS")
prog.add_func(reset_day_fuc,call_23,"RESET_END_DAY")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST",["MAXITER300"])
prog.main_loop()
#prog.add_func(get_data_from_api,HandelProg.run_anyway,"TEST_API")
#prog.triger_func("TEST_API")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST_F",["ITER2","MAXITER30"])
#prog.main_loop()     
