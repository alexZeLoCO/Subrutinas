#Se le denomina RECURSIVIDAD a llamar a la función dentro de sí misma.
#Programaremos una función para calcular el factorial de un número usando la recursividad.

def Factorial (número):

    if (número==1):     #Si el número es 0, no hay más factorial que calcular y se devuelve la suma.
        return número
    else:       #Si el número no es 0, hay que seguir multiplicando.
        return (número* Factorial (número-1))     #Entonces a la suma habría que multiplicarle el factorial del número anterior.
             #Para calcular el factorial del número anterior, llamamos de nuevo a la función Factorial(número) y le pasamos
             #como parámetro el número original menos 1. El bucle se sigue repitiendo hasta que éste número sea 0.
             #Al ser 0, se cumple la condición if(número==0): y se empiezan a devolver los valores suma entre ellos
             #hasta llegar al primero.

print(Factorial(4))

#En este ejemplo, creamos la función Factorial (número), le pasaremos el número cuyo factorial vamos a calcular como
#parámetro.
#
#No sólo podemos llamar a una subrutina dentro de una subrutina. Sino que podemos llamar -como ya hemos visto- condicionales
#como if y else (o elif) y bucles. Pero más importante aún, es que podemos llamar a otras Subrutinas.
#
#Programaremos dos subrutinas y llamaremos a una dentro de la otra.

def areaBase (radio):
    PI = 3.141592654        #Inicializa PI
    return radio**2*PI      #Calcula area de base y la devuelve

def volumen (AreaBase, Altura):
    return AreaBase*Altura      #Calcula volumen de figura y lo devuelve

print(volumen(areaBase(10),2))      #Llamada a ambas subrutinas.
                     #Radio
               #AreaBase,Altura
        #Volumen
        
#Podemos entender que las subrutinas son 'churreras' que reciben unos datos, los procesan y sacan otros. Este tipo de
#programas, con varias 'churreras' anidadas se pueden ver como 'churreras industriales', que están conectadas unas tras las
#otras y modifican datos mucho más que una sola.
#
#En este mismo ejemplo, podemos ver:
#
#   CHURRERA 1:         RADIO ---> AREA BASE
#   CHURRERA 2:     AREA BASE ---> VOLUMEN
#
#   CHURRERA INDUSTRIAL (1+2):      RADIO ---> AREA BASE ---> VOLUMEN
#                                      CHURRERA 1     CHURRERA 2
#
#En este ejemplo hemos creado 2 subrutinas, una llamada 'areaBase (radio)' y otra 'volumen (AreaBase, Altura)'.
#La primera de ellas recibe como parámetro el radio de una circunferencia. Devuelve el area de la base.
#La segunda de ellas recibe el area de una base y la altura. Devuelve el volumen de la figura.
#Hemos utilizado las dos conjuntamente para calcular el volumen de un cilindro.