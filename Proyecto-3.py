texto = input('dime el texto que quieres: ')
letra1 = input('dime la primera letra para contar: ')
letra2 = input('dime la segunda letra para contar: ')
letra3 = input('dime la tercera letra para contar: ')

texto = texto.lower()
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

cuenta_letra1 = texto.count(letra1)
cuenta_letra2 = texto.count(letra2)
cuenta_letra3 = texto.count(letra3)

print('la letra ' + letra1 + ' esta ' + str(cuenta_letra1) + ' veces')
print('la letra ' + letra2 + ' esta ' + str(cuenta_letra2) + ' veces')
print('la letra ' + letra3 + ' esta ' + str(cuenta_letra3) + ' veces')

# 2
palabras = texto.split()
cuenta_palabras = len(palabras)
print('Este es el recuento de palabras: ' + str(cuenta_palabras))

# 3
letra_primera = texto[0]
letra_ultima = texto[-1]
print('Esta es la primera letra: ' + letra_primera + '\n' +'Esta es la ultima letra: ' + letra_ultima)

# 4
palabras = texto.split()
invertir_palabra = palabras[::-1]
texto_invertido = ' '.join(invertir_palabra)
print(texto_invertido)

# 5
if 'python' in texto.lower():
    print('La palabra python esta')
else:
    print('La palabra python no esta')