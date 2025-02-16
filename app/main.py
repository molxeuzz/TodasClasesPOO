
from app.interface import TiendaUI
from app.model import Tienda, Cliente

def main():
    cliente = Cliente("Juan")  # Creamos un cliente
    tienda: Tienda = Tienda("Tienda barata", cliente)
    interface: TiendaUI = TiendaUI(tienda)
    interface.ejecutar()

if __name__ == "__main__":
    main()

# proyecto parcialmente terminado, falta completar las demas partes.