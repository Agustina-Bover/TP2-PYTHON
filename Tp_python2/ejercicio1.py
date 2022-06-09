########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
########
"""
Escribir una función que retorne True cuando un número entero es par y
False cuando no lo sea, sin utilizar módulo. (%)
"""
def es_par(numero):
    """
    La funcion comprueba si el numero es par. Tanto si es positivo
    como negativo
    """
    if numero>0:
        while numero>0:
            numero-=2
        if numero==0:
            return True
        return False
    else:
        while numero<0:
            numero+=2
        if numero==0:
            return True
        return False

def principal():
    """
    Esta funcion es la parte interactiva del ejercicio
    """
    numero=int(input("Ingrese un numero--> "))
    resultado=es_par(numero)
    print(f"¿{numero} es par? {resultado}")
if __name__ =='__main__':
    principal ()