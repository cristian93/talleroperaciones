
def suma():
        print( "resultado de la suma es=", a+b)
        input()


def resta():
    print("resultado de la resta es=", a - b)
    input()

def mult():
    print("resultado de la multiplicacion es =", a * b)
    input()

def div():
    if(b==0):
        print("no hay division entre 0")
        input()
    else:
        print("resultado de la division es=", a / b)
        input()

def mns():
    print("ha digitado una opcion incorrecta")

while(True):
    a = float(input("ingresar primer numero: "))
    b = float(input("ingresar segundo numero: "))

    print ("1 suma")
    print ("2 resta")
    print ("3 multiplicacion")
    print ("4 division")

    opcion=int(input("ingresar opcion\n"))
    if(opcion==1):

        suma()

    if(opcion==2):

        resta()

    if(opcion==3):

        mult()

    if(opcion==4):

        div()

    if(opcion>=5):
         mns()










