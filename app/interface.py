
from rich.console import Console
from app.model import Tienda

class TiendaUI:
    def __init__(self, tienda: Tienda):
        self.tienda: Tienda = tienda
        self.consola: Console = Console()
