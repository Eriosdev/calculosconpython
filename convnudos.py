def nudos_a_kmh(nudos):
    # Factor de conversión de nudos a km/h
    factor_conversion = 1.852
    # Conversión de nudos a km/h
    kmh = nudos * factor_conversion
    return kmh

def main():
    # Solicitar al usuario que ingrese la velocidad en nudos
    nudos = float(input("Ingresa la velocidad en nudos: "))

    # Convertir nudos a km/h utilizando la función definida anteriormente
    kmh = nudos_a_kmh(nudos)

    # Mostrar el resultado
    print(f"{nudos} nudos equivalen a {kmh} kilómetros por hora.")

if __name__ == "__main__":
    main()
