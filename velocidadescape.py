import math

# Definir la constante de gravitación universal (m^3/kg*s^2)
G = 6.674 * (10 ** -11)

# Datos de los astros
astros = [
    {"nombre": "Earth", "masa": 5.97e24, "radio": 6370000},
    {"nombre": "Moon", "masa": 7.3e22, "radio": 1737000},
    {"nombre": "Mars", "masa": 6.4e23, "radio": 3400000},
    {"nombre": "Jupiter", "masa": 1.9e27, "radio": 69900000},
    {"nombre": "Sun", "masa": 1.99e30, "radio": 696000000},
    {"nombre": "White Dwarf (Sirius B)", "masa": 2.0e30, "radio": 6000000},
    {"nombre": "Neutron Star (Crab Pulsar)", "masa": 2.8e30, "radio": 10000},
    {"nombre": "Black Hole (Cygnus X-1)", "masa": 3.0e31, "radio": 135000}
]

# Función para calcular la velocidad de escape
def calcular_velocidad_escape(masa, radio):
    return math.sqrt(2 * G * masa / radio) / 1000  # Convertir a km/s

# Imprimir resultados
print("Velocidades de escape:")
for astro in astros:
    velocidad_escape = calcular_velocidad_escape(astro["masa"], astro["radio"])
    print(f"{astro['nombre']}: {round(velocidad_escape, 2)} km/s")
