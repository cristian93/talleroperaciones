def ingreso():
    global a,b
    a=float(input("ingresar primer numero"))
    b= float(input("ingresar segundo numero"))

def suma():
        print( "resultado=", a+b)
        input()


def resta():
    print("resultado=", a - b)
    input()

def mult():
    print("resultado=", a * b)
    input()

def div():
    if(b==0):
        print("no hay division entre 0")
        input()
    else:
        print("resultado=", a / b)
        input()

def mns():
    print("ha digitado una opcion incorrecta")

while(True):
    print ("1 suma")
    print ("2 resta")
    print ("3 multiplicacion")
    print ("4 division")

    opcion=int(input("ingresar opcion\n"))
    if(opcion==1):
        ingreso()
        suma()

    if(opcion==2):
        ingreso()
        resta()

    if(opcion==3):
        ingreso()
        mult()

    if(opcion==4):
        ingreso()
        div()

    if(opcion>=5):
         mns()







