import requests
from swarm import Agent

class SwarmAgentInterpretacionDatos(Agent):
    def __init__(self, laravel_url):
        super().__init__()
        self.name = "Agente de Interpretación de Datos"
        self.laravel_url = laravel_url

    def interpretar_datos(self, perfiles, proyectos):
        habilidades = {}
        for perfil in perfiles:
            for habilidad in perfil["habilidades"]:
                habilidades[habilidad] = habilidades.get(habilidad, 0) + 1
        insights = {
            "habilidades_comunes": sorted(habilidades, key=habilidades.get, reverse=True)[:5],
            "tasa_exito": 85  # Simulado para este ejemplo
        }
        requests.post(f"{self.laravel_url}/api/insights", json=insights)
        
        return insights
