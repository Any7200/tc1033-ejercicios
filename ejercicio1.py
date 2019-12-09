#A01366974
def greet(_name):
    print("Hello",_name)
def run(_number):
    if _number >= 0 and _number <= 10:
        value = 0
        while value!=_number:
            print("Running")
            value+=1
def perceptron(a,b,c,d):
    x = (a*b)+(c*d)
    if x>20:
        print("1")
        return 1
    else:
        print("0")
        return 0 
#Inicio de programa 
if __name__ == "__main__":
    obj1 = greet("Hansel")
    obj1 = greet("Gretel")
    obj2 = run(5)

