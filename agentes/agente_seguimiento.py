import requests
from swarm import Agent

class SwarmAgentSeguimiento(Agent):
    def __init__(self, laravel_url, checkpoints):
        super().__init__()
        self.name = "Agente de Seguimiento"
        self.laravel_url = laravel_url
        self.checkpoints = checkpoints

    def monitorear_progreso(self, progreso):
        alertas = []
        reconocimientos = []
        for checkpoint in self.checkpoints:
            if checkpoint in progreso["completados"]:
                reconocimientos.append(f"Checkpoint {checkpoint} completado.")
            else:
                alertas.append(f"Checkpoint {checkpoint} pendiente.")
        
        reporte = {"alertas": alertas, "reconocimientos": reconocimientos}
        requests.post(f"{self.laravel_url}/api/seguimiento", json=reporte)
        
        return reporte
