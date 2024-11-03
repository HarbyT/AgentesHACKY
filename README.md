# Hacky Project - Sistema de Agentes de IA con Integración en Laravel

Este proyecto implementa un sistema modular de agentes de inteligencia artificial para la plataforma "Hacky". Los agentes de IA colaboran para personalizar y gestionar proyectos para usuarios, generando perfiles, creando proyectos personalizados, evaluando su viabilidad, emparejando usuarios y proporcionando retroalimentación continua.

## Estructura de Agentes

1. **Agente de Perfilamiento de Usuarios**: Genera perfiles detallados de los usuarios.
2. **Agente Generador de Proyectos**: Crea proyectos personalizados según los perfiles.
3. **Agente Crítico/Discriminador**: Evalúa los proyectos generados.
4. **Agente de Emparejamiento (Matching)**: Forma equipos basados en habilidades y disponibilidad.
5. **Agente de Seguimiento y Retroalimentación**: Monitorea el progreso de los proyectos.
6. **Agente de Interpretación de Datos**: Analiza datos de usuarios y proyectos para extraer insights.

## Configuración del Proyecto

### Requisitos Previos

- Python 3.10+
- Clave de API de OpenAI para integrar el LLM
- Laravel backend (se debe configurar la URL de la API en `main.py`)

### Instalación de Dependencias

Clona el repositorio y navega a la carpeta del proyecto:

```bash
git clone https://github.com/HarbyT/AgentesHACKY.git
cd AgentesHACKY
