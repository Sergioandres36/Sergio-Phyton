# 1
palabra = 'escritorio'
print(palabra[2])

# 2
palabra = 'No es por nada, pero este videojuego es demasiado fáci'
indice = palabra.find('videojuego')
print(indice)

# 3
palabra = 'Tengo que asegurarme de comprobar el ejercicio para que no tenga errores'
indice = palabra.rfind('ejercicio')
print(indice)

# 4
palabra = 'Escribir código es fundamental para aprender programación'
indice = palabra[0:8]
print(indice)

# 5 
palabra = 'Python es uno de los lenguajes más populares de la actualidad'
indice = palabra[6::3]
print(indice)

# 6
palabra = 'Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida'
indice = palabra[::-1]
print(indice)

# 7
palabra = 'Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programació'
indice = palabra.upper()
print(indice)

# 8
palabras = ["Este", "curso", "me", "gusta"]
indice = ' '.join(palabras)
print(indice)

# 9
palabra = 'No sé con cuál quedarme, si con el primero o con el segundo'
indice = palabra.replace('el primero', 'JavaScript').replace('el segundo', 'Python')
print(indice) 

# 10
palabra = 'Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado'
print(palabra)
indice = 'trabajo' in palabra
print(indice)

# 11
palabra = 'Python'
indice = palabra * 12
print(indice)

# 12 
palabra = 'esternocleidomastoideo'
print(len(palabra))

# 13
lista = ['python', 'sergio', {'a','b','c'},[1, 2, 3],11.24, (27, 28, 29),]
print(lista)

# 14 
lista = ["Python", "Ruby", "PHP", "CSS"]
lista.append('JavaScript')
print(lista)

# 15
lista = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "LG"]
lista.pop(5)
print(lista)

# 16 
diccionario = {'nombre':'Sergio', 'apellido':'Grisales', 'edad':'30', 'profesión':'soporte informatico'}

#17
print(diccionario['apellido'])

# 18
diccionario = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28}
diccionario["pais"] = ("España")
print(diccionario)

# 19
tupla_ejercicio = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)
contar = tupla_ejercicio.count(3)
print(contar)

# 20
tupla_ejercicio = (1, 2, 3, 4, 5, 1, 2, 3, 4)
lista = list(tupla_ejercicio)
print(lista)

# 21 
tupla_ejercicio = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")
a, b, c, d, e, f = tupla_ejercicio
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('e:', e)
print('f:', f)

# 22
set_1 = {8, 10, "once", "doce"}
set_2 = {"once", 4, 5}
set_3 = set_1.union(set_2)
print(set_3)

# 23
loteria = {"Python", "Java", "SQL", "jQuery", "Git", "Github"}
aleatorio = loteria.pop()
print(aleatorio)

# 24
nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}
nombres.add('Lorenzo')
print(nombres)

#25
comparacion = (27 >= 23)
print(comparacion)

#26
numero_1 = 19238 / 38
numero_2 = 92*59
comparacion = (numero_1 > numero_2)
print(comparacion)

#27 
raiz_cuadrada = 25 ** 0.5
verifica = (raiz_cuadrada == 5)
print(verifica)