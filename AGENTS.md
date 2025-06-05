# Guía para el Agente de IA: Reconstrucción del Proyecto `estabilidad-taludes_model`

## 1. Objetivo General del Proyecto

Reconstruir desde cero una aplicación de escritorio robusta y funcional para el análisis de estabilidad de taludes, utilizando los métodos de Bishop simplificado y Fellenius. La aplicación debe contar con una interfaz gráfica de usuario (GUI) intuitiva, un motor de cálculo preciso y una estrategia de pruebas exhaustiva para garantizar su fiabilidad.

## 2. Contexto y Problemas a Resolver (Basado en la Versión Anterior)

La versión previa del proyecto presentaba deficiencias críticas que deben ser corregidas en esta nueva implementación:

*   **Restricción del Área de Búsqueda de Círculos de Falla:** El algoritmo de optimización de círculos era demasiado restrictivo, impidiendo la detección del círculo crítico en ciertos escenarios.
*   **GUI Inoperante:** Los botones "ANALIZAR TALUD" y "LIMPIAR" no funcionaban correctamente. La funcionalidad "EXPORTAR" debe ser eliminada por completo.
*   **Falta de Calidad del Código:** Ausencia de pruebas exhaustivas, manejo de errores deficiente, configuración rígida y modularización inadecuada.

## 3. Plan de Trabajo Detallado

El proyecto se abordará en fases, asegurando una base sólida y la corrección de todas las problemáticas identificadas.

### Fase 1: Configuración del Entorno y Estructura Base

1.  **Inicialización del Repositorio Git:**
    *   Crear un nuevo repositorio Git vacío.
    *   Realizar el commit inicial con un `README.md` básico.
2.  **Definición y Creación de la Estructura de Directorios:**
    *   `src/`: Código fuente de la aplicación.
        *   `src/core/`: Lógica de negocio (cálculos, optimización, validación central).
        *   `src/data/`: Definiciones de modelos de datos (dataclasses).
        *   `src/gui/`: Implementación de la interfaz de usuario.
        *   `src/utils/`: Funciones auxiliares genéricas (logging, helpers).
    *   `tests/`: Pruebas unitarias y de integración.
    *   `config/`: Archivos de configuración externa.
    *   `docs/`: Documentación del proyecto.
    *   `requirements.txt`: Dependencias del proyecto.
3.  **Gestión de Dependencias:**
    *   Crear `requirements.txt` con las dependencias necesarias: `customtkinter`, `numpy`, `matplotlib`, `scipy`, `pytest`, `pytest-cov`.
    *   Instalar todas las dependencias.
4.  **Creación del `README.md` Detallado:**
    *   Incluir descripción del proyecto, propósito, funcionalidades, instrucciones de instalación, configuración y ejecución, y una guía para desarrolladores.

### Fase 2: Modelos de Datos y Lógica de Negocio (Core)

1.  **`src/data/models.py` - Definición de Modelos:**
    *   Implementar todas las dataclasses necesarias (e.g., `CirculoFalla`, `Estrato`, `Dovela`, `PerfilTerreno`, `PropiedadesSuelo`).
    *   Asegurar la correcta definición y manejo de atributos críticos como `y_base` y `y_superficie` en `Dovela`.
    *   Aplicar `type hinting` exhaustivo.
2.  **`src/core/calculos.py` - Métodos de Análisis Fundamental:**
    *   Implementar `crear_dovelas` (cálculo geométrico, altura, peso, presión de poros).
    *   Desarrollar los algoritmos de `Bishop Simplificado` y `Fellenius` para el cálculo del Factor de Seguridad.
    *   Crear funciones auxiliares robustas (interpolación, geometría).
3.  **`src/core/optimizacion.py` - Algoritmo de Búsqueda de Círculos:**
    *   Implementar el "Smart Circle Optimizer".
    *   **CRÍTICO:** Diseñar y codificar una lógica de límites y validación de círculos (`validar_y_corregir_circulo` o similar) que sea inherentemente flexible y permita una exploración amplia del espacio de búsqueda, evitando las restricciones previas.
4.  **`src/core/validacion.py` - Validación de Datos de Entrada (Core):**
    *   Implementar un sistema de validación de datos de entrada a nivel de la lógica de negocio, independiente de la GUI.
    *   Validar rangos, tipos, consistencia y coherencia de los datos.
    *   Lanzar excepciones personalizadas y descriptivas.

### Fase 3: Desarrollo de la Interfaz Gráfica de Usuario (GUI)

1.  **`src/gui/gui_app.py` - Clase Principal de la Aplicación GUI:**
    *   Diseñar y construir una interfaz de usuario moderna y responsiva con `customtkinter`.
    *   Implementar widgets para la entrada de parámetros (talud, suelo, nivel freático).
    *   **Funcionalidad de Botones - Corrección y Mejora:**
        *   **"ANALIZAR TALUD":** Conectar de forma robusta con la lógica de `src/core/`. Asegurar que inicie el análisis, muestre el progreso y actualice los resultados.
        *   **"LIMPIAR":** Implementar la funcionalidad completa para restablecer *todos* los campos de entrada, paneles de resultados y gráficos a su estado inicial.
        *   **Eliminación de "EXPORTAR":** No incluir ningún botón o código relacionado con la funcionalidad de exportación.
    *   Desarrollar paneles para la visualización clara de resultados numéricos y gráficos interactivos.
2.  **`start_gui.py` - Punto de Entrada de la Aplicación:**
    *   Crear un script mínimo para instanciar y ejecutar la aplicación GUI.
    *   Asegurar el uso correcto de `app.root.mainloop()` para el bucle principal de Tkinter.

### Fase 4: Implementación de la Estrategia de Pruebas Exhaustiva

1.  **Configuración de Pytest y Cobertura:**
    *   Configurar `pytest` para el descubrimiento automático de pruebas.
    *   Integrar `pytest-cov` para medir la cobertura de código, con un objetivo mínimo del **80%** en los módulos `src/core/`, `src/gui/gui_app.py`, y `src/data/models.py`.
2.  **Pruebas Unitarias (Módulos `src/core/` y `src/data/`):**
    *   `tests/test_models.py`: Validar la creación y el comportamiento de las dataclasses.
    *   `tests/test_calculos.py`: Pruebas de `crear_dovelas` y los métodos de Bishop/Fellenius con diversos escenarios y casos de prueba conocidos.
    *   `tests/test_optimizacion.py`: Validar el algoritmo de optimización en diferentes topologías de taludes. **Énfasis:** Pruebas rigurosas sobre la flexibilidad del área de búsqueda.
    *   `tests/test_validacion.py`: Probar la validación de datos de entrada con datos válidos, inválidos y casos extremos.
3.  **Pruebas de la GUI (con Mocking/Simulación):**
    *   `tests/test_gui_buttons.py`: Simular interacciones con los botones "ANALIZAR TALUD" y "LIMPIAR", verificando su funcionalidad y el estado de la GUI. Confirmar la ausencia del botón "EXPORTAR".
    *   `tests/test_gui_inputs.py`: Validar la entrada y recuperación de datos en los widgets de la GUI.
    *   `tests/test_gui_display.py`: Asegurar que los resultados y gráficos se actualizan correctamente en la interfaz.
4.  **Pruebas de Integración y Regresión:**
    *   `tests/test_full_analysis_flow.py`: Simular flujos completos de usuario (entrada de datos -> análisis -> visualización de resultados).
    *   Crear pruebas de regresión para asegurar que las nuevas funcionalidades o correcciones no introducen errores.
    *   Probar escenarios de error de extremo a extremo para verificar el manejo de errores en toda la aplicación.

### Fase 5: Mejoras Técnicas Adicionales y Documentación

1.  **Manejo de Errores y Logging Avanzado:**
    *   Implementar un sistema de logging centralizado (`logging` de Python) para registrar eventos, advertencias y errores.
    *   Desarrollar un mecanismo para presentar mensajes de error claros y amigables al usuario en la GUI.
2.  **Externalización de la Configuración:**
    *   Crear un archivo de configuración (`config/settings.json` o `.ini`) para parámetros ajustables (ej. número de iteraciones del optimizador, tolerancias, límites de búsqueda, valores por defecto).
    *   Implementar la carga y el uso de estos parámetros.
3.  **Refinamiento de la Modularización y Separación de Responsabilidades:**
    *   Mantener una separación estricta entre la GUI, la lógica de negocio y la capa de datos.
    *   Minimizar el acoplamiento y maximizar la cohesión de los módulos.
4.  **Uso Consistente de Type Hinting:**
    *   Asegurar que todos los nuevos desarrollos y las refactorizaciones incluyan type hints.
5.  **Documentación del Código y del Proyecto:**
    *   Escribir docstrings claros y concisos para todas las clases, métodos y funciones.
    *   Mantener el `README.md` actualizado.
    *   Considerar la creación de documentación adicional en `docs/`.

## 4. Prioridades Clave

*   **Funcionalidad Core:** Asegurar que los cálculos de Bishop y Fellenius, la creación de dovelas y la optimización de círculos (con el área de búsqueda ampliada) funcionen de manera precisa y robusta.
*   **GUI Funcional:** Garantizar que los botones "ANALIZAR TALUD" y "LIMPIAR" operen correctamente y que la funcionalidad "EXPORTAR" sea eliminada.
*   **Estrategia de Pruebas:** Desarrollar las pruebas unitarias y de integración de manera concurrente con el desarrollo de la funcionalidad.

## 5. Reporte de Progreso

Se espera un reporte regular sobre el avance en cada fase, destacando los hitos alcanzados, los desafíos encontrados y las soluciones implementadas.