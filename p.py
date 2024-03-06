total =0
escalas = int(input("Cuantas escalas desea realizar  <"))

for i in  range (escalas):
    dsitancia= int(input("Distancia "))

    total += dsitancia


print("La distancia total es:", total)
print("Se han ingresado "+ str(escalas) +" etapas.")