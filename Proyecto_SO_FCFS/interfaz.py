import tkinter as tk
import threading

from proceso import Proceso
from simulador import simulacion_fcfs
from utils import escribir_log


procesos = []


def iniciar_interfaz():

    ventana = tk.Tk()

    ventana.title(
        "Simulador FCFS"
    )

    ventana.geometry("850x700")

    ventana.config(bg="#1e1e1e")

    # -----------------------------
    # Funciones internas
    # -----------------------------

    def agregar_proceso():

        nombre = entry_nombre.get()

        if (
            nombre == ""
            or entry_cpu.get() == ""
            or entry_llegada.get() == ""
        ):

            escribir_log(
                area_log,
                "⚠️ Completa todos los campos"
            )

            return

        try:

            tiempo_cpu = int(entry_cpu.get())

            llegada = int(entry_llegada.get())

        except:

            escribir_log(
                area_log,
                "⚠️ Valores inválidos"
            )

            return

        nuevo_proceso = Proceso(
            nombre,
            tiempo_cpu,
            llegada
        )

        procesos.append(nuevo_proceso)

        lista_procesos.insert(
            tk.END,
            f"{nombre} | CPU: {tiempo_cpu} "
            f"| Llegada: {llegada}"
        )

        escribir_log(
            area_log,
            f"✅ {nombre} agregado"
        )

        entry_nombre.delete(0, tk.END)
        entry_cpu.delete(0, tk.END)
        entry_llegada.delete(0, tk.END)

    def iniciar_simulacion():

        hilo = threading.Thread(
            target=simulacion_fcfs,
            args=(
                procesos,
                area_log,
                label_cpu_actual
            )
        )

        hilo.start()

    # -----------------------------
    # Título
    # -----------------------------

    titulo = tk.Label(
        ventana,
        text="SIMULADOR DE CPU - FCFS",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#1e1e1e"
    )

    titulo.pack(pady=15)

    # -----------------------------
    # CPU actual
    # -----------------------------

    label_cpu_actual = tk.Label(
        ventana,
        text="CPU ACTUAL: LIBRE",
        font=("Arial", 14, "bold"),
        fg="#00ff00",
        bg="#1e1e1e"
    )

    label_cpu_actual.pack(pady=10)

    # -----------------------------
    # Frame inputs
    # -----------------------------

    frame_inputs = tk.Frame(
        ventana,
        bg="#1e1e1e"
    )

    frame_inputs.pack(pady=10)

    # Nombre
    tk.Label(
        frame_inputs,
        text="Nombre",
        fg="white",
        bg="#1e1e1e"
    ).grid(row=0, column=0, padx=10)

    entry_nombre = tk.Entry(frame_inputs)

    entry_nombre.grid(row=0, column=1)

    # CPU
    tk.Label(
        frame_inputs,
        text="Tiempo CPU",
        fg="white",
        bg="#1e1e1e"
    ).grid(row=1, column=0, padx=10)

    entry_cpu = tk.Entry(frame_inputs)

    entry_cpu.grid(row=1, column=1)

    # Llegada
    tk.Label(
        frame_inputs,
        text="Llegada",
        fg="white",
        bg="#1e1e1e"
    ).grid(row=2, column=0, padx=10)

    entry_llegada = tk.Entry(frame_inputs)

    entry_llegada.grid(row=2, column=1)

    # Botón agregar
    btn_agregar = tk.Button(
        frame_inputs,
        text="Agregar Proceso",
        command=agregar_proceso,
        bg="#3498db",
        fg="white"
    )

    btn_agregar.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10
    )

    # Lista
    lista_procesos = tk.Listbox(
        ventana,
        width=70,
        height=8
    )

    lista_procesos.pack(pady=10)

    # Botón iniciar
    btn_iniciar = tk.Button(
        ventana,
        text="Iniciar Simulación",
        command=iniciar_simulacion,
        bg="green",
        fg="white"
    )

    btn_iniciar.pack(pady=10)

    # Logs
    area_log = tk.Text(
        ventana,
        width=95,
        height=22,
        bg="black",
        fg="#00ff00"
    )

    area_log.pack(pady=10)

    ventana.mainloop()