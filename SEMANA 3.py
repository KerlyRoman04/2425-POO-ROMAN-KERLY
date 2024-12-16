# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas


# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# Función principal que coordina las otras funciones
def main():
    # Ingresar las temperaturas diarias
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio semanal
    promedio = calcular_promedio(temperaturas)

    # Mostrar el resultado
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


# Llamada a la función principal
if __name__ == "__main__":
    main()


# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []  # Lista para almacenar las temperaturas de la semana
    for i in range(7):  # Un ciclo que se repite 7 veces para los 7 días de la semana
        # Solicitar al usuario la temperatura para cada día de la semana
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)  # Agregar la temperatura a la lista
    return temperaturas  # Retornar la lista con todas las temperaturas ingresadas


# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)  # Sumar todas las temperaturas de la lista
    promedio = suma / len(temperaturas)  # Calcular el promedio dividiendo la suma entre la cantidad de días
    return promedio  # Retornar el promedio calculado


# Función principal que coordina las otras funciones
def main():
    # Ingresar las temperaturas diarias utilizando la función definida previamente
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio semanal de las temperaturas
    promedio = calcular_promedio(temperaturas)

    # Mostrar el resultado del promedio semanal de las temperaturas
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()  # Llamar a la función main para iniciar el programa
