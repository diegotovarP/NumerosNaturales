class CalculadoraMCD:
    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

# Instanciar la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los números para calcular el MCD
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular el MCD utilizando el método de la instancia de la clase
mcd = calculadora.calcular_mcd(num1, num2)
print("El máximo común divisor de", num1, "y", num2, "es:", mcd)

