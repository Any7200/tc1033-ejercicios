#A01366974
def greet(_name):
    print("Hello",_name)
def run(_number):
    if _number >= 0 and _number <= 10:
        value = 0
        while value!=_number:
            print("Running")
            value+=1
print("Nombre?")
name = str(input())
obj1 = greet(name)
obj1
print("Número?")
number = int(input())
obj2 = run(number)
obj2
