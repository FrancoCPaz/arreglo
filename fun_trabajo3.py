import numpy as np


def datos_usuario(nombre, apellido, rut, telefono, banco):
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    rut = input('ingrese su rut:')
    telefono = input('ingrese su telefono: ')
    banco = input('ustes es del bancoDuoc ? (si/no) :')
    if banco.lower() == 'si':
        banco = 'bancoDuoc'
    else:
        print('usted es de otro banco')
    return nombre.upper(), apellido.upper(), rut, telefono, banco


def modificar_datos_pasajero(masiento, mrut):
    masiento = str(input('Ingrese el número del asiento del pasajero: '))
    mrut = str(input('Ingrese el rut del pasajero: '))
    return masiento, mrut


def imprimir_ticket(nombre, apellido, rut, telefono, banco, asiento, preciototal):
    print('---------------\nSu ticket\n---------------')
    print(f'Boleto a nombre de: {nombre} {apellido}')
    print(f'RUT: {rut}')
    print(f'Teléfono: {telefono}')
    print(f'Banco: {banco}')
    print(f'Asiento N°: {asiento}')
    print(f'Costo: ${preciototal}\n---------------')
