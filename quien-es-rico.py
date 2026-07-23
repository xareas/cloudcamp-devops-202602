import sys

# sys.argv[0] es el nombre del script, por lo que necesitamos 3 elementos en total
if len(sys.argv) != 3:
    print("Error: Debes proporcionar exactamente dos argumentos.")
    print("Uso correcto: python quien-es-rico.py <nombre> <edad>")
    sys.exit(1) # Salimos del script con código de error

nombre = sys.argv[1]
edad = sys.argv[2]

print(f"Hola {nombre} tu tienes {edad}, y eres rico")
