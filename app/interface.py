import Prompt
from rich.console import Console
from app.model import Tienda

class TiendaUI:
    def __init__(self, tienda: Tienda):
        self.tienda: Tienda = tienda
        self.consola: Console = Console()

    def mostrar_menu(self):
        self.consola.print("\n[bold green]Tienda virtual[/bold green]")
        self.consola.print("\n 1. Agregar producto a la tienda")
        self.consola.print("\n 2. Mostrar productos de la tienda")
        self.consola.print("\n 3. Agregar producto al carrito")
        self.consola.print("\n 4. Mostrar carrito de compras")
        self.consola.print("\n 5. Calcular total de la compra")
        self.consola.print("\n 6. Salir")
        opcion = Prompt.ask("\n Seleccione una opcion: ", choices=["1", "2", "3", "4", "5", "6"])

        return opcion

    def ejercutar(self):
        while True:
            opcion = self.mostrar_menu()
            match opcion:
                case "1":

                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    self.consola.print("Gracias!!", style="bold yellow")
                    break