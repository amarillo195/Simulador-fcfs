import time

from utils import escribir_log


def simulacion_fcfs(
    procesos,
    area_log,
    label_cpu_actual
):

    if len(procesos) == 0:

        escribir_log(area_log, "⚠️ No hay procesos")

        return

    tiempo_actual = 0

    cola = []

    proceso_actual = None

    completados = []

    escribir_log(
        area_log,
        "\n========== INICIO FCFS ==========\n"
    )

    while len(completados) < len(procesos):

        escribir_log(
            area_log,
            f"\n⏱️ Tiempo actual: {tiempo_actual}"
        )

        # Llegada de procesos
        for proceso in procesos:

            if proceso.llegada == tiempo_actual:

                proceso.estado = "Listo"

                cola.append(proceso)

                escribir_log(
                    area_log,
                    f"🟡 {proceso.nombre} llegó al sistema"
                )

        # CPU toma proceso
        if proceso_actual is None and len(cola) > 0:

            proceso_actual = cola.pop(0)

            proceso_actual.estado = "Ejecutando"

            if proceso_actual.inicio is None:

                proceso_actual.inicio = tiempo_actual

            escribir_log(
                area_log,
                f"🟢 {proceso_actual.nombre} entra a CPU"
            )

        # Ejecutar proceso
        if proceso_actual:

            label_cpu_actual.config(
                text=f"CPU ACTUAL: {proceso_actual.nombre}"
            )

            proceso_actual.restante -= 1

            escribir_log(
                area_log,
                f"🔥 Ejecutando {proceso_actual.nombre}"
                f" | Restante: {proceso_actual.restante}"
            )

            # Finalización
            if proceso_actual.restante == 0:

                proceso_actual.estado = "Finalizado"

                proceso_actual.fin = tiempo_actual + 1

                completados.append(proceso_actual)

                escribir_log(
                    area_log,
                    f"✅ {proceso_actual.nombre} FINALIZÓ"
                )

                proceso_actual = None

        else:

            label_cpu_actual.config(
                text="CPU ACTUAL: LIBRE"
            )

        cola_nombres = [p.nombre for p in cola]

        escribir_log(
            area_log,
            f"📋 Cola: "
            f"{cola_nombres if cola_nombres else 'Vacía'}"
        )

        tiempo_actual += 1

        time.sleep(1)

    # Resultados
    escribir_log(
        area_log,
        "\n========== RESULTADOS ==========\n"
    )

    total_espera = 0

    total_retorno = 0

    for proceso in procesos:

        retorno = proceso.fin - proceso.llegada

        espera = retorno - proceso.tiempo_cpu

        total_espera += espera

        total_retorno += retorno

        escribir_log(area_log, f"🧩 {proceso.nombre}")

        escribir_log(
            area_log,
            f"   Espera: {espera}"
        )

        escribir_log(
            area_log,
            f"   Retorno: {retorno}\n"
        )

    promedio_espera = total_espera / len(procesos)

    promedio_retorno = total_retorno / len(procesos)

    escribir_log(
        area_log,
        f"📈 Tiempo promedio de espera: "
        f"{promedio_espera}"
    )

    escribir_log(
        area_log,
        f"📈 Tiempo promedio de retorno: "
        f"{promedio_retorno}"
    )

    label_cpu_actual.config(
        text="CPU ACTUAL: FINALIZADA"
    )