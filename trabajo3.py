import numpy as np
import fun_trabajo3 as fn
op = 0
compra = 0
nombre = ''
apellido = ''
rut = ''
telefono = ''
banco = ''
asiento = ''
precio = 0
normal = 78900
vip = 240000
preciodescuento = 0
datosUsuario = ''
opm = 0
masiento = ''
mrut = ''
ticket = ''
asientos_disponibles = np.array([
    ['1', '2', '3', '4', '5', '6'],
    ['7', '8', '9', '10', '11', '12'],
    ['13', '14', '15', '16', '17', '18'],
    ['19', '20', '21', '22', '23', '24'],
    ['25', '26', '27', '28', '29', '30'],
    ['31', '32', '33', '34', '35', '36'],
    ['37', '38', '39', '40', '41', '42']])
print('bienvenido a Vuelos-Duoc')
while op != 5:
    try:
        print('que desea\n--------------')
        print('1. ver asientos disponibles')
        print('2. comprar asientos')
        print('3. anular vuelo')
        print('4. modificar datos de pasajero')
        print('5. salir')
        op = int(input(': '))
        if op == 1:
            print(asientos_disponibles)
        if op == 2:
            print('Asiento normal (1-30) $78.900\nAsiento vip(31-42) $240.000.')
            nombre, apellido, rut, telefono, banco = (fn.datos_usuario(
                nombre, apellido, rut, telefono, banco))
            asiento = str(input('que asiento\n: '))
            if asiento in asientos_disponibles:
                asientos_disponibles[np.where(
                    asientos_disponibles == asiento)] = 'x'
        if op == 3:
            print('desea anular el vuelo')
            respuesta = input('Desea deshacer el cambio? (si/no): ')
            if respuesta.lower() == 'si':
                asientos_disponibles[np.where(
                    asientos_disponibles == 'x')] = asiento
                print('asiento restaurado:')
                print(asientos_disponibles)
            else:
                print('Cambio confirmado.')
        if op == 4:
            masiento, mrut = (fn.modificar_datos_pasajero(masiento, mrut))
            if mrut == rut and masiento == asiento:
                print('Son iguales')
                opm = 0
                while opm != 3:
                    print(
                        'Qué dato desea modificar?\n1. Nombre\n2. Teléfono\n3. Salir')
                    opm = int(input(': '))
                    if opm == 1:
                        print('Ingrese un nuevo nombre:')
                        nombre = str(input(': '))
                    elif opm == 2:
                        print('Ingrese un nuevo teléfono:')
                        telefono = str(input(': '))
                    elif opm == 3:
                        break
            else:
                print('Los datos no coinciden')
    except ValueError:
        print('tiene que ingresar un numero')
if asiento <= '30':
    precio = 78900
else:
    precio = 240000
if banco == 'bancoDuoc':
    preciodescuento = (precio * 0.15)

preciototal = precio - preciodescuento
fn.imprimir_ticket(nombre, apellido, rut, telefono,
                   banco, asiento, preciototal)
