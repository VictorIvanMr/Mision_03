#Autor: Víctor Iván Morales Ramos A01377601
#Descripción: Calcular el rendimiento de kilometros y millas de un carro.

#Funcion que calcula el rendimiento en litro

def calcularRendimientoKm(km, l):
    rkm = km / l
    return rkm

#Funcion que calcula el rendimiento en galones

def calcularRendimientoMi(km, l):
    rmi = (km / 1.6093) / (l * 0.264)
    return rmi

#Esta funcion calcula los km que recorrera el auto
def calcularKmarecorrer(km, litros, kmarecorrer):
    l = kmarecorrer * 0.0358
    return l

#Funcion principal que resuelve el problema
def main():
    km = int(input("Dame el número de Km recorridos: "))
    l = int(input("Dame el número de litros de gasolina usados: "))
    rkm = calcularRendimientoKm(km, l)
    rmi = calcularRendimientoMi(km, l)
    print(""" \x1b[1;30m 
Si recorres""",(km),"""kms. con""", (l), """litros de gasolina, el rendimiento es:
%.2f""" %(rkm), """km/l
%.2f""" %(rmi), """mi/gal
""")
    kmarecorrer = int(input("\x1b[0;m¿Cuántos kilómetros vas a recorrer? "))
    l = calcularKmarecorrer(km, l, kmarecorrer)
    print(""" \x1b[1;30m 
Para recorrer""", (kmarecorrer),"""km. necesitas %.2f""" % (l), """litros de gasolina""")

main()
