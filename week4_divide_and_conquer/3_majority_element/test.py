import random
import sys
import os

# Aceptar el numero de tests como un comando en la linea de parametros
tests = int(sys.argv[1])
n = 10
vector = [x for x in range(0,n)]
for i in range(tests):
    test_file = [f"Test #{str(i)}"]
    print("Test #" + str(i))
    # Ejecutar el archivo de la prueba de estres con el parametro n y la semilla i
    os.system("python generator.py " + str(i))
    # Creación de variables para el modelo
    superior = random.randrange(n)
    if i % 10 == 0:
        dif_numbers = [x for x in range(0,n)]
    dif_numbers = [x for x in range(0, superior)]
    # Ejecutar el primer modelo
    os.system("python majority_element.py")
    
    # Actualización de variable
    n *= 5
    n = random.randrange()

    # Leer el resultado del modelo
    # with open("model.txt") as f: model = f.read()
    # print("Model: ", model)
    # # Leer sobre el main
    # with open("main.txt") as f: main = f.read()
    # print("Main: ", main)
    # print("-" * 50)
    # if model != main:
    #     break