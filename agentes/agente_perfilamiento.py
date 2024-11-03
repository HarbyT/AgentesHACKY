import openai
import requests
from swarm import Agent

class SwarmAgentPerfilamiento(Agent):
    def __init__(self, laravel_url, api_key):
        super().__init__()
        self.name = "Agente de Perfilamiento"
        self.laravel_url = laravel_url
        openai.api_key = api_key

    def generar_perfil(self, datos_usuario):
        """Genera un perfil personalizado y lo guarda en Laravel"""
        prompt = f"Genera un perfil para el usuario basado en los siguientes datos: {datos_usuario}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        perfil = response.choices[0].text.strip()

        # Guardar perfil en Laravel
        perfil_json = {
            "nombre": datos_usuario["nombre"],
            "perfil": perfil,
            "habilidades": datos_usuario["habilidades"]
        }
        requests.post(f"{self.laravel_url}/api/perfiles", json=perfil_json)
        
        return perfil_json
