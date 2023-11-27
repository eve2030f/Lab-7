#EVELYN FENG WU B82870
# LABORATORIO 7

import os
import sys
import time
import psutil
import matplotlib.pyplot as plt

def monitorear_proceso(ejecutable, intervalo, duracion):
    # Iniciar el proceso
    proceso = subprocess.Popen(ejecutable, shell=True)

    # Inicializar listas para almacenar los datos de monitoreo
    tiempos = []
    consumo_cpu = []
    consumo_memoria = []

    try:
        tiempo_inicio = time.time()

        while time.time() - tiempo_inicio < duracion:
            # Obtener información de consumo de recursos
            info_proceso = proceso.as_dict(attrs=['cpu_percent', 'memory_info'])
            tiempo_actual = time.time() - tiempo_inicio

            # Registrar datos
            tiempos.append(tiempo_actual)
            consumo_cpu.append(info_proceso['cpu_percent'])
            consumo_memoria.append(info_proceso['memory_info'].rss)

            # Esperar el intervalo especificado antes de la siguiente lectura
            time.sleep(intervalo)

    except KeyboardInterrupt:
        print("\nMonitoreo detenido manualmente.")

    finally:
        # Finalizar el proceso
        proceso.terminate()
        proceso.wait()

        # Crear el archivo de log
        with open('log_consumo.txt', 'w') as log_file:
            log_file.write("Tiempo\tConsumo_CPU (%)\tConsumo_Memoria (bytes)\n")
            for i in range(len(tiempos)):
                log_file.write(f"{tiempos[i]:.2f}\t{consumo_cpu[i]:.2f}\t{consumo_memoria[i]}\n")

        # Graficar los datos
        plt.plot(tiempos, consumo_cpu, label='Consumo de CPU (%)')
        plt.plot(tiempos, consumo_memoria, label='Consumo de Memoria (bytes)')
        plt.xlabel('Tiempo (segundos)')
        plt.ylabel('Consumo')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    ejecutable = input("Ingrese la ruta al ejecutable: ")

    try:
        intervalo = float(input("Ingrese el intervalo de monitoreo en segundos: "))
        duracion = float(input("Ingrese la duración total del monitoreo en segundos: "))
    except ValueError:
        print("Error: Intervalo y duración deben ser valores numéricos.")
        sys.exit(1)

    monitorear_proceso(ejecutable, intervalo, duracion)