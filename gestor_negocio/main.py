import time
import pandas as pd
import random
from termcolor import colored, cprint

Workers_csv = pd.read_csv("Assets/workers.csv", index_col = 0)
Products_csv = pd.read_csv("Assets/products.csv", index_col= 0)

pd.options.display.max_rows = None

sep = '--------------------------------------------------------------------------'

def registrar_Empleado(name, last_name, sex, age, mobile_number, selling_products = 0):
    if len(Workers_csv.index) == 100:
        text = cprint('Registro de empleados llenos', 'red')
        return text
    try:
        last_id = Workers_csv.index.max()+1
    except:
        last_id = 1
    with open('Assets/workers.csv', mode = 'a+') as workers:
        workers.write(f"\n{last_id},{name},{last_name},{sex},{age},{mobile_number}, {selling_products}")
    workers.close()
    text = cprint('\nEmpleado Registrado correctamente', 'green')
    time.sleep(2)
    return text

def registrar_producto(id_product, name_product, price, quantity):
    id = id_product
    count = 0
    while True:
        if (id in Products_csv.index) and count < 999:
            id = random.randint(0, 1000000)
        break
    with open('Assets/products.csv', mode = 'a+') as products:
        products.write(f"\n{id_product},{name_product},{price},{quantity}")
    products.close()

def existencia_producto(name_product):

    try:
        # Detecta el indice del dataframe si esta registrado o no
        row = Products_csv.loc[Products_csv["name_product"] == name_product]
        row_id = row.index[0]
        print(f"El producto {name_product.capitalize()} existe y hay {Products_csv.loc[row_id, 'quantity']} unidades disponibles.\nsu precio es {Products_csv.loc[row_id, 'price']}")
    except:
        pass
        # Al no estar registrado o no existe en el dataframe regresara el mensaje que no existe
    print(f"El producto {name_product} no existe")

def products_list():
    print(Products_csv)


def main():
    cprint("------------------------------GESTOR VENTAS----------------------------\n", 'yellow')
    while True:

        command = input(f"Ingresa un comando, en caso de no conocer un comando ingrese \'{colored('help', 'green', 'on_dark_grey')}\': ").upper()

        if command == '1':
            print(sep)
            cprint("\n-----------------Registro de empleado-----------------------\n")
            while True:
                print(f"Ingrese el nombre, apellido, sexo {colored('(M para Masculino y F para Femenino)', 'yellow')}, edad y numero de celular, separados por espacios, o ingresa \'{colored('back', 'light_blue', 'on_black')}\': ")
                command = input()
                if command == 'back':
                    break
                try:
                    name, last_name, sex, age, cel_number = command.split()
                    registrar_Empleado(name, last_name, sex, age, cel_number)
                except:
                    cprint("\nERROR AL REGISTRAR EL USAURIO, INGRESA TODOS LOS DATOS", 'red')
                    continue
        elif command == '2':
            print(f"Ingrese el nombre, apellido, sexo {colored('(M para Masculino y F para Femenino)', 'yellow')}, edad y numero de celular, separados por espacios")
            name, last_name, sex, age, cel_number = input().split()
            registrar_Empleado(random.randint(0, 1000000), name, last_name, sex, age, cel_number)
            pass
        elif command == '3':
            pass
        elif command == '4':
            products_list()
        elif command == 'HELP':
            print("Los comandos son los que se usan son los siguientes:\n\n1. Registrar Empleado\n2. Registrar Producto\n3. Buscar producto\n4. Productos en inventario\n5.Venta\n6.Reporte Ventas\n")
            cprint(sep, 'red')
            time.sleep(2)
        elif command == 'STOP':
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()