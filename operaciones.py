def suma(sumando1, sumando2):
    sumando1 = float(sumando1)
    sumando2 = float(sumando2)
    suma = sumando1+sumando2
    return suma
sumando1=input('Primer sumando: ')
sumando2=input('Segundo sumando: ')
print(f"{sumando1}+{sumando2}={suma(sumando1,sumando2)}\n¿Es correcto?")