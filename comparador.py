# Mostrar resultados
from ejercicio2scraper import scrapear_productos
import json

productos = scrapear_productos()
# Comparador de productos Xiaomi en Amazon
for p in productos:
    print(f"📦 Título: {p.titulo}\n💰 Precio: {p.precio}\n🖼️ Imagen: {p.imagen}\n")
    
# Guardar como JSON
with open('productos.json', 'w', encoding='utf-8') as archivo_json:
    json.dump([p.__dict__ for p in productos], archivo_json, ensure_ascii=False, indent=4)
    
print(f"✅ Se han guardado {len(productos)} productos en 'productos.json'.")