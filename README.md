# Sistema de Compras en una Tienda Virtual

## Descripción General
Este proyecto implementa un sistema de compras en una tienda virtual utilizando Programación Orientada a Objetos (POO). Permite la gestión de productos, la administración de un cliente y la simulación de una compra a través de un carrito de compras.

## Requisitos del Sistema
El sistema cuenta con las siguientes clases:

### Clase `Producto`
**Atributos:**
- `nombre` (str): Nombre del producto.
- `precio` (float): Precio del producto.

**Métodos:**
- `mostrar_info()`: Devuelve una cadena con el nombre y el precio del producto.

### Clase `Cliente`
**Atributos:**
- `nombre` (str): Nombre del cliente.
- `carrito` (list): Lista de productos agregados al carrito de compras.

**Métodos:**
- `agregar_producto(producto: Producto)`: Agrega un producto al carrito.
- `mostrar_carrito()`: Muestra la lista de productos en el carrito.
- `calcular_total()`: Devuelve la suma total de los precios de los productos en el carrito.

### Clase `Tienda`
**Atributos:**
- `nombre` (str): Nombre de la tienda.
- `productos` (list): Lista de productos disponibles en la tienda.

**Métodos:**
- `agregar_producto(producto: Producto)`: Agrega un producto a la tienda.
- `mostrar_productos()`: Muestra la lista de productos disponibles en la tienda.

## Interacción con el Usuario (Menú de Opciones)
El sistema permite al usuario interactuar a través de un menú en la consola con las siguientes opciones:

1. **Agregar producto a la tienda**: Permite registrar un nuevo producto en la tienda con su nombre y precio.
2. **Mostrar productos de la tienda**: Muestra todos los productos disponibles en la tienda.
3. **Agregar producto al carrito**: Permite que el cliente agregue un producto disponible en la tienda a su carrito de compras.
4. **Mostrar carrito de compras**: Muestra los productos que el cliente ha agregado al carrito.
5. **Calcular total de compra**: Calcula y muestra el precio total de los productos en el carrito.
6. **Salir**: Finaliza la ejecución del programa.

## Restricciones
- El sistema debe validar que los productos agregados al carrito existan en la tienda.
- Se debe manejar correctamente la entrada de datos del usuario para evitar errores.

## Tecnologías Utilizadas
- Python 3
- Programación Orientada a Objetos (POO)
- Python UV
- Python Rich

## Instalación y Ejecución
1. Clonar este repositorio.
2. Ejecutar el script principal con Python:
   ```sh
   python -m main.py
   ```

## Autor
- Mateo Molina Gonzalez y Universidad de Medellín
