import os
import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """
        Carga el inventario desde el archivo si existe. Si el archivo no existe, lo crea.
        """
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as f:
                    contenido = f.read()
                    if contenido:
                        self.productos = json.loads(contenido)
        except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
            print(f"Error al cargar el archivo de inventario: {e}")

    def guardar_en_archivo(self):
        """
        Guarda el inventario en el archivo, manejando posibles errores.
        """
        try:
            with open(self.archivo, "w") as f:
                json.dump(self.productos, f, indent=4)
            print("Inventario actualizado correctamente en el archivo.")
        except (PermissionError, IOError) as e:
            print(f"Error al escribir en el archivo de inventario: {e}")

    def agregar_producto(self, nombre, cantidad):
        """
        Agrega un producto al inventario y lo guarda en el archivo.
        """
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' agregado/actualizado exitosamente.")

    def actualizar_producto(self, nombre, cantidad):
        """
        Actualiza la cantidad de un producto en el inventario.
        """
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' actualizado exitosamente.")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario si existe.
        """
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")

    def mostrar_inventario(self):
        """
        Muestra el inventario actual.
        """
        if self.productos:
            print("Inventario actual:")
            for nombre, cantidad in self.productos.items():
                print(f"{nombre}: {cantidad}")
        else:
            print("El inventario está vacío.")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    inventario.agregar_producto("Manzanas", 10)
    inventario.agregar_producto("Plátanos", 5)
    inventario.actualizar_producto("Manzanas", 15)
    inventario.mostrar_inventario()
    inventario.eliminar_producto("Plátanos")
    inventario.mostrar_inventario()
