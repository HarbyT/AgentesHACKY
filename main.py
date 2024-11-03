from agentes.agente_perfilamiento import SwarmAgentPerfilamiento
from agentes.agente_generador_proyectos import SwarmAgentGeneradorProyectos
from agentes.agente_critico import SwarmAgentCritico
from agentes.agente_emparejamiento import SwarmAgentEmparejamiento
from agentes.agente_seguimiento import SwarmAgentSeguimiento
from agentes.agente_interpretacion_datos import SwarmAgentInterpretacionDatos
from swarm import Swarm
import os

laravel_url = "https://tu-laravel-backend.com"
openai_api_key = os.getenv("OPENAI_API_KEY")

swarm = Swarm()
swarm.add_agent(SwarmAgentPerfilamiento(laravel_url, openai_api_key))
swarm.add_agent(SwarmAgentGeneradorProyectos(laravel_url, openai_api_key))
swarm.add_agent(SwarmAgentCritico(laravel_url))
swarm.add_agent(SwarmAgentEmparejamiento(laravel_url))
swarm.add_agent(SwarmAgentSeguimiento(laravel_url, ["Diseño", "Desarrollo", "Pruebas", "Lanzamiento"]))
swarm.add_agent(SwarmAgentInterpretacionDatos(laravel_url))

def ejecutar_flujo(datos_usuario):
    perfil = swarm.get_agent("Agente de Perfilamiento").generar_perfil(datos_usuario)
    propuesta = swarm.get_agent("Agente Generador de Proyectos").generar_propuesta(perfil)
    evaluacion = swarm.get_agent("Agente Crítico").evaluar_propuesta(propuesta)
    equipo = swarm.get_agent("Agente de Emparejamiento").emparejar_usuarios([perfil], [propuesta])
    seguimiento = swarm.get_agent("Agente de Seguimiento").monitorear_progreso({"completados": ["Diseño"]})
    insights = swarm.get_agent("Agente de Interpretación de Datos").interpretar_datos([perfil], [propuesta])
    print("Insights Generados:", insights)

# Ejecutar flujo de trabajo
if __name__ == "__main__":
    datos_usuario = {
        "nombre": "María Pérez",
        "habilidades": ["programación", "diseño gráfico"],
        "experiencia": "intermedio",
        "disponibilidad": "20 horas/semana"
    }
    ejecutar_flujo(datos_usuario)
