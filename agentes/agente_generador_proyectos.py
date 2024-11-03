import openai
import requests
from swarm import Agent

class SwarmAgentGeneradorProyectos(Agent):
    def __init__(self, laravel_url, api_key):
        super().__init__()
        self.name = "Agente Generador de Proyectos"
        self.laravel_url = laravel_url
        openai.api_key = api_key

    def generar_propuesta(self, perfil_usuario):
        prompt = f"Crea una propuesta de proyecto para un usuario con el siguiente perfil: {perfil_usuario['perfil']}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        propuesta = response.choices[0].text.strip()

        # Guardar propuesta en Laravel
        propuesta_json = {
            "usuario": perfil_usuario["nombre"],
            "proyecto": propuesta
        }
        requests.post(f"{self.laravel_url}/api/proyectos", json=propuesta_json)

        return propuesta_json

