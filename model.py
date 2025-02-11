
class Producto:

    def __init__(self, nombre: str, precio: float):
        self.nombre: str = nombre
        self.precio: float = precio

    def mostrar_info(self) -> str:
        return f"{self.nombre} - {self.precio}"

p1: Producto = Producto("Arroz", 10000)
p2: Producto = Producto("Panela", 6000)

print(p1.mostrar_info())
print(p2.mostrar_info())