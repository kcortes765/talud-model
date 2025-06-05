"""Interfaz gráfica básica para el análisis de estabilidad de taludes."""

from __future__ import annotations

import customtkinter as ctk
from typing import Callable, Optional


class SlopeStabilityApp:
    """Aplicación principal con botones de análisis y limpieza."""

    def __init__(self, root: Optional[ctk.CTk] = None,
                 analyze_callback: Optional[Callable[[], None]] = None,
                 clean_callback: Optional[Callable[[], None]] = None) -> None:
        self.root = root or ctk.CTk()
        self.root.title("Estabilidad de Taludes")
        self.analyze_callback = analyze_callback or (lambda: None)
        self.clean_callback = clean_callback or (lambda: None)
        self._build_ui()

    def _build_ui(self) -> None:
        self.btn_analizar = ctk.CTkButton(
            master=self.root,
            text="ANALIZAR TALUD",
            command=self.analyze_callback,
        )
        self.btn_analizar.pack(padx=10, pady=10)

        self.btn_limpiar = ctk.CTkButton(
            master=self.root,
            text="LIMPIAR",
            command=self.clean_callback,
        )
        self.btn_limpiar.pack(padx=10, pady=10)

    def mainloop(self) -> None:
        self.root.mainloop()
