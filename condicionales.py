# Declaramos una variable
from gc import callbacks


calificacion = input ("Introduce tu calificacion del AZ-900: ")

calificacion = int(calificacion)

# Prerguntamos si la calificacion es menor a 700
if calificacion < 700 : 
    print("Veees por no estudiar") # Si es menor a 700, muestra esto
elif calificacion > 1000:
    print("MIENTEESS, no puedes sacar mas de mil")
else : # Si no se cumple el if anterior, pasa a esta linea
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad 
edad = input("Introduce tu edad ")
edad = int(edad)

if edad >=18 and edad <=100 :
    print("Bienvenid@ al nombrePNG")
elif edad > 100 :
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

# En python no hay Switch case 
