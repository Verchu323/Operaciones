num_uno = 0
num_dos = 0
num_tres = 0
num_cuatro = 0
num_cinco = 0
while True:
    operacion = int(input("""Elige el numero de las siguientes operaciones
    Suma = 1
    Resta = 2
    Multiplicacion = 3
    Division = 4
    : """))
    if operacion == 1:
        num_uno = int(input("Haz seleccionado la suma. Dame el primer valor: "))
        num_dos = int(input("Haz seleccionado la suma. Dame el segundo valor: "))
        print(f"Este es el resultado de sumar lo siguientes valores {num_uno} + {num_dos} = {num_uno + num_dos}")
        text = input("Si quieres realizar una nueva operacion, escibe 'Si'. En caso contrario escribe 'No': ")
        if text == "Si":
            continue
        else:
            break
    if operacion == 2:
        num_uno = int(input("Haz seleccionado la resta. Dame el primer valor: "))
        num_dos = int(input("Haz seleccionado la resta. Dame el segundo valor: "))
        print(f"Este es el resultado de restar los siguientes valores: {num_uno} + {num_dos} = {num_uno - num_dos}")
        text = input("Si quieres realizar una nueva operacion, escibe 'Si'. En caso contrario escribe 'No': ")
        if text == "Si":
            continue
        else:
            break
    if operacion == 3:
        num_uno = int(input("Haz seleccionado la multiplicacion. Dame el primer valor: "))
        num_dos = int(input("Haz seleccionado la multiplicacion. Dame el segundo valor: "))
        print(f"Este es el resultado de multiplicar los siguientes valores: {num_uno} + {num_dos} = {num_uno * num_dos}")
        text = input("Si quieres realizar una nueva operacion, escibe 'Si'. En caso contrario escribe 'No': ")
        if text == "Si":
            continue
        else:
            break
    if operacion == 4:
        num_uno = int(input("Haz seleccionado la division. Dame el primer valor: "))
        num_dos = int(input("Haz seleccionado la division. Dame el segundo valor: "))
        print(f"Este es el resultado de dividir los siguientes valores {num_uno} + {num_dos} = {num_uno / num_dos}")
        text = input("Si quieres realizar una nueva operacion, escibe 'Si'. En caso contrario escribe 'No': ")
        if text == "Si":
            continue
        else:
            break
print("Fin del programa")