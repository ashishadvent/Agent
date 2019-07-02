
class configuration:
   
    def __init__(self,path):
        self.path=path
        
    def get_values(self):
        d={}
        with open(self.path) as f:
            lines = f.read().splitlines() 
            for j in lines:
                a=j.split("=")
                if len(a) >= 2:
                    d[a[0]] = a[1]
        return d
