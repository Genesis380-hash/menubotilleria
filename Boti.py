import os
import pyfiglet
from datetime import datetime

def inicio_portada():
    print(pyfiglet.figlet_format("Menu Botilleria",font="slant",justify="centre"))
    print("\n\n")
    print("                                  Autores: Genesis Adasme")
    print("                                           Eduardo Salgado")
    print("\n\n")
    os.system("pause")

def buscar_cod(cod):
    for a in productos:
        if a[0] == cod:
            return a
    return -1

def buscar_indice_cod(cod):
    i = 0
    for a in productos:
        if a[0] == cod:
            return i
        i += 1
    return -1

def get_folio():
    if len(ventas) != 0:
        elemento = len(ventas)-1
        return int(ventas[elemento][0])
    else:
        return -1

def cargar_productos():
    with open("productos.txt", 'r') as file:
        for producto in file:
            producto = producto.strip()
            datos = producto.split(',')
            productos.append(datos)

def cargar_ventas():
    with open("ventas.txt", "r") as file:
        for venta in file:
            venta = venta.strip()
            datos = venta.split(',')
            ventas.append(datos)

def respaldar_datos():
    with open("ventas.txt", "w") as file:
        for mis_ventas in ventas:
            mis_ventas=mis_ventas.strip()
            datos=mis_ventas.split()

            file.write(datos + '\n')
        print(" Datos respaldados correctamente ")

folio = 10000
fecha = datetime.now().strftime('%d-%m-%Y')
productos = []
ventas = []

inicio_portada()

op = 0
while op != 5:
    os.system("cls")
    print("\t \t \t \t \t \t \t Fecha: ", fecha)
    print("\t \t \t \t \t \t \t Version v002")
    print(""" 
                                ╔══════════════════════╗
                                ║   SISTEMA DE VENTAS  ║
                                ╠══════════════════════╣
                                ║  1. Vender producto  ║ 
                                ║  2. Reportes         ║
                                ║  3. Mantenedores     ║
                                ║  4. Administracion   ║
                                ║  5. Salir            ║
                                ╚══════════════════════╝
    """)
    op = int(input("Ingrese una opción [1-5]: "))

    if 1 <= op <= 5:
        match op:
            case 1:
                while True:
                    os.system("cls")
                    cod = input("Ingrese el código del producto: ")
                    producto = buscar_cod(cod)

                    if producto == -1:
                        print("Código de producto no encontrado.")
                        os.system("pause")
                        continue

                    print("            Detalles del Producto:")
                    print("\n--------------------------------------------------\n")
                    print("Producto:", producto[1])
                    print("Marca:", producto[2])
                    print("Unidad de medida:", producto[3])
                    print("Stock disponible:", producto[4])
                    print("Precio: $", producto[5])
                    print("\n--------------------------------------------------\n")

                    cantidad = int(input("¿Cuántas unidades desea comprar? "))
                    print("\n--------------------------------------------------\n")
                    
                    if cantidad > int(producto[4]):
                        print("No hay suficiente stock para la cantidad solicitada.")
                        print("\n--------------------------------------------------\n")
                        continue

                    total_pagar = cantidad * int(producto[5])
                    print("Total a pagar: $", total_pagar)
                    print("\n--------------------------------------------------\n")

                    confirmar = input("¿Desea confirmar la compra? (si/no): ").lower()
                    print("\n--------------------------------------------------\n")
                    if confirmar == 'si':
                        producto[4] = str(int(producto[4]) - cantidad)
                        fecha_venta = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        ventas.append([folio, datetime.now().strftime('%d-%m-%Y'), producto[0], cantidad, total_pagar])
                        folio += 1

                        print("          Venta realizada exitosamente.")
                        print(cantidad, producto[1], producto[2], "$", total_pagar)
                        print(fecha_venta)
                        print("\n--------------------------------------------------\n")

                    else:
                        continuar = input("¿Desea continuar con otra compra? (si/no): ").lower()
                        print("\n--------------------------------------------------\n")
                        if continuar == 'no':
                            break

                    comprar_otra = input("¿Desea comprar otro producto? (si/no): ").lower()
                    print("\n--------------------------------------------------\n")
                    if comprar_otra == 'no':
                        break

            case 2:
                op = 0
                while op != 4:
                    os.system("cls")
                    print("""
                                ╔═══════════════════════════════════╗
                                ║             REPORTES              ║
                                ╠═══════════════════════════════════╣
                                ║  1. General de ventas             ║ 
                                ║  2. Ventas por fecha específica   ║
                                ║  3. Ventas por rango de fecha     ║
                                ║  4. Salir al menu principal       ║
                                ╚═══════════════════════════════════╝
                    """)
                    op = int(input("Ingrese una opción [1-4]: "))

                    if 1 <= op <= 4:
                        match op:
                            case 1:
                                os.system("cls")
                                for venta in ventas:
                                    print(venta[0], " ", venta[1], " ", venta[2], " ", venta[3], " ", venta[4])
                                os.system("pause")
                            case 2:
                                os.system("cls")
                                fecha_inicial = input("Ingrese fecha de la compra (dd-mm-aaaa): ")
                                print("\n--------------------------------------------------\n")
                                total = 0
                                for venta in ventas:
                                    if venta[1] == fecha_inicial:
                                        print(venta)
                                        total += float(venta[4])
                                print("Total = $", total)
                                print("\n--------------------------------------------------\n")
                                os.system("pause")
                            case 3:
                                os.system("cls")
                                fecha_inicial = input("Ingrese la primera fecha (dd-mm-aaaa): ")
                                fecha_final = input("Ingrese la segunda fecha (dd-mm-aaaa): ")
                                print("\n--------------------------------------------------\n")
                                total = 0
                                for venta in ventas:
                                    if fecha_inicial <= venta[1] <= fecha_final:
                                        print(venta)
                                        total += float(venta[4])
                                print("Total= $", total)
                                print("\n--------------------------------------------------\n")
                                os.system("pause")
                            case 4:
                                os.system("cls")
                                print("Saliendo al menú principal...")
                                os.system("pause")
                                break
                    else:
                        print("Opción no válida. Intente de nuevo.")
                        print("\n--------------------------------------------------\n")
                        os.system("pause")
            case 3:
                opc = 0
                while opc != 6:
                    os.system("cls")
                    print("""
                                ╔═══════════════════════════════════╗ 
                                ║           MANTENEDORES            ║
                                ╠═══════════════════════════════════╣
                                ║   1. Agregar                      ║
                                ║   2. Buscar                       ║
                                ║   3. Eliminar                     ║
                                ║   4. Modificar                    ║
                                ║   5. Listar                       ║
                                ║   6. Salir al menu principal      ║
                                ╚═══════════════════════════════════╝
                    """)
                    opc = int(input("Ingrese una opción [1-6]: "))

                    if 1 <= opc <= 6:
                        match opc:
                            case 1:
                                os.system("cls")
                                print("Agregar datos a la lista de productos")
                                cod = input("Ingrese el código del producto: ")
                                nombre = input("Ingrese el nombre del producto: ")
                                marca = input("Ingrese la marca del producto: ")
                                uni_medida = input("Ingrese la unidad de medida del producto: ")
                                stock = int(input("Ingrese el stock del producto: "))
                                valor = int(input("Ingrese el valor del producto: "))
                                productos.append([cod, nombre, marca, uni_medida, str(stock), str(valor)])
                                print("Producto agregado exitosamente")
                                os.system("pause")

                            case 2:
                                os.system("cls")
                                cod = input("Ingrese código para buscar: ")
                                producto = buscar_cod(cod)
                                if producto != -1:
                                    print(producto)
                                else:
                                    print("Error. Producto no encontrado.")
                                os.system("pause")

                            case 3:
                                os.system("cls")
                                cod = input("Ingrese código del producto a eliminar: ")
                                producto = buscar_cod(cod)
                                if producto != -1:
                                    productos.remove(producto)
                                    print("Producto eliminado exitosamente.")
                                    print(productos)
                                else:
                                    print("Error. Producto no encontrado.")
                                os.system("pause")

                            case 4:
                                os.system("cls")
                                print("Modificar")
                                cod = input("Ingrese codigo a buscar (cod): ")
                                nombre = input("Ingrese el nuevo nombre de producto: ")
                                marca = input("Ingrese la nueva marca de producto: ")
                                uni_medida = input("Ingrese la nueva unidad de medida del producto: ")
                                stock = input("Ingrese el nuevo stock: ")
                                valor = input("Ingrese el nuevo valor: ")

                                producto = buscar_cod(cod)

                                if producto != -1:
                                    producto[1] = nombre
                                    producto[2] = marca
                                    producto[3] = uni_medida
                                    producto[4] = stock
                                    producto[5] = valor
                                    print("\n Listo! datos modificados")
                                    print(productos)
                                else:
                                    print("cod no existe...")
                                os.system("pause")

                            case 5:
                                os.system("cls")
                                print("Listar los productos")
                                for e in productos:
                                    print(e[0], " ", e[1], " ", e[2], " ", e[3], " ", e[4], " ", e[5])
                                os.system("pause")

                            case 6:
                                os.system("cls")
                                print("Saliendo al menú principal...")
                                os.system("pause")
                                break

            case 4:
                opc = 0
                while opc != 3:
                    os.system("cls")
                    print("""     
                                    ╔═══════════════════════════════════╗ 
                                    ║           ADMINISTRACION          ║
                                    ╠═══════════════════════════════════╣
                                    ║   1. Cargar Datos                 ║
                                    ║   2. Respaldar Datos              ║
                                    ║   3. Salir al menu principal      ║
                                    ╚═══════════════════════════════════╝    
                        """)
                    opc = int(input("Ingrese una opción [1-3]: "))

                    if 1 <= opc <= 3:
                        match opc:
                            case 1:
                                os.system("cls")
                                continuar = input("Desea cargar datos? (si/no): ").lower()
                                if continuar == "si":
                                    cargar_productos()
                                os.system("pause")
                            case 2:
                                os.system("cls")
                                continuar = input("Desea respaldar datos? (si/no): ").lower()
                                if continuar == "si":
                                    respaldar_datos()
                                os.system("pause")
                            case 3:
                                os.system("cls")
                                print("Saliendo al menú principal...")
                                os.system("pause")
                                break
                    else:
                        print("Opción no válida. Intente de nuevo.")
                        os.system("pause")

print("Fin del menú.")
