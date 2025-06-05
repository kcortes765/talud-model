import types
import importlib
import sys


class DummyWidget:
    def __init__(self, *args, **kwargs):
        self.text = kwargs.get("text", "")
        self.command = kwargs.get("command")
    def pack(self, *args, **kwargs):
        pass


class DummyRoot:
    def __init__(self, *args, **kwargs):
        self.title_text = None
    def title(self, text):
        self.title_text = text
    def mainloop(self):
        pass


dummy_ctk = types.SimpleNamespace(
    CTk=DummyRoot,
    CTkButton=DummyWidget,
    CTkLabel=DummyWidget,
    CTkEntry=DummyWidget,
)

def test_gui_has_buttons(monkeypatch):
    monkeypatch.setitem(sys.modules, "customtkinter", dummy_ctk)
    import src.gui.gui_app as gui_app
    importlib.reload(gui_app)
    root = dummy_ctk.CTk()
    app = gui_app.SlopeStabilityApp(root)
    texts = [app.btn_analizar.text, app.btn_limpiar.text]
    assert "ANALIZAR TALUD" in texts
    assert "LIMPIAR" in texts
    assert all("EXPORTAR" not in t for t in texts)
