# lab_strings.py
"""
Sesión 02: Tipos de Datos Básicos
Práctica: Texto (String)

Objetivo: Manipular y formatear strings para procesamiento de datos textuales.
"""

def analizar_producto(codigo):
   """
   Analiza el código de un producto y extrae sus componentes
   Formato: TIPO-MARCA-NUMERO (ej: LAP-HP-001)
   """
   # TODO: Separar el código en partes usando split()
   
   # TODO: Convertir tipo a mayúsculas
   
   # TODO: Validar formato del código
   
   return {
       'tipo': '',
       'marca': '',
       'numero': ''
   }

def formatear_descripcion(producto):
   """
   Crea una descripción formateada del producto
   """
   # TODO: Crear descripción usando f-strings
   
   # TODO: Aplicar capitalización apropiada
   
   return ''

def validar_email(email):
   """
   Valida formato básico de email
   """
   # TODO: Verificar @ en email
   
   # TODO: Verificar dominio válido
   
   # TODO: Verificar caracteres permitidos
   
   return False

def main():
   # Casos de prueba
   codigos_prueba = [
       "LAP-HP-001",
       "MON-DELL-123",
       "TEC-LOG-456"
   ]
   
   emails_prueba = [
       "cliente@email.com",
       "soporte@tech",
       "@invalido.com"
   ]
   
   print("=== Sistema de Procesamiento de Texto ===")
   
   # Prueba análisis de códigos
   for codigo in codigos_prueba:
       componentes = analizar_producto(codigo)
       descripcion = formatear_descripcion(componentes)
       print(f"\nCódigo: {codigo}")
       print(f"Descripción: {descripcion}")
   
   # Prueba validación emails
   print("\n=== Validación de Emails ===")
   for email in emails_prueba:
       es_valido = validar_email(email)
       print(f"Email: {email} - {'Válido' if es_valido else 'Inválido'}")

if __name__ == "__main__":
   main()

"""
Ejercicios adicionales:
1. Implementar búsqueda de productos por palabra clave
2. Agregar validación de nombres de producto
3. Crear función para generar códigos de producto
"""