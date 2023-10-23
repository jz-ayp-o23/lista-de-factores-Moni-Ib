"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
numeros = []

# Entradas
entrada = int(input("¿De qué número desea los factores? "))

# Proceso
for numero in range(1, entrada + 1):
    if entrada % numero == 0:
        numeros.append(numero)
print(f"Los factores de {entrada} son: {numeros}")

