
class Producto:

    def __init__(self, nombre: str, precio: float):
        self.nombre: str = nombre
        self.precio: float = precio

    def mostrar_info(self) -> str:
        return f"{self.nombre} - {self.precio}"

class Cliente:

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.carrito: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.carrito.append(producto)

    def mostrar_carrito(self) -> str:
        carrito_str: str = ""
        for producto in self.carrito:
            carrito_str += producto.mostrar_info() + "\n"
        return carrito_str

    def mostrar_carrito(self) -> float:
        total: float = 0
        for producto in self.carrito:
            total += producto.precio
        return total

p1: Producto = Producto("Arroz", 10000)
p2: Producto = Producto("Panela", 6000)

print(p1.mostrar_info())
print(p2.mostrar_info())

