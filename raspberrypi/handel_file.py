
# Handelfile calss, can handel files easily but it not used

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
    