import requests
from swarm import Agent

class SwarmAgentCritico(Agent):
    def __init__(self, laravel_url):
        super().__init__()
        self.name = "Agente Crítico"
        self.laravel_url = laravel_url

    def evaluar_propuesta(self, propuesta):
        aprobado = "completo" in propuesta["proyecto"]
        retroalimentacion = "El proyecto cumple con los requisitos" if aprobado else "El proyecto necesita ajustes."

        evaluacion_json = {
            "proyecto": propuesta["proyecto"],
            "aprobado": aprobado,
            "retroalimentacion": retroalimentacion
        }
        requests.post(f"{self.laravel_url}/api/evaluaciones", json=evaluacion_json)

        return evaluacion_json
