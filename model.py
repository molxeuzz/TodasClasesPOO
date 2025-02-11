
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre: str = nombre
        self.precio: float = precio
    def mostrar_info(self) -> str:
        return f"{self.nombre} - {self.precio}"