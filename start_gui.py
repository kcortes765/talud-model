"""Punto de entrada para la aplicación de escritorio."""

from __future__ import annotations

import customtkinter as ctk

from src.gui.gui_app import SlopeStabilityApp
from src.core.optimizacion import smart_circle_optimizer
from src.utils.config import load_settings
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("talud.app")
    settings = load_settings("config/settings.json")

    def run_analysis() -> None:
        smart_circle_optimizer(
            [0, 1, 0, 1, 0.5, 1.0],
            n_dovelas=settings.get("n_dovelas", 4),
            peso_unitario=settings.get("peso_unitario", 18.0),
            angulo_friccion=settings.get("angulo_friccion", 30.0),
        )
        logger.info("Análisis completado")

    app = SlopeStabilityApp(analyze_callback=run_analysis)
    app.mainloop()


if __name__ == "__main__":
    main()
