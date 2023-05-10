class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_logs(self) -> dict[str, any]:

        solicitudes_get: int = 0
        solicitudes_post: int = 0
        respuesta_total: int = 0
        solicitud: dict = {}
        solicitudes: int = 0

        with open('eventos.txt') as eventos:

            for line in eventos:

                if "Fecha y hora" in line:
                    solicitudes += 1
                    solicitud["solicitudes"] = solicitudes
                elif "POST" in line:
                    respuesta_total += line.strip().split(": ")[1]
                    solicitud["codigo de respuesta totales"] = 1

                elif "GET" in line:
                    solicitudes_get += 1
                    solicitud["Solicitudes por GET"] = solicitudes_get

                elif "POST" in line:
                    solicitudes_post += 1
                    solicitud["Solicitudes por POST"] = solicitudes_post


            return solicitud


evento = AnalizadorLogs("eventos")
print(evento.procesar_logs())
