import os

class start:
    def __init__(self,dri_path):
        self.d_path=dri_path

    def start(self):
        cmd=r"START /MIN"+" "+self.d_path
        os.system(cmd)

    def stop(self):
        cmd=r"TASKKILL /IM Winnium.exe"
        os.system(cmd)
