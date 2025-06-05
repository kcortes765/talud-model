"""Punto de entrada para la aplicación de escritorio."""

from __future__ import annotations

import customtkinter as ctk

from src.gui.gui_app import SlopeStabilityApp
from src.core.optimizacion import smart_circle_optimizer


def main() -> None:
    def run_analysis() -> None:
        # Parámetros mínimos de ejemplo
        smart_circle_optimizer([0, 1, 0, 1, 0.5, 1.0], n_dovelas=4, peso_unitario=18.0, angulo_friccion=30.0)

    app = SlopeStabilityApp(analyze_callback=run_analysis)
    app.mainloop()


if __name__ == "__main__":
    main()
