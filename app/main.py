
from app.interface import TiendaUI
from app.model import Tienda

def main():
    tienda: Tienda = Tienda("Tienda barata")
    ui: TiendaUI = TiendaUI(tienda)
    ui.ejercutar()

if __name__ == "__main__":
    main()