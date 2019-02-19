#Víctor Iván Morales Ramos A01377601
#Descripción: Calcular el perimetro y el area de un trapecio

#Funcion que calcula el area
def calcularArea(bmayor, bmenor, h):
    a = ((bmayor + bmenor)/2)*h
    return a

#Función que calcula el perimetro
def calcularPerimetro(bmayor, bmenor, h):
    bl = (bmayor - bmenor)/2
    l = (bl **2 + h**2) ** 0.5
    p = bmayor + bmenor + (2 * l)
    return p

#Llamada de la función
def main():
    bmayor = int(input("Dame el tamaño de la base mayor: "))
    bmenor = int(input("Dame el tamaño de la base menor: "))
    h = int(input("Dame la altura: "))
    a = calcularArea(bmayor, bmenor, h)
    p = calcularPerimetro(bmayor, bmenor, h)
    print("Área: %.2f" %(a))
    print("Perímetro: %.2f" %(p))

main()
