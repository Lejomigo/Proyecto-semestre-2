import pickle
import time
import re


# [0] = Num hab
# [1] = tipo de hab 0 sencilla 1 doble 2 suite 3 presidencial
# [2] = estado de hab 0 libre 1 reservada 2 ocupada
# [3] = fecha de entrada
# [4] = fecha de salida
# [5] = nombre de habitante
# [6] = ci del habitante
#Definir los Regex
regexNombre = r"^[A-Z][a-zA-Z' -]+ [A-Z][a-zA-Z' -]+$"
patternNombre = re.compile(regexNombre)
regexCedula = r"^[VE]-\d{7,8}$"
patternCedula = re.compile(regexCedula)
regexFecha =r"^(?:(?:31/(0[13578]|1[02]))|(?:30/(0[13-9]|1[0-2]))|(?:0[1-9]|1\d|2[0-9])/(0[1-9]|1[0-2])|(?:29/02/(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:16|[2468][048]|[3579][26])00)))/\d{4}$"
patternFecha = re.compile(regexFecha)


def cargardatos():
    with open('Habitaciones.bin', 'rb') as file:
        loaded_hab = pickle.load(file)
        return loaded_hab
    return[]

def convertirFecha(fecha):
    dia, mes, año = map(int, fecha.split('/'))
    return (año, mes, dia)

def validarFechas(fecha_ingreso, fecha_salida):
    ingreso = convertirFecha(fecha_ingreso)
    salida = convertirFecha(fecha_salida)
    if salida > ingreso:
        return True
    else:
        return False

def guardarMatriz(matriz, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(matriz, f)

def validarFecha(fecha):
    if patternFecha.match(fecha):
        return True
    else:
        return False
 
def validarCedula(cedula):
    if patternCedula.match(cedula):
        return True
    else:
        return False

def validarNombre(nombre):
    if patternNombre.match(nombre):
        return True
    else:
        return False

def estadoHabitacion(estado):
    if estado==0:
        return 'Disponible'
    elif estado==1:
        return 'Reservada'
    else:
        return 'Ocupada'

def tipoDeHabitacion(tipo):
    if tipo==0:
        return 'Sencilla'
    elif tipo ==1:
        return 'Doble'
    elif tipo==2:
        return 'Suite'
    else:
        return 'Presidencial'

def verDisponibilidad(matriz):
    for i in range(len(matriz)):
        print(f"La habitacion {matriz[i][0]} está {estadoHabitacion(matriz[i][2]) } y es una habitacion {tipoDeHabitacion(matriz[i][1])}")
        if estadoHabitacion(matriz[i][2])== 'Ocupada':
            print(f'está ocupada desde el dia {matriz[i][3]} hasta el día {matriz[i][4]}')

def buscarUnaHab(matriz):
    print('-------------------------------------------------')
    print('1) Buscar por un tipo de habitación')
    print('2) Buscar por número de habitación')
    print()
    choose= int(input('Qué desea hacer?: '))
    if choose==1 or choose==2:
        if choose==1:
            print('-------------------------------------------------')
            print('Tipo de habitación:')
            print('1) Sencilla')
            print('2) Doble')
            print('3) Suit')
            print('4) Presidencial')
            print()
            desicion=int(input('Cual desea: '))
            if desicion<1 or desicion>4:
                return print('Error, elegiste la opción incorrecta. ')
            else: 
                for i in range(len(matriz)):
                    if matriz[i][1]==desicion-1:
                        print(f'La habitacion {matriz[i][0]} es del tipo que buscas y está {estadoHabitacion(matriz[i][2])}')
        elif choose==2:
            print('Ingrese el número de habitación que desea: ')
            desicion=int(input(''))
            if desicion<1 or desicion>15:
                 return print('Error, elegiste la opción incorrecta. ')
            else:
                for i in range(len(matriz)):
                    if matriz[i][0]==desicion:
                        print(f'La habitacion {matriz[i][0]}  está {estadoHabitacion(matriz[i][2]) } y es una habitacion {tipoDeHabitacion(matriz[i][1])}')
                        if estadoHabitacion(matriz[i][2])== 'Ocupada':
                            print(f'está ocupada desde el dia {matriz[i][3]} hasta el día{matriz[i][4]}')
    else:
        return print('Tiene que elegir algo válido. ')

def chekIn(matriz):
    print('-------------------------------------------------')
    print('1) Proceder con el checkin')
    print('(Otro número) Mas opciones...')
    print('')
    opcion = int(input('Qué desea?:'))

    while opcion != 1:
            print('1) Proceder con el check in')
            print('2) Buscar una habitación')
            print('3) Ver disponibilidad')
            print('4) Volver al menu')
            opcion = int(input('Qué desea?:'))
            if opcion ==3:
                verDisponibilidad(matriz)
            elif opcion ==2:
                buscarUnaHab(matriz)
            elif opcion == 4:
                return matriz
    numHab =int(input ('Ingrese número de habitación:'))
    if numHab<1 or numHab>len(matriz):
        print(f'Error, no hay más de {len(matriz)} habitaciones por ahora. ')
        return matriz
    elif  matriz[numHab-1][2]!=0:
         print('Esta habitación no está disponible.')
    else:
        matriz[numHab -1][2] = 2

        nombre=input('Ingrese Nombre y Apellido con ese formato: ')
        while validarNombre(nombre)==False:
            nombre=input('Ingrese un formato  de nombre válido: ')

        cedula=input('Ingrese su cedula con el formato V-xxxxxxxx: ')
        while validarCedula(cedula)==False:
            cedula=input('Ingrese un formato  de Cédula válido (V-xxxxxxxx): ')

        fechaIngreso= input('Ingrese la fecha de ingreso con formato dd/mm/yyyy: ')
        while validarFecha(fechaIngreso)==False:
            
            fechaIngreso = input('Ingrese de nuevo la fecha de ingreso con formato dd/mm/yyyy: ')

        fechaSalida= input('Ingrese la fecha de salida con formato dd/mm/yyyy: ')
        while validarFecha(fechaSalida)==False:
            fechaSalida = input('Ingrese de nuevo la fecha de salida con formato dd/mm/yyyy: ')
        
        while validarFechas(fechaIngreso,fechaSalida) == False:
            print('Las fechas no son válidas, sea serio')
            fechaIngreso= input('Ingrese la fecha de ingreso con formato dd/mm/yyyy: ')
            while validarFecha(fechaIngreso)==False:
                fechaIngreso = input('Ingrese la fecha de ingreso con formato dd/mm/yyyy: ')

            fechaSalida= input('Ingrese la fecha de salida con formato dd/mm/yyyy: ')
            while validarFecha(fechaSalida)==False:
                fechaSalida = input('Ingrese la fecha de salida con formato dd/mm/yyyy: ')
            
        if validarFechas(fechaIngreso, fechaSalida)== True:
            matriz[numHab -1][3] = fechaIngreso
            matriz[numHab -1][4] = fechaSalida
            matriz[numHab -1][5] = nombre
            matriz[numHab -1][6] = cedula
            print(f'Checkin exitoso, feliz estadía {nombre}.')
            return matriz
    return matriz
         
def checkOut(matriz):

    print('-------------------------------------------------')    
    print('Confirmar checkout: ')
    print('1) Si')
    print('2) No')
    print('')
    opcion =int(input('Qué desea hacer?: '))
    if opcion ==1:
        print('-------------------------------------------------')
       
        nombre=input('Ingrese el nombre del hospedado con formato Nombre y Apellido: ')
        
        while validarNombre(nombre)== False:
            nombre =input('Ingrese un formato válido Nombre y Apellido: ')
        numHab= int(input('Ingrese el número de habitación: '))
        while numHab>15 or numHab<1:
            numHab= int(input('Ingrese un numero de habitación que exista.'))
        for i in range(len(matriz)):
            if matriz[i][5]== nombre and matriz[i][0]==numHab:
                print('Check out exitoso, gracias por la estadía. ')
                matriz[i][2]=0
                matriz[i][3]=''
                matriz[i][4]=''
                matriz[i][5]=''
                matriz[i][6]=''
                return matriz
        print('Los datos dados no corresponden al de ninguna habitación. ')
        return matriz
    else:
        return matriz
    
def reservacion(matriz):
    print('-------------------------------------------------')
    print('1) Hacer reservación')
    print('2) Cancelar reservación')
    print('3) Volver al menú')
    print('')
    opcionReserva=int(input('Qué desea hacer?: '))
    if opcionReserva==1:
        print('-------------------------------------------------')
        print('1) Proceder con la reserva')
        print('(Otro número) Mas opciones...')
        print('')
        opcion = int(input('Qué desea?:'))
    
        while opcion != 1:
                print('1) Proceder con la reserva')
                print('2) Buscar una habitación')
                print('3) Ver disponibilidad')
                print('4) Volver al menu')
                opcion = int(input('Qué desea?:'))
                if opcion ==3:
                    verDisponibilidad(matriz)
                elif opcion ==2:
                    buscarUnaHab(matriz)
                elif opcion == 4:
                    return matriz
        numHab =int(input ('Ingrese número de habitación:'))
        if numHab<1 or numHab>len(matriz):
                print(f'Error, no hay más de {len(matriz)} habitaciones por ahora. ')
                return matriz
        elif  matriz[numHab-1][2]!=0:
            print('Esta habitación no está disponible.')
        else:
            
    
            nombre=input('Ingrese Nombre y Apellido con ese formato: ')
            while validarNombre(nombre)==False:
                nombre=input('Ingrese un formato  de nombre válido: ')
    
            cedula=input('Ingrese su cedula con el formato V-xxxxxxxx: ')
            while validarCedula(cedula)==False:
                cedula=input('Ingrese un formato  de Cédula válido (V-xxxxxxxx): ')
    
            fechaIngreso= input('Ingrese la fecha de ingreso con formato dd/mm/yyyy: ')
            while validarFecha(fechaIngreso)==False:
                
                fechaIngreso = input('Ingrese de nuevo la fecha de ingreso con formato dd/mm/yyyy: ')
    
            fechaSalida= input('Ingrese la fecha de salida con formato dd/mm/yyyy: ')
            while validarFecha(fechaSalida)==False:
                fechaSalida = input('Ingrese de nuevo la fecha de salida con formato dd/mm/yyyy: ')
            
            while validarFechas(fechaIngreso,fechaSalida) == False:
                print('Las fechas no son válidas, sea serio')
                fechaIngreso= input('Ingrese la fecha de ingreso con formato dd/mm/yyyy: ')
                while validarFecha(fechaIngreso)==False:
                    fechaIngreso = input('Ingrese la fecha de ingreso con formato dd/mm/yyyy: ')
    
                fechaSalida= input('Ingrese la fecha de salida con formato dd/mm/yyyy: ')
                while validarFecha(fechaSalida)==False:
                    fechaSalida = input('Ingrese la fecha de salida con formato dd/mm/yyyy: ')
                
            if validarFechas(fechaIngreso, fechaSalida)== True:
                matriz[numHab -1][2] = 3
                matriz[numHab -1][3] = fechaIngreso
                matriz[numHab -1][4] = fechaSalida
                matriz[numHab -1][5] = nombre
                matriz[numHab -1][6] = cedula
                print(f'Reserva exitosa, le esperamos con gusto {nombre}.')
                return matriz
            else:
                print('Las fechas son inválidas.')
        return matriz
    elif opcionReserva==2:
        print('-------------------------------------------------')    
        print('Cancelar reserva: ')
        print('1) Si')
        print('2) No')
        print('')
        opcion =int(input('Qué desea hacer?: '))
        if opcion ==1:
            print('-------------------------------------------------')

            nombre=input('Ingrese el nombre del hospedado con formato Nombre y Apellido: ')

            while validarNombre(nombre)== False:
                nombre =input('Ingrese un formato válido Nombre y Apellido: ')
            numHab= int(input('Ingrese el número de habitación: '))
            while numHab>15 or numHab<1:
                numHab= int(input('Ingrese un numero de habitación que exista.'))
            for i in range(len(matriz)):
                if matriz[i][5]== nombre and matriz[i][0]==numHab:
                    print('Cancelar reserva exitosa. ')
                    matriz[i][2]=0
                    matriz[i][3]=''
                    matriz[i][4]=''
                    matriz[i][5]=''
                    matriz[i][6]=''
                    return matriz
            print('Los datos dados no corresponden al de ninguna habitación. ')
            return matriz
        else:
            return matriz
    else:
        return matriz



