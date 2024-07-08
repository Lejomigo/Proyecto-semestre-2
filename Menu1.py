import Funciones
import pickle
import time
matrizHotel =Funciones.cargardatos()
# [0] = Num hab
# [1] = tipo de hab 0 sencilla 1 doble 2 suite 3 presidencial
# [2] = estado de hab 0 libre 1 reservada 2 ocupada
# [3] = fecha de entrada
# [4] = fecha de salida
# [5] = nombre de habitante
# [6] = ci del habitante


while True:
     # print(matrizHotel)
     time.sleep(1)
     print('-------------------------------------------------')
     print('      MENÚ DEL HOTEL CHARALLAVE and SUITES       ')
     print('-------------------------------------------------')
     print('1) Deseo ver la disponibilidad de habitaciones.')
     print('2) Deseo buscar una habitación. ')
     print('3) Deseo hacer un check in.')
     print('4) Deseo hacer un check out.')
     print('5) Gestionar Reservación.')
     print('6) Salir del Menú')
     print()
     accion=input('Qué desea hacer?: ')

     if accion =='1':
          Funciones.verDisponibilidad(matrizHotel)
     elif accion =='2':
          Funciones.buscarUnaHab(matrizHotel)
     elif accion =='3':
          matrizHotel =Funciones.chekIn(matrizHotel)
          Funciones.guardarMatriz(matrizHotel,'Habitaciones.bin')
     elif accion =='4':
          matrizHotel = Funciones.checkOut(matrizHotel)
          Funciones.guardarMatriz(matrizHotel,'Habitaciones.bin')
     elif accion =='5':
          matrizHotel = Funciones.reservacion(matrizHotel)
          Funciones.guardarMatriz(matrizHotel,'Habitaciones.bin')
     elif accion =='6':
          print('Vuelva pronto.')
          break
     else:
          print('Opción incorrecta. ')
          True
          


            
            
