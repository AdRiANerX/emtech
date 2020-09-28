"""
#ULISES ADRIAN GÓMEZ RICO
#GRUPO 4
#PROYECTO 02 EMTECH
"""
import csv
import sys #PARA PODER TERMINAR EL PROGRAMA
import os #PARA PODER LIMPIAR LA PANTALLA
from operator import itemgetter #PARA PODER USAR KEY EN SORTED

routes_list = []
value_global = 0


# Función que agrega una nueva ruta si esta no existe
def newRoute(row):
  direction = row[1]
  origin = row[2]
  destination = row[3]
  product = row[6]
  transport_mode = row[7]
  company_name = row[8]
  total_value = row[9]

  routes_list.append(
    {
      "direction": direction,
      "origin": origin,
      "destination": destination,
      "product": product,
      "transport_mode": transport_mode,
      "company_name": company_name,
      "total_records": 1,
      "total_sum": int(total_value)
    }
  )
# Fin de newRoute

# Función que verifica si ya existe la ruta o no
def verifyRoute(row):
  global value_global
  direction = row[1]
  origin = row[2]
  destination = row[3]
  total_value = row[9]

  #Realizamos la suma del costo/ganancia de todas las transacciones
  value_global +=  int(total_value) 

  if routes_list == []:
    # Crear la primera ruta
    newRoute(row)
  else:
    flag = False
    # Comparamos con la fila con la todas las rutas para saber si ya existe la ruta o creamos una nueva
    for route in routes_list:
      if route["direction"] == direction and route["origin"] == origin and route["destination"] == destination :
        # Sumar a la ruta creada
        route["total_records"] += 1
        route["total_sum"] += int(total_value)
        flag = True
        break

    if flag == False:
      # Se crea una nueva ruta en caso de no existir
      newRoute(row)
# Fin de verifyRoute

def print_routes_details():
  cont_routes = 0

  cont_sea = 0
  sea_value = 0
  cont_air = 0
  air_value = 0
  cont_rail = 0
  rail_value = 0
  cont_road = 0
  road_value = 0

  cont_imports = 0
  total_value_imports = 0

  cont_exports = 0
  total_value_exports = 0

  print("\nDetalles de las rutas\n\n")
  for route in routes_list:
    cont_routes += 1

    # Contamos solo importaciones y exportaciones
    if route["direction"] == "Imports":
      cont_imports += 1
      total_value_imports += route["total_sum"]
    else:
      cont_exports += 1
      total_value_exports += route["total_sum"]
    
    # Contamos el medio de transporte
    if route["transport_mode"] == "Air":
      cont_air += 1
      air_value += route["total_sum"]
    if route["transport_mode"] == "Sea":
      cont_sea += 1
      sea_value += route["total_sum"]
    if route["transport_mode"] == "Rail":
      cont_rail += 1
      rail_value += route["total_sum"]
    if route["transport_mode"] == "Road":
      cont_road += 1
      road_value += route["total_sum"]


    print("Dirección: ", route["direction"])
    print("Origen: ", route["origin"])
    print("Destino: ", route["destination"])
    print("Producto: ", route["product"])
    print("Modo de Transporte: ", route["transport_mode"])
    print("Compañia: ", route["company_name"])
    print("Número de registros: ", route["total_records"])
    print("Valor total: {:,.2f}".format( route["total_sum"] ))
    print("Porcentaje sobre el valor global: {:,.3f}%".format( route["total_sum"]*100/value_global ) )
    print("\n\n")

  print("Resumen de medios de transporte")
  print("Valor total de importaciones: {:,.2f}".format( total_value_imports ) )
  print("Valor total de exportaciones: {:,.2f}".format( total_value_exports ) )
  print("\n")
  print("Valor total por aire: {:,.2f}".format( air_value ) )
  print("Porcentaje sobre el valor global: {:,.3f}%".format( air_value*100/value_global ) )
  print("Número de imp/exp por aire: ", cont_air )
  print("\n")
  print("Valor total por carretera: {:,.2f}".format( road_value ) )
  print("Porcentaje sobre el valor global: {:,.3f}%".format( road_value*100/value_global ) )
  print("Número de imp/exp por carretera: ", cont_road )
  print("\n")
  print("Valor total por mar: {:,.2f}".format( sea_value ) )
  print("Porcentaje sobre el valor global: {:,.3f}%".format( sea_value*100/value_global ) )
  print("Número de imp/exp por mar: ", cont_sea )
  print("\n")
  print("Valor total por tren: {:,.2f}".format( rail_value ) )
  print("Porcentaje sobre el valor global: {:,.3f}%".format( rail_value*100/value_global ) )
  print("Número de imp/exp por tren: ", cont_rail )
# Fin de print_routes_details

def best_routes():
  #Ordenamos las rutas de mayor a menor
  routes_order_list = sorted(routes_list, key=lambda row: row['total_sum'], reverse=True)

  # Contamos cuantas rutas nos generan el 80% y 20% de ingresos
  cont_routes_80 = 0
  cont_routes_20 = 0
  countries_80 = []
  countries_20 = []
  for route in routes_order_list :
    if (cont_routes_80*100/value_global) < 80 :
      cont_routes_80 += route["total_sum"]
      if route["origin"] not in countries_80 :
        countries_80.append( route["origin"] )
      if route["destination"] not in countries_80 :
        countries_80.append( route["destination"] )
    else:
      cont_routes_20 += route["total_sum"]
      if route["origin"] not in countries_20 :
        countries_20.append( route["origin"] )
      if route["destination"] not in countries_20 :
        countries_20.append( route["destination"] )

  # Impresión de las 10 mejores rutas
  print("\n- . - . 10 Mejores rutas\n")
  cont = 0
  for route in routes_order_list :
    print("# # Ruta ", cont+1)
    print("Dirección: ", route["direction"])
    print("Origen: ", route["origin"])
    print("Destino: ", route["destination"])
    print("Producto: ", route["product"])
    print("Modo de Transporte: ", route["transport_mode"])
    print("Compañia: ", route["company_name"])
    print("Número de registros: ", route["total_records"])
    print("Valor total: {:,.2f}".format( route["total_sum"] ))
    print("Porcentaje sobre el valor global: {:,.3f}%".format( route["total_sum"]*100/value_global ) )
    print("\n\n")
    cont += 1
    if cont == 10:
      break

  print("80 - 20 de las rutas\n")

  print("Cantidad total sobre el 80% de las mejores rutas: {:,.2f}".format( cont_routes_80 ))
  print("Lista de paises que se encuentran en el 80%")
  for contry in countries_80:
    print(contry)
  print("\n")

  print("Cantidad total sobre el 20% de las rutas restantes: {:,.2f}".format( cont_routes_20 ))
  print("Lista de paises que se encuentran en el 20%")
  for contry in countries_20:
    print(contry)
  print("\n")
  
  cont_min_contries = 0
  cont_min_routes = 0
  _80s = set( countries_80 )
  _20s = set( countries_20 )
  list_min_contries = list( _20s.difference(_80s) )
  print("Lista de paises que NO se encuentran en el 80%" )
  for contry in list_min_contries:
    print(contry)

  for route in routes_order_list :
    if route["origin"] in list_min_contries or route["origin"] in list_min_contries :
      cont_min_contries += route["total_sum"]
      cont_min_routes += 1

  print("Valor total de los paises que no estan en el 80% {:,.2f}".format( cont_min_contries ))
  print("Cantidad de rutas en estos paises:", cont_min_routes)
  print("Porcentaje sobre el valor global: {:,.3f}%".format( cont_min_contries*100/value_global ) )
# Fin de best_routes

# INICIO DE PROGRAMA - * - * - * - * - *
with open('synergy_logistics_database.csv') as File:
    reader = csv.reader(File)
    cont = 0
    # Ciclo que lee cada fila y la manda a analizar para agruparla en la ruta correspondiente
    for row in reader:
      if cont == 0:
        cont += 1
      else:
        verifyRoute(row)

# Capturamos toda la impresion en un documento txt
sys.stdout = open("report.txt", 'wt') 
print_routes_details()
best_routes()

File.close()