import requests
from swarm import Agent

class SwarmAgentEmparejamiento(Agent):
    def __init__(self, laravel_url, max_equipo_size=3):
        super().__init__()
        self.name = "Agente de Emparejamiento"
        self.laravel_url = laravel_url
        self.max_equipo_size = max_equipo_size

    def emparejar_usuarios(self, perfiles, proyectos):
        equipo = {
            "proyecto": proyectos[0]["proyecto"],
            "equipo": [perfil["nombre"] for perfil in perfiles[:self.max_equipo_size]],
            "roles": ["Miembro" for _ in range(len(perfiles[:self.max_equipo_size]))]
        }
        requests.post(f"{self.laravel_url}/api/equipos", json=equipo)
        return equipo
