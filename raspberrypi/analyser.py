
# Analyser Calss, it analyses the receaved data, most of the code is not used

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
        try:
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
            return new_values
        except:
            return False


