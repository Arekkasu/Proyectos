'''Esto es un proyecto de inventario de Tienda
   Tratando de aplicar lo aprendido en el curso de python 
   de la universidad Nacional de colombia PT.1'''
print()

print('Bienvenido'.center(100,'-'))

print()

print('Para conocer los comandos ingrese \'Help\'')
Inv = {} #Diccionario donde se almacena los datos

print()

while True:
   comando = str(input(('Ingresa un comando: ')))
   print()
   comand = comando.upper()

   if comand == 'AGREGAR':

      name_item = input('Ingrese el nombre del item: ')
      print()
      name_item = name_item.upper()
      amount_item = int(input('Ingrese la cantidad: '))
      print()
      value_item = int(input('Ingrese el valor: '))

      if name_item not in Inv:
         Inv[name_item] = list()

      Inv[name_item].append(amount_item) #Cantidad de item tiene como indice 0 en la lista
      Inv[name_item].append(int(value_item)) #Valor tiene como indice en la lista como 1
      print()
      continue

   if comand == 'COMPRA':

      cop_security = {item: [Cantidad, Precio] for item, (Cantidad, Precio) in Inv.items()}
      total = [] #Ira almacenando el costo por producto que se ingrese para luego ser sumado

      while True: #En este ciclo se empezara el proceso de compra

         name_item = input('Ingrese el nombre del item: ')
         name_item.upper()
         print()
         if name_item not in Inv:
               print('El Articulo no esta registrado en el inventario')
               print()
               continue
         amount_item = int(input('Cuantos llevara: '))
         print()
         values_dict = Inv[name_item]
         amount = values_dict[0] # --> Cantidad que hay en el inventario
         if amount < amount_item:
                  if amount == 0:
                     print(f'No hay unidades en el inventario')
                     continue
                  if amount == 1:
                     print('Hay 1 unidad en el inventario')
                     continue
                  print(f'Hay {amount} unidades en el inventario')
                  continue
         valor = values_dict[1] # --> Valor del item
         Inv[name_item].remove(amount) #Remueve la cantidad que tenia
         amount = int(amount-amount_item)
         Inv[name_item].insert(0, amount)
         total.append(valor*amount_item)
         Total = sum(total)
         
         comando = str(input('Ingresa \'Y\' si desea continuar, Ingresa \'N\' si acabo el proceso: '))
         comand = comando.upper()

         if comand == 'Y':
               continue

         if comand == 'N':
               print(f'El total es: {Total}')
               client = int(input('Ingrese el valor: '))
               if client < Total:
                  print('Dinero Insuficiente para pagar.')
                  print()
                  print(client-Total)
                  print()
                  print('La compra se cancela')
                  Inv = cop_security
                  break
               print(f'Valor: {Total} Cliente: {client} Cambio: {Total-client}')
               break
         print()
         continue
   elif comand == 'LISTAR':
         if len(Inv) == 0:
               print('No hay nada en el inventario para hacer lista')
               continue
         
         print('')
         list = 1
         print('\t\tIndice\t\tNombre\t\tCantidad\t\tValor')
         print()
         for nombre, (cantidad, valor) in Inv.items(): # --> Iterara sobre las parejas que hay en el diccionario, por eso la funcion .items()
            print(f'\t\t{list}\t\t{nombre}\t\t{cantidad}\t\t\t{valor}')
            print()
            list += 1
         print()
         continue
   elif comand == 'DETENER':
      print('Fin del proceso')
      break
   elif comand == 'HELP':
      print('Los comandos son los siguientes: Agregar, Compra, Listar')
      print()
      continue
   else:
      print(f'{comand} no existe como opcion, Ingresa \'help\' para conocer los comandos')