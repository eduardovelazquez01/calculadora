#Calculadora en Python para Evaluacion 2, Universidad UK.

nombre = input("Ingresa tu nombre: ")

print(f"¡Bienvenido a 'KuepiPlus+' {nombre}!, tu calculadora personal :)")


#Agregamos funciones por cada operación
def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    if b != 0:
        return a / b
    else:
        return "¡Error!, no se puede dividir entre cero."

def residuo (a, b):
    if b != 0:
        return a % b
    else:
        return "¡Error! No se puede sacar residuo a un numero por cero"

def potencia(a, b):
    return a ** b

#Bucle de ejecucion infinita, hasta que usuario salga

while True:
    print(""" 
(1) - Suma +
(2) - Resta -
(3) - Multiplicación *
(4) - División /
(5) - Residuo %
(6) - Potencia **
(7) - Salir :( """)
    opcion = input("Elige la operación que desees realizar: ")
    #Condicional para salir
    if opcion == '7':
        print(f"¡Nos vemos luego {nombre}! :)")
        break
    #Condicional para evitar numero fuera de rango
    if opcion not in ('1','2','3','4','5','6'):
        print(f"¡Hola {nombre} :) esa opción NO es valida!, Por favor elige un numero del 1 al 7")
        continue
    try:
    #Entrada de datos
        numero_1 = float(input("Ingresa el primer numero: "))
        numero_2 = float(input("Ingresa el segundo numero: "))
    except ValueError:
        print(f"Error :(, debes ingresar números válidos. Intentálo nuevamente {nombre}.")
        continue
    #Operaciones
    if opcion == '1':
        print("El resultado de ésta Suma es: ", suma(numero_1, numero_2))
    elif opcion == '2':
        print("El resultado de ésta Resta es: ", resta(numero_1, numero_2))
    elif opcion == '3':
        print("El resultado de ésta Multiplicación es: ", multiplicacion(numero_1, numero_2))
    elif opcion == '4':
        print("El resultado de ésta División es: ", division(numero_1, numero_2))
    elif opcion == '5':
        print("El Residuo de esta división es:", residuo(numero_1, numero_2))
    elif opcion == '6':
        print("El resultado de la potencia es: ", potencia(numero_1, numero_2))







