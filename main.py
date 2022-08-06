# 4 basic data typse

First_name = "Ronnie"
Last_name = "Tabiano"
Full_name = First_name +" "+ Last_name
print("Hello "+Full_name)
print(type(First_name))
# String Store a series of character

age = 19
age += 1
print("Your age is: "+ str(age))
print(type(age))
# int store a hole integer

height = 180.5
print ("your height is: "+str(height) +"cm")
print  (type(height))
# float floating point number, mumeric value with a decimal

human = True
print("Are you a human: "+str(human))
print(type(human))
# bolean store true or false

# Type Casting = Convert the data types of a value to another data types.
x = "1"   #string
y = 2.0   #float
z = 3     #int

x = int(x)
y = str(y)
z = float(z)

print (x*5)
print ("this is now string not float "+y)
print (z*5)
