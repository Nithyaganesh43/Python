class dpet():
    clg="SECE"
    def __init__(self,dpart,year):
        self.dpart=dpart
        self.year=year
class classes(dpet):
    def __init__(self,cls,adwiser,dpart,year):
        self.cls=cls
        self.adwiser=adwiser
        dpet.__init__(self,dpart,year)
class student(classes):
    def __init__(self,name,roll,cls,adwiser,dpart,year):
        self.name=name
        self.roll=roll
        classes.__init__(self,cls,adwiser,dpart,year)
    def showstd(self):
        print(f"student name:{self.name}\nroll:{self.roll}\nclass:{self.cls}\nclass adwiser:{self.adwiser}\ndepartmant:{self.dpart}\nyear:{self.year}")
std1=student("poojana","23cs113","cseb","akila T","Computer Science","1")
std1.showstd()
