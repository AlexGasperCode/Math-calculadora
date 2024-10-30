import math

print("Calculadora científica")
print("1. Exponenciación")
print("2. Raíz cuadrada")
print("3. Logaritmo")
print("4. Función trigonométrica")
print("5. Salir")

while True:
    select = int(input("Eliga la opción: "))

    if select == 5:
        print("Salir...")
        break


    elif select == 1:
        base = float(input("Ingrese el número: "))
        exponent = float(input("Ingrese exponente: "))
        result = math.pow(base, exponent)
        print("El resultado es:", result)

    elif select == 2:
        num = float(input("Ingrese en número: "))
        result = math.sqrt(num)
        print("El resultado es:", result)

    elif select == 3:
        num = float(input("Ingrese en número: "))
        base = float(input("Ingrese la base: "))
        result = math.log(num, base)
        print("El resultado es:", result)

    elif select == 4:
        angle = float(input("Introduzca el ángulo en grados: "))
        result_sin = math.sin(math.radians(angle))
        result_cos = math.cos(math.radians(angle))
        result_tan = math.tan(math.radians(angle))
        print("Seno:", result_sin)
        print("Coseno:", result_cos)
        print("Tangente:", result_tan)

    else:
        print("Selección incorrecta. Por favor eliga del 1 al 5.")