# Clase base
class Persona:
    def __init__(self, nombre, edad):
        # Atributos encapsulados
        self.__nombre = nombre  # Encapsulación con doble guion bajo
        self.__edad = edad

    # Métodos para acceder a los atributos encapsulados
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:  # Validación simple
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo.")

    # Método común para todas las personas
    def presentarse(self):
        return f"Hola, me llamo {self.__nombre} y tengo {self.__edad} años."

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera  # Atributo específico de la clase derivada

    # Método sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, me llamo {self.get_nombre()}, tengo {self.get_edad()} años y estudio {self.carrera}."

    # Método específico de Estudiante
    def estudiar(self):
        return f"{self.get_nombre()} está estudiando {self.carrera}."

# Clase adicional para demostrar más polimorfismo
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Método sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy el profesor {self.get_nombre()}, tengo {self.get_edad()} años y enseño {self.materia}."

    # Método específico de Profesor
    def ensenar(self):
        return f"El profesor {self.get_nombre()} está enseñando {self.materia}."

# Instancias y demostración
if __name__ == "__main__":
    # Creación de una persona
    persona = Persona("Luis", 40)
    print(persona.presentarse())

    # Creación de un estudiante
    estudiante = Estudiante("María", 20, "Ingeniería en Sistemas")
    print(estudiante.presentarse())
    print(estudiante.estudiar())

    # Creación de un profesor
    profesor = Profesor("Carlos", 45, "Matemáticas")
    print(profesor.presentarse())
    print(profesor.ensenar())

    # Uso de encapsulación para modificar atributos
    estudiante.set_edad(21)
    print(estudiante.presentarse())

    # Intento de poner una edad negativa
    profesor.set_edad(-5)  # Esto no cambiará el valor debido a la validación
