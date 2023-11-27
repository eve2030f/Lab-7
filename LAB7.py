#EVELYN FENG WU B82870
# LABORATORIO 7


import psutil
import sys

def imprimir(pid):
    try:
        proceso = psutil.Process(pid)
        nombre = proceso.name()
        pid = proceso.pid
        ppid = proceso.ppid()
        usuario = proceso.username()
        uso_cpu = proceso.cpu_percent()
        consumo_memoria = proceso.memory_info().rss
        estado = proceso.status()
        path_ejecutable = proceso.exe()

        return {
            'Nombre del proceso': nombre,
            'ID del proceso': pid,
            'Parent process ID': ppid,
            'Usuario propietario': usuario,
            'Porcentaje de uso de CPU': uso_cpu,
            'Consumo de memoria': consumo_memoria,
            'Estado': estado,
            'Path del ejecutable': path_ejecutable
        }
    except psutil.NoSuchProcess as e:
        return f"Error: No se encontró el proceso con ID {pid}"

if __name__ == "__main__":
    pid = input("Ingrese el ID del proceso: ")
    if len(sys.argv) != 2:
        print("Uso: python script.py <PID>")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: El PID debe ser un número entero.")
        sys.exit(1)

    informacion = imprimir(pid)

    if isinstance(informacion, dict):
        print("\nInformación del proceso:")
        for key, value in informacion.items():
            print(f"{key}: {value}")
    else:
        print(informacion)