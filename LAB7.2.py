#EVELYN FENG WU B82870
# LABORATORIO 7


import os
import sys
import time
import subprocess


def monitorear_proceso():
    nombre_proceso = input("Ingrese el nombre del proceso: ")
    comando_ejecucion = input("Ingrese el comando para ejecutar el proceso: ")

    while True:
        # Verificar si el proceso está en ejecución
        procesos = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if
                    nombre_proceso.lower() in p.info['name'].lower()]

        if not procesos:
            print(f"El proceso {nombre_proceso} no está en ejecución. Iniciando...")
            subprocess.Popen(comando_ejecucion, shell=True)

        time.sleep(60)  # Esperar 60 segundos antes de revisar de nuevo


if __name__ == "__main__":
    monitorear_proceso()