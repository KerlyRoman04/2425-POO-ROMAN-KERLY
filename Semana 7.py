class Archivo:
    def __init__(self, nombre):
        """Constructor que inicializa el nombre del archivo y abre el archivo en modo escritura."""
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo '{self.nombre}' creado y abierto para escritura.")

    def escribir(self, texto):
        """Método para escribir texto en el archivo."""
        self.archivo.write(texto + '\n')
        print(f"Texto escrito en '{self.nombre}'.")

    def __del__(self):
        """Destructor que cierra el archivo si está abierto."""
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado correctamente.")

# Clase para gestionar una colección de elementos
class Coleccion:
    def __init__(self, nombre):
        """Constructor que inicializa el nombre y la lista de elementos."""
        self.nombre = nombre
        self.elementos = []
        print(f"Colección '{self.nombre}' creada.")

    def agregar(self, elemento):
        """Método para agregar un elemento a la colección."""
        self.elementos.append(elemento)
        print(f"Elemento '{elemento}' agregado a la colección '{self.nombre}'.")

    def mostrar(self):
        """Método para mostrar los elementos de la colección."""
        print(f"Elementos en '{self.nombre}': {', '.join(self.elementos)}")

    def __del__(self):
        """Destructor que muestra un mensaje al destruir la colección."""
        print(f"Colección '{self.nombre}' eliminada de la memoria.")

# Demostración de uso
if __name__ == "__main__":
    # Uso de la clase Archivo
    archivo = Archivo("demo.txt")
    archivo.escribir("Este es un ejemplo de escritura en un archivo.")
    archivo.escribir("Los destructores se encargan de cerrar el archivo automáticamente.")

    # Uso de la clase Coleccion
    coleccion = Coleccion("Mis Elementos")
    coleccion.agregar("Elemento 1")
    coleccion.agregar("Elemento 2")
    coleccion.mostrar()

    # Fin del programa
    print("Fin del programa. Los destructores se activarán automáticamente si es necesario.")