#A01366974
def greet(_name):
    print("Hello",_name)
def run(_number):
    if _number >= 0 and _number <= 10:
        value = 0
        while value!=_number:
            print("Running")
            value+=1
#Inicio de programa 
if __name__ == "__main__":
    obj1 = greet("Hansel")
    obj1 = greet("Gretel")
    obj2 = run(5)
