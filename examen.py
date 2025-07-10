#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

#stock = {modelo: [precio, stock], ...]
stock = {
'8475HD': [387990,10], 
'2175HD': [327990,4], 
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], 
'123FHD': [290890,32], 
'342FHD': [444990,7],
'GF75HD': [749990,2], 
'UWU131HD': [349990,1], 
'FS1230HD': [249990,0]
}

def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opc = int(input("ingrese su opcion: "))
        if opc == 1:
            marca = input("ingrese la marca a buscar: ")
            buscar_marca(marca)
        elif opc == 2:
            buscar_precio()
        elif opc == 3:
                actualizar_precio()
        elif opc == 4:
            break
        else:
            print("debe ingresar una opcion valida")


def buscar_marca(marca):
    try:
        marca = marca.lower()
        total = 0
        for codigo, datos in productos.items():
            if datos[0].lower() == marca:
                total += stock[codigo][1]
    except ValueError:
        print("error")
    print(f"hay {total} en stock de: {marca}")

def buscar_precio():
    try:
        precio1 = int(input("ingrese el precio minimo: "))
        precio2 = int(input("ingrese el precio maximo: "))
        if precio1 < 0 > precio2:
            print("ingrese un valor")
        else:
            for datos, codigo in stock.items():
                precio = stock[datos][0]
                print(f"{precio}")
                for codigo, datos in productos.items():
                    if precio >= precio1 and precio <= precio2:
                        print([productos][1][codigo])
    except ValueError:
        print("ingrese un valor numerico")

def actualizar_precio():
    while True:
        try:
            for valor, datos in stock.items():
                act = input("ingrese el modelo a actualizar: ")
                act = act.lower()
                if valor.lower() == act:
                    precio = int(input("ingrese el nuevo valor: "))
                    if precio > 0:
                        datos[0] = precio
                        print("actualizacion exitosa")
                        alt = int(input("desea actualizar otro valor? (1:si / 2:no): "))
                        if alt == 1:
                            break
                        else:
                            return
                    else:
                        print("ingresa un valor: ")
                else:
                    print("debe ingresar un modelo existente")
                    alt = int(input("desea actualizar otro valor? (1:si / 2:no): "))
                    if alt == 1:
                        break
                    else:
                        return
        except ValueError:
            print("ingrese un codigo existente")

menu()