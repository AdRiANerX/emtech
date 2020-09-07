"""
#ULISES ADRIAN GÓMEZ RICO
#GRUPO 4
#PROYECTO 01 EMTECH
"""
import sys as System #PARA PODER TERMINAR EL PROGRAMA
import os #PARA PODER LIMPIAR LA PANTALLA
from operator import itemgetter #PARA PODER USAR KEY EN SORTED
from lifestore_file import * #IMPORTACIÓN DEL DATA SET

os.system("cls")
print("\n  Bienvenido a LifeSotore System")

#Ciclo que repite el menú hasta que el usuario desee salir del sistema
#Dentro del ciclo se encuentra otros 2 ciclos, uno para administrador y otro para usuario
while True:
  print("""
  ########################################
  #  Por favor ingresa la opción deseada #
  #  1 - Ingresar como administrador     #
  #  2 - Ingresar como usuario           #
  #  3 - Salir del sistema               #
  ########################################
  """)
  opcion = input("  OPCION: ")

  #Administrador
  if opcion == "1":
    os.system("cls")
    #Validación de contraseña
    print("Por favor ingresa la contraseña como administrador.")
    pssw = input("Contraseña: ")
    if pssw != "123456":
      os.system("cls")
      print("La contraseña es incorrecta")
    else:
      os.system("cls")
      print("#  Bienvenido Administrador")
      while True:
        print("""
    
    #  Por favor ingresa la opción deseada 
    #   1 - Visualizar 50 Productos con mayores ventas     
    #   2 - Visualizar 100 Productos con mayores busquedas 
    #   3 - Visualizar 50 Productos con menores ventas por categoría   
    #   4 - Visualizar 100 Productos con menores busquedas por categoría
    #   5 - Visualizar 20 Productos con mejores reseñas 
    #   6 - Visualizar 20 Productos con peores reseñas 
    #   7 - Visualizar reporte de ventas (total de ingresos y desglose por mes)
    #   9 - Regresar al menú principal               
    #  10 - Salir del sistema               
  
        """)
        opcion = input("  OPCION: ")
        if opcion == "1":
          os.system("cls")
          print("\n    50 Productos con mayores ventas")
          lista_ventas_por_producto = []
          id_producto = 1
          contador = 0
          #Busqueda de ventas por producto
          while id_producto <= 96:
            for x in lifestore_sales:
              if( x[1] == id_producto):
                contador += 1
            lista_ventas_por_producto.append( [id_producto,contador] )
            contador = 0
            id_producto += 1

          #Ordenamiento de la nueva lista creada de los productos mas vendidos
          cincuenta_mejores = sorted( lista_ventas_por_producto, key=itemgetter(1), reverse=True )

          #Impresion de la lista
          contador = 0
          print("Ventas\t -  Producto")
          for x in cincuenta_mejores:
            # print(x)
            print("  ", x[1], "\t - " ,lifestore_products[ x[0]-1 ][1] )
            contador += 1
            if contador == 50:
              break
        
        if opcion == "2":
          os.system("cls")
          print("\n    100 Productos con mayores busquedas")
          lista_busquedas_por_producto = []
          id_producto = 1
          contador = 0
          #Busqueda de busqeudas por producto
          while id_producto <= 96:
            for x in lifestore_searches:
              if( x[1] == id_producto):
                contador += 1
            lista_busquedas_por_producto.append( [id_producto,contador] )
            contador = 0
            id_producto += 1

          cien_mejores = sorted( lista_busquedas_por_producto, key=itemgetter(1), reverse=True )
          contador = 0
          print("Busquedas\t -  Producto")
          for x in cien_mejores:
            # print(x)
            print("  ", x[1], "\t - " ,lifestore_products[ x[0]-1 ][1] )
            contador += 1
            if contador == 100:
              break

        if opcion == "3":
          os.system("cls")
          print("\n    50 Productos con menores ventas por categoría")
          lista_ventas_por_producto = []
          id_producto = 1
          contador = 0
          while id_producto <= 96:
            for x in lifestore_sales:
              if( x[1] == id_producto ):
                contador += 1
            lista_ventas_por_producto.append( [id_producto,contador] )
            contador = 0
            id_producto += 1

          cincuenta_peores = sorted( lista_ventas_por_producto, key=itemgetter(1) )

          contador = 0
          print("Ventas\t -  Producto")
          for x in cincuenta_peores:
            # print(x)
            print("  ", x[1], "\t - " ,lifestore_products[ x[0]-1 ][1] )
            contador += 1
            if contador == 50:
              break
          print("\n\n - - - - - - - - - - - - - - - - - - - - - - \n\n   POR CATEGORÍAS \n\n" )

          # Se crea una lista de las categorias existentes
          lista_categorias = []
          lista_categorias.append( lifestore_products[0][3] )
          for x in lifestore_products:
            if x[3] in lista_categorias:
              continue
            else:
              lista_categorias.append( x[3] )
    
          for categoria in lista_categorias:
            print("   " ,  categoria.upper() )
            contador = 0
            print("Ventas\t -  Producto")
            for x in cincuenta_peores:
              if lifestore_products[ x[0]-1 ][3] == categoria:
                print("  ", x[1], "\t - " ,lifestore_products[ x[0]-1 ][1] )
              contador += 1
            print("\n")
        
        if opcion == "4":
          os.system("cls")
          print("\n    100 Productos con menores busquedas por categoría")
          lista_busquedas_por_producto = []
          id_producto = 1
          contador = 0
          while id_producto <= 96:
            for x in lifestore_searches:
              if( x[1] == id_producto):
                contador += 1
            lista_busquedas_por_producto.append( [id_producto,contador] )
            contador = 0
            id_producto += 1

          cien_peores_busquedas = sorted( lista_busquedas_por_producto, key=itemgetter(1) )

          contador = 0
          print("Busquedas\t -  Producto")
          for x in cien_peores_busquedas:
            # print(x)
            print("  ", x[1], "\t - " ,lifestore_products[ x[0]-1 ][1] )
            contador += 1
            if contador == 100:
              break
          print("\n\n - - - - - - - - - - - - - - - - - - - - - - \n\n   POR CATEGORÍAS \n\n" )

          # Se crea una lista de las categorias existentes
          lista_categorias = []
          lista_categorias.append( lifestore_products[0][3] )
          for x in lifestore_products:
            if x[3] in lista_categorias:
              continue
            else:
              lista_categorias.append( x[3] )
    
          for categoria in lista_categorias:
            print("   " ,  categoria.upper() )
            contador = 0
            print("Busquedas\t -  Producto")
            for x in cien_peores_busquedas:
              if lifestore_products[ x[0]-1 ][3] == categoria:
                print("  ", x[1], "\t - " ,lifestore_products[ x[0]-1 ][1] )
              contador += 1
            print("\n")
        
        if opcion == "5":
          os.system("cls")
          print("\n    20 Productos con mejores reseñas\n")
          mejores_productos = []
          id_producto = 1
          contador = 0
          contador_resena = 0
          contador_devolucion = 0
          while id_producto <= 96:
            for x in lifestore_sales:
              if( x[1] == id_producto ):
                contador += 1
                contador_resena += x[2]
                if( x[4] == 1 ):
                  contador_devolucion += 1
              if contador != 0:
                prom = contador_resena/contador
                prom = round(prom,1)
              else:
                prom = 0
            mejores_productos.append( [id_producto,contador,prom,contador_devolucion] )
            contador = 0
            contador_resena = 0
            contador_devolucion = 0
            id_producto += 1

          veinte_mejores = sorted( mejores_productos, key=itemgetter(2,1), reverse=True )
        
          contador = 0
          print("Reseña\t - Ventas\t -  Producto \n")
          for x in veinte_mejores:
            print("  ", x[2], "\t -  ", x[1], "\t\t - ", lifestore_products[ x[0]-1 ][1] )
            contador += 1
            if contador == 20:
              break

          print("\n\n - - - - - - - - - - - - - - - - - - - - - - \n\n" )
          print("\n    20 Productos con mayores ventas y mejores reseñas\n")
          veinte_mejores = sorted( mejores_productos, key=itemgetter(1,2), reverse=True )

          contador = 0
          print("Reseña\t - Ventas\t -  Producto \n")
          for x in veinte_mejores:
            print("  ", x[2], "\t -  ", x[1], "\t\t - ", lifestore_products[ x[0]-1 ][1] )
            contador += 1
            if contador == 20:
              break

          print("\n\n - - - - - - - - - - - - - - - - - - - - - - \n\n" )      
            
        if opcion == "6":
          os.system("cls")
          print("\n    20 Productos con peores reseñas y devoluciones\n")
          peores_productos = []
          id_producto = 1
          contador = 0
          contador_resena = 0
          contador_devolucion = 0
          while id_producto <= 96:
            for x in lifestore_sales:
              if( x[1] == id_producto ):
                contador += 1
                contador_resena += x[2]
                if( x[4] == 1 ):
                  contador_devolucion += 1
              if contador != 0:
                prom = contador_resena/contador
                prom = round(prom,1)
              else:
                prom = 0
            peores_productos.append( [id_producto,contador,prom,contador_devolucion] )
            contador = 0
            contador_resena = 0
            contador_devolucion = 0
            id_producto += 1

          veinte_peores = sorted( peores_productos, key=itemgetter(2,1) )
        
          contador = 0
          print("Reseña\t - Devol    - Ventas\t - Producto \n")
          for x in veinte_peores:
            if(x[1] != 0 ):
              print(" ", x[2], "\t -  ", x[3], "     -  ", x[1], "\t -  ", lifestore_products[ x[0]-1 ][1] )
              contador += 1
            else:
              continue
            if contador == 20:
              break

          print("\n\n - - - - - - - - - - - - - - - - - - - - - - \n\n" )
          print("\n    Productos con cero ventas\n")
          contador = 0
          print("Reseña\t - Ventas\t -  Producto \n")
          for x in veinte_peores:
            if(x[1] == 0 ):
              print("  ", x[2], "\t -  ", x[1], "\t\t - ", lifestore_products[ x[0]-1 ][1] )
            contador += 1
    
        if opcion == "7":
          os.system("cls")
          print("\n    Reporte de ventas\n")
          total_ingresos_2019 = 0
          total_devoluciones_2019 = 0
          total_ingresos_2020 = 0
          total_devoluciones_2020 = 0
          #mensuales representa las ventas por mes y la cantidad de productos vendidos
          mensuales = [
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0]
          ]
          for x in lifestore_sales:
            ################2019
            if x[3][6:] == "2019":
              total_ingresos_2019 += lifestore_products[ x[1]-1 ][2]
              #si el producto es devolucion
              if x[4] == 1:
                total_ingresos_2019 -= lifestore_products[ x[1]-1 ][2]
                total_devoluciones_2019 += lifestore_products[ x[1]-1 ][2]

            ################2020
            if x[3][6:] == "2020":
              total_ingresos_2020 += lifestore_products[ x[1]-1 ][2]
              #si el producto es devolucion
              if x[4] == 1:
                total_ingresos_2020 -= lifestore_products[ x[1]-1 ][2]
                total_devoluciones_2020 += lifestore_products[ x[1]-1 ][2]
              #si el producto se vendio en enero
              if x[3][3:5] == "01":
                mensuales[0][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[0][1] += 1
              if x[3][3:5] == "02":
                mensuales[1][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[1][1] += 1
              if x[3][3:5] == "03":
                mensuales[2][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[2][1] += 1
              if x[3][3:5] == "04":
                mensuales[3][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[3][1] += 1
              if x[3][3:5] == "05":
                mensuales[4][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[4][1] += 1
              if x[3][3:5] == "06":
                mensuales[5][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[5][1] += 1
              if x[3][3:5] == "07":
                mensuales[6][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[6][1] += 1
              if x[3][3:5] == "08":
                mensuales[7][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[7][1] += 1
              if x[3][3:5] == "09":
                mensuales[8][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[8][1] += 1
              if x[3][3:5] == "10":
                mensuales[9][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[9][1] += 1
              if x[3][3:5] == "11":
                mensuales[10][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[1][1] += 1
              if x[3][3:5] == "12":
                mensuales[11][0] += lifestore_products[ x[1]-1 ][2]
                mensuales[1][1] += 1
          
          print("\n-- -- 2019 -- --\n")
          print("Total de ingresos 2019 - $",round(total_ingresos_2019,2) )
          print("Total de devoluciones 2019 - $",round(total_devoluciones_2019,2) )
          print("\n-- -- 2020 -- --\n")
          print("Total de ingresos 2020 - $",round(total_ingresos_2020,2) )
          print("Total de devoluciones 2020 - $",round(total_devoluciones_2020,2) )
          print("\n\tENERO")
          print("  Ingreso de ventas : $",round(mensuales[0][0],2) )
          print("  Número de ventas  : ", mensuales[0][1])
          if mensuales[0][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[0][0]/mensuales[0][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tFEBRERO")
          print("  Ingreso de ventas : $",round(mensuales[1][0],2) )
          print("  Número de ventas  : ", mensuales[1][1])
          if mensuales[1][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[1][0]/mensuales[1][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tMARZO")
          print("  Ingreso de ventas : $",round(mensuales[2][0],2) )
          print("  Número de ventas  : ", mensuales[2][1])
          if mensuales[2][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[2][0]/mensuales[2][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tABRIL")
          print("  Ingreso de ventas : $",round(mensuales[3][0],2) )
          print("  Número de ventas  : ", mensuales[3][1])
          if mensuales[3][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[3][0]/mensuales[3][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tMAYO")
          print("  Ingreso de ventas : $",round(mensuales[4][0],2) )
          print("  Número de ventas  : ", mensuales[4][1])
          if mensuales[4][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[4][0]/mensuales[4][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tJUNIO")
          print("  Ingreso de ventas : $",round(mensuales[5][0],2) )
          print("  Número de ventas  : ", mensuales[5][1])
          if mensuales[5][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[5][0]/mensuales[5][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tJULIO")
          print("  Ingreso de ventas : $",round(mensuales[6][0],2) )
          print("  Número de ventas  : ", mensuales[6][1])
          if mensuales[6][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[6][0]/mensuales[6][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tAGOSTO")
          print("  Ingreso de ventas : $",round(mensuales[7][0],2) )
          print("  Número de ventas  : ", mensuales[7][1])
          if mensuales[7][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[7][0]/mensuales[7][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tSEPTIEMBRE")
          print("  Ingreso de ventas : $",round(mensuales[8][0],2) )
          print("  Número de ventas  : ", mensuales[8][1])
          if mensuales[8][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[8][0]/mensuales[8][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tOCTUBRE")
          print("  Ingreso de ventas : $",round(mensuales[9][0],2) )
          print("  Número de ventas  : ", mensuales[9][1])
          if mensuales[9][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[9][0]/mensuales[9][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tNOVIEMBRE")
          print("  Ingreso de ventas : $",round(mensuales[10][0],2) )
          print("  Número de ventas  : ", mensuales[10][1])
          if mensuales[10][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[10][0]/mensuales[10][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          print("\n\tDICIEMBE")
          print("  Ingreso de ventas : $",round(mensuales[11][0],2) )
          print("  Número de ventas  : ", mensuales[11][1])
          if mensuales[11][1] != 0:
            print("  Promedio mensual  : $",round(mensuales[11][0]/mensuales[11][1],2))
          else:
            print("  Promedio mensual  : $0.00")
          

          mejores_meses = sorted( mensuales, key=itemgetter(0) )
            


        #Regresar al menú anterior
        if opcion == "9":
          opcion = None
          break

        # Salir del sistema
        if opcion == "10":
          os.system("cls")
          print("Gracias por utilizar LifeStore System")
          System.exit(0)

        #Si el usuario ingresa alguna opcion que no se encuentre se captura y se le manda un mensaje
        #para que indique una opcion valida
        if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7" and opcion != "9" and opcion != "10":
          os.system("cls")
          print("Por favor introduce una opción valida.")
          print("Intentalo nuevamente.")


      os.system("cls")

  #Usuario
  if opcion == "2":
    os.system("cls")
    while True:
      print("""
  #  Bienvenido Usuario
  #  Por favor ingresa la opción deseada 
  #   1 - Visualizar reporte de ventas (total de ingresos y desglose por mes)
  #   9 - Regresar al menú principal               
  #  10 - Salir del sistema               
 
      """)
      opcion = input("  OPCION: ")

      if opcion == "1":
        os.system("cls")
        print("\n    Reporte de ventas\n")
        total_ingresos_2019 = 0
        total_devoluciones_2019 = 0
        total_ingresos_2020 = 0
        total_devoluciones_2020 = 0
        #mensuales representa las ventas por mes y la cantidad de productos vendidos
        mensuales = [
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0],
          [0,0]
        ]
        for x in lifestore_sales:
          ################2019
          if x[3][6:] == "2019":
            total_ingresos_2019 += lifestore_products[ x[1]-1 ][2]
            #si el producto es devolucion
            if x[4] == 1:
              total_ingresos_2019 -= lifestore_products[ x[1]-1 ][2]
              total_devoluciones_2019 += lifestore_products[ x[1]-1 ][2]

          ################2020
          if x[3][6:] == "2020":
            total_ingresos_2020 += lifestore_products[ x[1]-1 ][2]
            #si el producto es devolucion
            if x[4] == 1:
              total_ingresos_2020 -= lifestore_products[ x[1]-1 ][2]
              total_devoluciones_2020 += lifestore_products[ x[1]-1 ][2]
            #si el producto se vendio en enero
            if x[3][3:5] == "01":
              mensuales[0][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[0][1] += 1
            if x[3][3:5] == "02":
              mensuales[1][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[1][1] += 1
            if x[3][3:5] == "03":
              mensuales[2][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[2][1] += 1
            if x[3][3:5] == "04":
              mensuales[3][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[3][1] += 1
            if x[3][3:5] == "05":
              mensuales[4][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[4][1] += 1
            if x[3][3:5] == "06":
              mensuales[5][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[5][1] += 1
            if x[3][3:5] == "07":
              mensuales[6][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[6][1] += 1
            if x[3][3:5] == "08":
              mensuales[7][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[7][1] += 1
            if x[3][3:5] == "09":
              mensuales[8][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[8][1] += 1
            if x[3][3:5] == "10":
              mensuales[9][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[9][1] += 1
            if x[3][3:5] == "11":
              mensuales[10][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[1][1] += 1
            if x[3][3:5] == "12":
              mensuales[11][0] += lifestore_products[ x[1]-1 ][2]
              mensuales[1][1] += 1
        
        print("\n-- -- 2019 -- --\n")
        print("Total de ingresos 2019 - $",round(total_ingresos_2019,2) )
        print("Total de devoluciones 2019 - $",round(total_devoluciones_2019,2) )
        print("\n-- -- 2020 -- --\n")
        print("Total de ingresos 2020 - $",round(total_ingresos_2020,2) )
        print("Total de devoluciones 2020 - $",round(total_devoluciones_2020,2) )
        print("\n\tENERO")
        print("  Ingreso de ventas : $",round(mensuales[0][0],2) )
        print("  Número de ventas  : ", mensuales[0][1])
        if mensuales[0][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[0][0]/mensuales[0][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tFEBRERO")
        print("  Ingreso de ventas : $",round(mensuales[1][0],2) )
        print("  Número de ventas  : ", mensuales[1][1])
        if mensuales[1][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[1][0]/mensuales[1][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tMARZO")
        print("  Ingreso de ventas : $",round(mensuales[2][0],2) )
        print("  Número de ventas  : ", mensuales[2][1])
        if mensuales[2][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[2][0]/mensuales[2][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tABRIL")
        print("  Ingreso de ventas : $",round(mensuales[3][0],2) )
        print("  Número de ventas  : ", mensuales[3][1])
        if mensuales[3][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[3][0]/mensuales[3][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tMAYO")
        print("  Ingreso de ventas : $",round(mensuales[4][0],2) )
        print("  Número de ventas  : ", mensuales[4][1])
        if mensuales[4][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[4][0]/mensuales[4][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tJUNIO")
        print("  Ingreso de ventas : $",round(mensuales[5][0],2) )
        print("  Número de ventas  : ", mensuales[5][1])
        if mensuales[5][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[5][0]/mensuales[5][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tJULIO")
        print("  Ingreso de ventas : $",round(mensuales[6][0],2) )
        print("  Número de ventas  : ", mensuales[6][1])
        if mensuales[6][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[6][0]/mensuales[6][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tAGOSTO")
        print("  Ingreso de ventas : $",round(mensuales[7][0],2) )
        print("  Número de ventas  : ", mensuales[7][1])
        if mensuales[7][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[7][0]/mensuales[7][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tSEPTIEMBRE")
        print("  Ingreso de ventas : $",round(mensuales[8][0],2) )
        print("  Número de ventas  : ", mensuales[8][1])
        if mensuales[8][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[8][0]/mensuales[8][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tOCTUBRE")
        print("  Ingreso de ventas : $",round(mensuales[9][0],2) )
        print("  Número de ventas  : ", mensuales[9][1])
        if mensuales[9][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[9][0]/mensuales[9][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tNOVIEMBRE")
        print("  Ingreso de ventas : $",round(mensuales[10][0],2) )
        print("  Número de ventas  : ", mensuales[10][1])
        if mensuales[10][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[10][0]/mensuales[10][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        print("\n\tDICIEMBE")
        print("  Ingreso de ventas : $",round(mensuales[11][0],2) )
        print("  Número de ventas  : ", mensuales[11][1])
        if mensuales[11][1] != 0:
          print("  Promedio mensual  : $",round(mensuales[11][0]/mensuales[11][1],2))
        else:
          print("  Promedio mensual  : $0.00")
        

        mejores_meses = sorted( mensuales, key=itemgetter(0) )
          
      #Regresar al menú anterior
      if opcion == "9":
        opcion = None
        break

      # Salir del sistema
      if opcion == "10":
        os.system("cls")
        print("Gracias por utilizar LifeStore System")
        System.exit(0)

      if opcion != "1" and opcion != "9" and opcion != "10":
        os.system("cls")
        print("Por favor introduce una opción valida.")
        print("Intentalo nuevamente.")

    os.system("cls")

  #Salida del sistema
  if opcion == "3":
    os.system("cls")
    print("Gracias por utilizar LifeStore System")
    System.exit(0)

  if opcion == None:
    continue

  #Si el usuario ingresa alguna opcion que no se encuentre se captura y se le manda un mensaje
  #para que indique una opcion valida
  if opcion != "1" and opcion != "2" and opcion != "3":
    os.system("cls")
    print("Por favor introduce una opción valida.")
    print("Intentalo nuevamente.")