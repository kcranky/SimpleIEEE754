import parameterDefinitions
import packUnpack
import math

# Globals
expSource = []
pyAdd = []
pyMul = []

def create_python_arrays():
   global expSource, pyAdd, pyMul
   # Generate the exponentials
   expSource = range(-12000, 12000, 50)
   expSource = [float(i)/100 for i in expSource]
   expSource = [math.exp(i) for i in expSource]
   
   # Get the python calculated values
   pyAdd = [x+x for x in expSource]
   pyMul = [x*x for x in expSource]


# Write output to csv
def create_file(name):
   global expSource, pyAdd, pyMul
   f = open(name+".csv", "w")
   f.write("start values, python addition, python multiplication\n")
   for i in range(len(expSource)):
      f.write(("{},{},{}\n").format(expSource[i], pyAdd[i], pyMul[i]))
   f.close()
   
   
if __name__ == "__main__":
   create_python_arrays()
   create_file("output")
   print("Task complete")