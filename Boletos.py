#Víctor Iván Morales Ramos A01377601
#Descripción: Escribir un codigo que calcule el precio de la cantidad de boletos recibidos de respectiva zona.

#Funcion que calcula el precio de la cantidad de boletos
def calcularPago(ba, bb, bc):
    pba = ba * 3250.00
    pbb = bb * 1730.00
    pbc = bc * 850.00
    pt = pba + pbb + pbc
    return pt

#Llamada de la función
def main():
    ba = int(input("Número de boletos en zona A: "))
    bb = int(input("Número de boletos en zona B: "))
    bc = int(input("Número de boletos en zona C: "))
    pt = calcularPago(ba, bb, bc)
    print("El precio total es: $%2.f" %(pt))

main()
