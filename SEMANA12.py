class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id  # ID único
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {[str(libro) for libro in self.libros_prestados]}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para IDs únicos de usuarios
        self.registro_usuarios = {}  # Diccionario para almacenar usuarios por ID

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            self.registro_usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.registro_usuarios[user_id]
            self.usuarios.remove(user_id)
            print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("El usuario no existe.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.registro_usuarios[user_id]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]  # Remover de la colección de libros disponibles
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.registro_usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Devolver a la colección de libros disponibles
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, filtro):
        resultados = [libro for libro in self.libros.values() if
                      filtro.lower() in libro.info[0].lower() or filtro.lower() in libro.info[
                          1].lower() or filtro.lower() in libro.categoria.lower()]
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.registro_usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# --- Pruebas del sistema ---

biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "0987654321")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("María López", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("U001", "1234567890")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")

# Devolver libro
biblioteca.devolver_libro("U001", "1234567890")

# Buscar libros
biblioteca.buscar_libro("Ficción")
