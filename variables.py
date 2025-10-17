"""nombre_tienda = "Tienda de Rafa Online"  # Variable de tipo string
precio_de_tablet = 350.75  # Variable de tipo float
stock_de_tablet = 10  # Variable de tipo entero
enviado = False  # Variable de tipo booleano

stock_de_tablet = stock_de_tablet + 1
print(stock_de_tablet) # imprime 11
stock_de_tablet *= 2
print(stock_de_tablet) # imprime 12

variable_boleana = 10 > 5
print(variable_boleana) # imprime True
variable_boleana = 10 < 5
print(variable_boleana) # imprime False
variable_boleana = 10 == 5
print(variable_boleana) # imprime False
variable_boleana = 10 == 10
print(variable_boleana) # imprime True
variable_boleana = 10 != 5
print(variable_boleana) # imprime True
variable_boleana = 10 <= 5
print(variable_boleana) # imprime False
variable_boleana = 10 >= 5
print(variable_boleana) # imprime True
"""
print(89 < 100)
print(89 > 100)
print(100 == 100)
print(100 <= 100)
print(100 >= 100)
print(89 >= 100)
print(89 == 100)
print(100 == 100)
print(89 != 100)
lista = ["Laptop", 1500.00, "Electronica"] # se puede modifica
tupla = ('Laptop', 1500.00, 'Electronica') # no se puede modificar
diccionario = {  # clave: valor
   'nombre': 'Laptop',
   'precio': 1500.00,
   'departamento': 'Electronica'
} # Variable de tipo diccionario
print(lista[2])
print(tupla[0])
print(diccionario['departamento'])

#conversion de tipos
numero_entero = 100
print(numero_entero, type(numero_entero))
numero_en_string = str(numero_entero)
print(numero_en_string, type(numero_en_string)) # "100"

numero_flotante = float(numero_entero)
print(numero_flotante, type(numero_flotante)) # 100.0
3.9516
print((round(3.9516,3)))

boleano_falso = False # False ==> 0
boleano_verdadero = True # True ==> 1
boleano_entero = int(boleano_verdadero)
print(boleano_entero, type(boleano_entero)) # 0

entero = 15
boleano = bool(entero)
print(boleano, type(boleano)) # True