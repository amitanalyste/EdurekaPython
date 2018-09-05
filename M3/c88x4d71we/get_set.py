class Edureka:
    def __init__(self,courseName):
        self.courseName=courseName

    def setCourse_Name(self,courseName):
        self.courseName=courseName

    def getCourse_Name(self):
        return(self.courseName)

ob=Edureka("Python")

print(ob.getCourse_Name())

ob.setCourse_Name("Machine Learning")
print(ob.getCourse_Name())