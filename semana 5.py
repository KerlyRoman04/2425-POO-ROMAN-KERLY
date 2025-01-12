# Este programa calcula el área de un círculo basado en el radio proporcionado
# y convierte una temperatura de grados Celsius a Fahrenheit.
# Utiliza varios tipos de datos: integer, float, string, boolean.

import math  # Importamos el módulo math para operaciones matemáticas


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    El área se calcula con la fórmula: área = π * radio^2
    """
    area = math.pi * radio ** 2  # Fórmula para calcular el área del círculo
    return area


# Función para convertir grados Celsius a Fahrenheit
def convertir_celsius_a_fahrenheit(celsius):
    """
    Convierte la temperatura de grados Celsius a Fahrenheit.
    La fórmula es: Fahrenheit = (Celsius * 9/5) + 32
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Función principal del programa
def main():
    # Solicitar al usuario el radio del círculo
    radio = float(input("Introduce el radio del círculo en metros: "))  # float para permitir decimales

    # Llamar a la función para calcular el área
    area = calcular_area_circulo(radio)

    # Mostrar el resultado
    print(f"El área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados.")

    # Solicitar al usuario la temperatura en Celsius
    celsius = float(input("Introduce la temperatura en grados Celsius: "))

    # Llamar a la función para convertir la temperatura
    fahrenheit = convertir_celsius_a_fahrenheit(celsius)

    # Mostrar el resultado de la conversión
    print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

    # Preguntar al usuario si desea realizar otra operación
    desea_continuar = input("¿Deseas realizar otra operación? (sí/no): ").lower()  # string con sí/no

    if desea_continuar == "sí":
        main()  # Llamar nuevamente a la función principal si el usuario desea continuar
    else:
        print("Gracias por usar el programa. ¡Hasta pronto!")  # Mensaje de despedida


# Ejecutar el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal para iniciar el programa
