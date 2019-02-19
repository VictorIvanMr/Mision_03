#Víctor Iván Morales Ramos A01377601
#Descripción:

#Función que calcula el pago normal
def calcularPagoNormal(hn, he, ph):
    pn = hn * ph
    return pn

#Función que calcula el pago de horas extra
def calcularPagoExtra(hn, he, ph):
    pe = (he * ph) + ((ph * .65)* he)
    return pe

#Llamada de la función
def main():
    hn= int(input("TDame las horas normales trabajadas: "))
    he = int(input("Dame las horas extras trabajadas: "))
    ph = int(input("Dame el pago por hora: "))
    pn = calcularPagoNormal(hn, he, ph)
    pe = calcularPagoExtra(hn, he, ph)
    pt = pn + pe
    print("Pago normal: \x1b [1;30m $%.2f" %(pn))
    print("\x1b [0;m Pago extra: \x1b [1;30m $%.2f" %(pe))
    print("---------------------------------------------")
    print("\x1b [0;m Pago total: \x1b [1;30m $%.2f" %(pt))

main()
