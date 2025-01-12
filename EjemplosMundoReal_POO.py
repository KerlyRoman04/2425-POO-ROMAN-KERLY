# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        """Inicializa un producto con nombre y precio"""
        self.nombre = nombre
        self.precio = precio

    def obtener_info(self):
        """Devuelve la información básica del producto"""
        return f"Producto: {self.nombre}, Precio: ${self.precio}"

# Clase derivada Libro (herencia de Producto)
class Libro(Producto):
    def __init__(self, nombre, precio, autor, isbn):
        """Inicializa un libro con autor y ISBN adicionales"""
        super().__init__(nombre, precio)  # Llamada al constructor de Producto
        self.autor = autor
        self.isbn = isbn

    def obtener_info(self):
        """Devuelve la información del libro, sobrescribiendo el método de Producto"""
        return f"Libro: {self.nombre}, Autor: {self.autor}, ISBN: {self.isbn}, Precio: ${self.precio}"

# Clase derivada Ropa (herencia de Producto)
class Ropa(Producto):
    def __init__(self, nombre, precio, talla, material):
        """Inicializa una prenda de ropa con talla y material adicionales"""
        super().__init__(nombre, precio)  # Llamada al constructor de Producto
        self.talla = talla
        self.material = material

    def obtener_info(self):
        """Devuelve la información de la ropa, sobrescribiendo el método de Producto"""
        return f"Ropa: {self.nombre}, Talla: {self.talla}, Material: {self.material}, Precio: ${self.precio}"

# Clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        """Inicializa un cliente con nombre y correo electrónico"""
        self.nombre = nombre
        self.email = email
        self.reservas = []  # Lista de productos reservados por el cliente

    def hacer_reserva(self, producto):
        """Añade un producto a las reservas del cliente"""
        self.reservas.append(producto)
        print(f"{self.nombre} ha reservado el producto: {producto.nombre}")

    def ver_reservas(self):
        """Muestra los productos reservados por el cliente"""
        if self.reservas:
            print(f"Productos reservados por {self.nombre}:")
            for producto in self.reservas:
                print(f"- {producto.obtener_info()}")
        else:
            print(f"{self.nombre} no tiene reservas.")

# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        """Inicializa una tienda con un nombre y una lista de productos disponibles"""
        self.nombre = nombre
        self.productos = []  # Lista de productos disponibles en la tienda

    def agregar_producto(self, producto):
        """Añade un producto a la tienda"""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra todos los productos disponibles en la tienda"""
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(f"- {producto.obtener_info()}")

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear productos
    libro1 = Libro("El Quijote", 25.99, "Miguel de Cervantes", "978-3-16-148410-0")
    libro2 = Libro("1984", 19.99, "George Orwell", "978-0-452-28423-4")
    ropa1 = Ropa("Camiseta", 15.49, "M", "Algodón")
    ropa2 = Ropa("Pantalón", 29.99, "L", "Denim")

    # Crear una tienda y agregar productos
    tienda = Tienda("Tienda Online")
    tienda.agregar_producto(libro1)
    tienda.agregar_producto(libro2)
    tienda.agregar_producto(ropa1)
    tienda.agregar_producto(ropa2)

    # Crear un cliente
    cliente = Cliente("Juan Pérez", "juanperez@email.com")

    # Mostrar productos disponibles en la tienda
    tienda.mostrar_productos()

    # El cliente hace reservas
    cliente.hacer_reserva(libro1)
    cliente.hacer_reserva(ropa2)

    # Ver las reservas del cliente
    cliente.ver_reservas()
