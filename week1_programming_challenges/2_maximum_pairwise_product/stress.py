import random
import sys
import os

# Aceptar el numero de tests como un comando en la linea de parametros
tests = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(tests):
    print("Test #" + str(i))
    # Ejecutar el archivo de la prueba de estres con el parametro n y la semilla i
    os.system("python generator.py " + str(n) + " " + str(i) + " > input.txt")
    # Ejecutar el primer modelo
    os.system("python opt.py <input.txt > main.txt")
    # Ejecutar el segundo modelo
    os.system("python max_pairwise_product.py <input.txt > model.txt")

    # Leer el resultado del modelo
    with open("model.txt") as f: model = f.read()
    print("Model: ", model)
    # Leer sobre el main
    with open("main.txt") as f: main = f.read()
    print("Main: ", main)
    print("-" * 50)
    if model != main:
        break