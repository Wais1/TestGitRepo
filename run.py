#1.
def convertToRadians(degrees):
    return(degrees * (3.14/180))
degrees = 150
radians = convertToRadians(150)
print("Degrees:" + str(degrees))
print("Radians: " + str(radians))

#2.
student1, student2, student3 = 80.0, 90.0, 66.5
average = sum((student1,student2,student3))/3
print("Student scores:\n" + str(student1), str(student2), str(student3))
print("Average: " + str(average))

#3.

def calcGroup(numStudents,numGroups):
    return(numStudents//numGroups)

def calcRemainder(numStudents,numGroups):
    return(numStudents%numGroups)

print("Number of students in each group")
print("Class1: " + str(calcGroup(32,5)))
print("Class2: " + str(calcGroup(45,7)))
print("Class3: " + str(calcGroup(51,6)))

print("Number of students leftover:")
print("Class1: " + str(calcRemainder(32,5)))
print("Class2: " + str(calcRemainder(45,7)))
print("Class3: " + str(calcRemainder(51,6)))

#4.

pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter/2
circumference = 2 * pi * pie_radius
circumference_msg = "Jimmy's pie has a circumference"
print(circumference_msg, circumference)

#5.

velocity = 343
frequency = 256

def calcWavelength(v, f):
    return(v/f)

print("The speed (m/s): ", velocity)
print("The frequency (Hz): ", frequency)
print("The wavelenth (m): ", calcWavelength(velocity,frequency))
