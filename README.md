# Proyecto de Estabilidad de Taludes

Este repositorio contiene la implementación desde cero de una aplicación de escritorio para el análisis de estabilidad de taludes utilizando los métodos de Bishop simplificado y Fellenius.

El proyecto se desarrolla en fases, siguiendo las directrices del archivo `AGENTS.md`. Cada fase incluye funcionalidades nuevas acompañadas de pruebas automatizadas para garantizar la corrección matemática y el buen funcionamiento de la interfaz gráfica.

## Estructura inicial

- `src/` código fuente de la aplicación
  - `core/` lógica de negocio y algoritmos de cálculo
  - `data/` definiciones de modelos de datos
  - `gui/` implementación de la interfaz gráfica con customtkinter
  - `utils/` utilidades y helpers generales
- `tests/` pruebas unitarias e integración
- `config/` archivos de configuración
- `docs/` documentación adicional

## Instalación

1. Crear un entorno virtual de Python
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar las pruebas para verificar la instalación:
   ```bash
   pytest
   ```

## Estado del proyecto

Actualmente se dispone de una versión inicial capaz de ejecutar un pequeño análisis desde la interfaz gráfica. Para lanzar la GUI ejecute:

```bash
python start_gui.py
```

Durante las siguientes iteraciones se seguirá ampliando la lógica de cálculo y el conjunto de pruebas para alcanzar una aplicación completa.

