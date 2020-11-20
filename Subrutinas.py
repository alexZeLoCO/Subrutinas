# Definimos una función como una parte del código escrita separada del resto. Podemos utilizar funciones para organizar
# mejor un programa, aprovechar variables, ayudarnos a resolver problemas etc...
#
# Para definir una función, utilizaremos la palabra def <nombre de función> (<parámetros>):
# el nombre de la función puede ser cualquiera que nos parezca prudente, y los parámetros son opcionales, deben ir entre
# paréntesis. Téngase en cuenta que una función siempre lleva paréntesis al final, haya o no parámetros.
# Para comenzar a escribir el código que se ejecutará en la función, añadiremos dos puntos (:) al final de su definición
# e indentado, en la línea siguiente escribiremos más código.
#
# Podríamos decir que una función es como los asteriscos de un texto, cuando ves uno *. Por lo que no sólo hay que saber
# para qué sirve el asterisco, sino que también hay que saber leer (dígase, utilizar el resto de funciones como bucles etc).
# *Lees donde haya otro.
#
# Programaremos una función:

def Napoleón ():
    print (2)

#Hemos definido una función llamada Napoleón, no recibe ningún parámetro. Cuando la llamemos, imprimirá un 2 por pantalla.
#Para llamar a una función que hayamos definido previamente, escribimos su nombre y parámetros (en este caso, ninguno).

Napoleón()

#Esta función sólamente imprime un valor. No sirve para nada más. Podemos operar con funciones si utilizamos la palabra RETURN
#RETURN sirve para lo que se llama devolver un valor al final de una función -por lo general, se usan en funciones que operen
#y aquello que devuelven es el resultado de la operación-.
#
#Devolver un valor no es lo mismo que imprimirlo, al imprimirlo, se muestra por pantalla, al devolverlo, no se muestra.
#Podemos sin embargo, imprimir una función que devuelva un valor. Esto imprimiría el valor devuelto por estar dentro de un print().
#
#Una función que devuelve algo (con un return) se llama comunmente FUNCIÓN, aquellas que no devuelven nada (como Napoleón())
#se llaman PROCEDIMIENTO. A ambas se les puede llamar SUBRUTINA. -O, mejor dicho, las FUNCIONES y PROCEDIMIENTOS son los
#dos tipos de SUBRUTINAS-.
#
#Programaremos una SUBRUTINA / FUNCIÓN (con RETURN):

def Curie ():
    x=2+4
    return x

#Hemos definido otra subrutina llamada Curie, no recibe ningún parámetro. Cuando la llamemos, calculará la suma de 2+4,
#almacenará su valor en x y al final lo devolverá (no imprimirá).

Curie()     #No imprime nada

print(Curie())      #Imprime un 6 (x) por estar dentro de un print, NO POR DEVOLVER EL VALOR X.

#Un valor se pasa como parámetro cuando éste se ha creado fuera de la subrutina y se quiere utilizar dentro de una.
#Es un tema que se puede complicar porque es fácil perder el rastro de las variables que hemos creado dentro y fuera.
#Para resumir tenemos la frase estrella:
#
#           "LAS VARIABLES DE UNA SUBRUTINA EXISTEN SÓLO DENTRO DE LA MISMA."
#
#Dígase, si creamos una variable fuera de una subrutina y la intentamos utilizar dentro de una, saldrá un error diciendo
#que dicha variable no ha sido inicializada. No porque no exista en el programa, sino porque no existe dentro de la subrutina.
#
#Los nombre de los parámetros no tienen por qué ser iguales dentro y fuera de la subrutina, puedo tener un valor llamado Alumnos
#fuera de la subrutina y definirlo en la definición de función como Vector.
#
#Programaremos una SUBRUTINA / FUNCIÓN (con RETURN) y pasándole un PARÁMETRO (<este>):

def Aristóteles (lado):
    area=lado**2
    return area

#Hemos definido una subrutina llamada Aristóteles, recibe un parámetro al que se llamará lado. Cuando la llamemos,
#calculará el área el cuadrado de lado pasado como parámetro. Y devolvera el resultado.

lateral = 2
print(Aristóteles(lateral))

#En este ejemplo, inicializamos la variable 'lateral' y le damos el valor 2. Después llamamos a la subrutina Aristóteles
#y le pasamos como parámetro 'lateral'. Aunque en la definición de la línea 62 el parámetro se llame lado, no significa
#que la variable que le vayamos a pasar se tenga que llamar lado fuera de la subrutina.
#
#Gracias a esto, podemos aprovechar la misma subrutina para 2 cálculos distintos:

lateral1 = 2
lateral2 = 3
print(Aristóteles(lateral1))
print(Aristóteles(lateral2))

#En este otro ejemplo, inicializamos 2 variables 'lateral1' y 'lateral2' y les damos 2 valores diferentes.
#Podemos llamar 2 veces a la función Aristóteles(lado): y pasarle una vez el 'lateral1' y otra el 'lateral2'.
#Hará sus cálculos tanto para la una como para la otra.
#
#Podemos entonces entender que, al llegar a la línea 80, el programa da un salto a la 62 y cambia el nombre de 'lateral1'
#por 'lado', hace sus cálculos y al acabar en la línea 64, vuelve a la 80, dejando la variable 'lado' con su nombre inicial
#pero con el nuevo valor que ha calculado.
#
#No existe un límite de parámetros que podamos pasar a una subrutina. Podemos por ejemplo:

def Newton (base, altura):
    area = base*altura
    return base

#Hemos definido una función Newton que recibe 2 parámetros, base y altura. Calcula el área del rectángulo y la devuelve.

base=2
altura=3
print (Newton(base,altura))
