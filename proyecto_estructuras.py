# proyecto_estructuras.py
"""
Sesión 02: Estructuras de Datos en Python
Proyecto: Sistema de Gestión de Inventario Inteligente

Objetivo: Implementar un sistema de gestión que use diferentes estructuras de datos
para manejar un inventario de productos tecnológicos.
"""

from datetime import datetime

class SistemaInventario:
   def __init__(self):
       # Lista de productos
       self.productos = []
       
       # Diccionario de categorías
       self.categorias = {
           'LAP': 'Laptops',
           'CEL': 'Celulares',
           'TAB': 'Tablets',
           'ACC': 'Accesorios'
       }
       
       # Tupla de estados válidos
       self.estados = ('disponible', 'agotado', 'descontinuado')
       
       # Diccionario de proveedores
       self.proveedores = {}

   def agregar_producto(self, codigo, nombre, precio, categoria):
       """Agrega un nuevo producto al inventario"""
       producto = {
           'codigo': codigo,
           'nombre': nombre,
           'precio': precio,
           'categoria': categoria,
           'stock': 0,
           'estado': self.estados[0],
           'historial': []
       }
       self.productos.append(producto)
       return True

   def registrar_movimiento(self, codigo, cantidad, tipo):
       """Registra entrada o salida de inventario"""
       for producto in self.productos:
           if producto['codigo'] == codigo:
               if tipo == 'entrada':
                   producto['stock'] += cantidad
               elif tipo == 'salida' and producto['stock'] >= cantidad:
                   producto['stock'] -= cantidad
               
               producto['historial'].append({
                   'fecha': datetime.now(),
                   'tipo': tipo,
                   'cantidad': cantidad
               })
               
               self._actualizar_estado(producto)
               return True
       return False

   def _actualizar_estado(self, producto):
       """Actualiza el estado del producto según el stock"""
       if producto['stock'] <= 0:
           producto['estado'] = self.estados[1]  # agotado
       else:
           producto['estado'] = self.estados[0]  # disponible

   def generar_reporte(self):
       """Genera reporte de inventario"""
       reporte = {
           'total_productos': len(self.productos),
           'por_categoria': {},
           'valor_total': 0,
           'agotados': []
       }
       
       for producto in self.productos:
           # Conteo por categoría
           cat = producto['categoria']
           if cat not in reporte['por_categoria']:
               reporte['por_categoria'][cat] = 0
           reporte['por_categoria'][cat] += 1
           
           # Cálculo valor total
           reporte['valor_total'] += producto['precio'] * producto['stock']
           
           # Lista de agotados
           if producto['estado'] == 'agotado':
               reporte['agotados'].append(producto['codigo'])
       
       return reporte

def main():
   # Inicializar sistema
   sistema = SistemaInventario()
   
   # Agregar productos
   sistema.agregar_producto('LAP001', 'Laptop HP', 1299.99, 'LAP')
   sistema.agregar_producto('CEL001', 'iPhone 13', 999.99, 'CEL')
   
   # Registrar movimientos
   sistema.registrar_movimiento('LAP001', 5, 'entrada')
   sistema.registrar_movimiento('LAP001', 2, 'salida')
   
   # Generar reporte
   reporte = sistema.generar_reporte()
   
   # Mostrar resultados
   print("\n=== Reporte de Inventario ===")
   print(f"Total productos: {reporte['total_productos']}")
   print("\nPor categoría:")
   for cat, cantidad in reporte['por_categoria'].items():
       print(f"- {cat}: {cantidad}")
   print(f"\nValor total: ${reporte['valor_total']:,.2f}")
   print(f"Productos agotados: {len(reporte['agotados'])}")

if __name__ == "__main__":
   main()

"""
Ejercicios de extensión:
1. Agregar manejo de múltiples almacenes
2. Implementar sistema de alertas de stock bajo
3. Agregar análisis de tendencias de movimientos
4. Implementar sistema de descuentos por volumen
"""