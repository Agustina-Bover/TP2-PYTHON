########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
########
"""
Implementar una función que obtenga los máximos, mínimos y promedio
de una secuencia con números, retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del
lenguaje que procesan secuencias.
"""

def obtener_estadistica(numero):
    minimo=99999
    maximo=0
    promedio=0
    if numero>maximo:
        maximo=numero
    elif numero<minimo:
        minimo=numero
    promedio+=numero
    promedio=promedio/10
    tupla=(maximo,minimo,promedio)
    return (tupla)

def principal():
    numero=int(input("Ingrese un numero-->"))
    try:
        assert isinstance(numero,int)
        
        
        
    except:
        resultado=obtener_estadistica(numero)
        print (resultado)
        
if __name__ =='__main__':
    principal ()        