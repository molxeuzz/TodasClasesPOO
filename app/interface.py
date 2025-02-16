
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from rich.console import Console
from app.model import Tienda, Producto

class TiendaUI:
    def __init__(self, tienda: Tienda):
        self.tienda: Tienda = tienda
        self.consola: Console = Console()

    def mostrar_menu(self):
        self.consola.print("\n[bold green]Tienda virtual[/bold green]")
        self.consola.print("\n 1. Agregar producto a la tienda")
        self.consola.print(" 2. Mostrar productos de la tienda")
        self.consola.print(" 3. Agregar producto al carrito")
        self.consola.print(" 4. Mostrar carrito de compras")
        self.consola.print(" 5. Calcular total de la compra")
        self.consola.print(" 6. Salir")
        opcion = Prompt.ask("\n Seleccione una opcion: ", choices=["1", "2", "3", "4", "5", "6"])

        return opcion

    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            match opcion:
                case "1":
                    self.agregar_producto_a_tienda()
                case "2":
                    self.mostrar_productos_tienda()
                case "3":
                    self.agregar_producto_a_carrito()
                case "4":
                    self.mostrar_productos_carrito()
                case "5":
                    self.calcular_total_compra()
                case "6":
                    self.consola.print("Gracias por visitar!!", style="bold yellow")
                    break

    def agregar_producto_a_tienda(self):
        nombre: str = Prompt.ask("Nombre del producto: ")
        precio: float = float(Prompt.ask("Precio del producto: "))
        producto: Producto = Producto(nombre, precio)
        self.tienda.agregar_producto(producto)
        self.consola.print(f"[green] Producto {nombre} agregado exitosamente!! [/green]")

    def mostrar_productos_tienda(self):
        if len(self.tienda.productos) == 0:
            self.consola.print("\n [red] No hay productos en la tienda [/red]")
            return

        tabla: Table = Table(title="\n Lista de productos", box=box.SQUARE_DOUBLE_HEAD)
        tabla.add_column("#", style="yellow")
        tabla.add_column("Nombre", style="yellow")
        tabla.add_column("Precio", style="yellow")

        for i, producto in enumerate(self.tienda.productos, start=1):
            tabla.add_row(str(i), producto.nombre, str(producto.precio))

        self.consola.print(tabla)

    def agregar_producto_a_carrito(self):
        if not self.tienda.productos:
            self.consola.print("[red] No hay productos disponibles para agregar al carrito. [/red]")
            return

        self.mostrar_productos_tienda()
        indice = int(Prompt.ask("Seleccione el número del producto a agregar al carrito: "))

        if 1 <= indice <= len(self.tienda.productos):
            producto = self.tienda.productos[indice - 1]
            self.tienda.cliente.agregar_producto(producto)  # Agregamos al carrito del cliente
            self.consola.print(f"[green] Producto {producto.nombre} agregado al carrito exitosamente!! [/green]")
        else:
            self.consola.print("[red] Selección inválida. [/red]")

    def mostrar_productos_carrito(self):
        if not self.tienda.cliente.carrito:
            self.consola.print("[red] No hay productos en el carrito [/red]")
            return

        tabla = Table(title="\n Carrito de Compras", box=box.SQUARE_DOUBLE_HEAD)
        tabla.add_column("#", style="yellow")
        tabla.add_column("Nombre", style="yellow")
        tabla.add_column("Precio", style="yellow")

        for i, producto in enumerate(self.tienda.cliente.carrito, start=1):
            tabla.add_row(str(i), producto.nombre, f"${producto.precio:.2f}")

        self.consola.print(tabla)

    def calcular_total_compra(self):
        if not self.tienda.cliente.carrito:
            self.consola.print("[red] El carrito está vacío [/red]")
            return

        total = self.tienda.cliente.calcular_total()
        self.consola.print(f"[yellow] Total a pagar: ${total:.2f} [/yellow]")
