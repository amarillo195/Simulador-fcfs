class Proceso:

    def __init__(self, nombre, tiempo_cpu, llegada):

        self.nombre = nombre
        self.tiempo_cpu = tiempo_cpu
        self.llegada = llegada

        self.restante = tiempo_cpu

        self.estado = "Nuevo"

        self.inicio = None
        self.fin = None