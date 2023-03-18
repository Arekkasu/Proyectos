import time
import pandas as pd
import random
from termcolor import colored, cprint

Workers_csv = pd.read_csv("Assets/workers.csv")
Products_csv = pd.read_csv("Assets/products.csv")

pd.options.display.max_rows = None

sep = '--------------------------------------------------------------------------'

def read_again_datas():

    """
    Se decide llamar la variable correspondiente al dataframe y se le asigna que se lea nuevamente en una variable,
    permitiendo que se mantega la lectura desde su ultima modificacion y al final con la funcion concat(), se unen los
    data frames y se genera uno solo
    """
    global Workers_csv
    global Products_csv
    new_data_workers = pd.read_csv('Assets/workers.csv')
    new_data_products = pd.read_csv('Assets/products.csv')
                                                    #Se seleciona verdadero para que consever el orden del index
    Workers_csv = pd.concat([Workers_csv, new_data_workers], ignore_index=True)
    Products_csv = pd.concat([Products_csv, new_data_products], ignore_index=True)



def registrar_Empleado(name, last_name, sex, age, mobile_number, username, password,selling_products = 0):

    if ((Workers_csv['name'] == name) & (Workers_csv['last_name'] == last_name) & (Workers_csv['cel_number'] == mobile_number)).any():
        output = cprint(f"El siguiente empleado {name} {last_name}, ya se encuentra registrado", "red")
    else:
        with open('Assets/workers.csv', mode='+a') as workers:
            workers.write(f"{name},{last_name},{sex},{age},{mobile_number},{username}, {password},{selling_products}\n")
            workers.close()
        time.sleep(2)
        output = cprint("Empleado Registrado Correctamente", "green")
    return output

def registrar_producto(id_product, name_product, price, quantity):

    with open('Assets/products.csv', mode = 'a+') as products:
        products.write(f"\n{id_product},{name_product},{price},{quantity}")
    products.close()

def existencia_producto(name_product):
    try:
        # Detecta el indice del dataframe si esta registrado o no
        row = Products_csv.loc[Products_csv["name_product"] == name_product]
        row_id = row.index[0]
        return print(f"El producto {name_product.capitalize()} existe y hay {Products_csv.loc[row_id, 'quantity']} unidades disponibles.\nsu precio es {Products_csv.loc[row_id, 'price']}")
    except:
        # Al no estar registrado o no existe en el dataframe regresara el mensaje que no existe
        return print(f"El producto {name_product} no existe")

def products_list():
    print(Products_csv)

def username_and_password(name, last_name):
    x = name[0:3]+'_'+last_name[0:4]
    y = str(random.randint(111,999))+name[::3]
    return x, y




def main():
    cprint("------------------------------GESTOR VENTAS----------------------------\n", 'yellow')
    while True:

        command = input(f"Ingresa un comando, en caso de no conocer un comando ingrese \'{colored('help', 'green', 'on_dark_grey')}\': ").upper()


        """
        OPCION DE REGISTRO DE EMPLEADO, EL CUAL PEDIRA LOS DATOS, Y SE GENERA UNA USERNAME Y UNA CONTRASENA MEDIANTE UNA FUNCION
        """
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
                    username, password = username_and_password(name, last_name)
                    read_again_datas()
                    registrar_Empleado(name, last_name, sex, age, cel_number, username, password)

                except:
                    cprint("\nERROR AL REGISTRAR EL USAURIO, INGRESA TODOS LOS DATOS", 'red')
                    continue

            # REGISTRAR PRODUCTO
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