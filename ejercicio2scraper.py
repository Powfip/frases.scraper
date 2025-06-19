from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import time

class Producto:
    def __init__(self, titulo, precio, enlace=None):
        self.titulo = titulo
        self.precio = precio
        self.enlace = enlace
        
def scrapear_productos(url='https://www.mercadolivre.com.br/ofertas'):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service('/opt/homebrew/bin/chromedriver')
    wd = webdriver.Chrome(service=service, options=options)
    
    wd.get(url)
    time.sleep(3)  # esperar que cargue JS
    soup = BeautifulSoup(wd.page_source, "lxml")
    wd.quit()
    
    productos = []
    
    # Buscar todos los bloques que contienen un producto
    for h3 in soup.find_all('h3', {'class': 'poly-component__title-wrapper'}):
        a_tag = h3.find('a', class_='poly-component__title')
        if not a_tag:
            continue
        
        titulo = a_tag.get_text(strip=True)
        enlace = a_tag.get('href', 'Enlace no encontrado')

        # Buscar el contenedor padre (el div o li que envuelve título + precio)
        producto_contenedor = h3.find_parent()

        # Buscar precio en el contenedor padre
        precio_tag = producto_contenedor.find('span', class_='andes-money-amount andes-money-amount--cents-superscript')
        precio = precio_tag['aria-label'] if precio_tag and precio_tag.has_attr('aria-label') else "Precio no encontrado"
        
        producto_obj = Producto(titulo, precio, enlace)
        productos.append(producto_obj)
    
    # Mostrar resultados
    for p in productos:
        print(f"📦 Título: {p.titulo}\n💰 Precio: {p.precio}\n🔗 Enlace: {p.enlace}\n")
        
    with open('productos.json', 'w', encoding='utf-8') as archivo:
        json.dump([p.__dict__ for p in productos], archivo, ensure_ascii=False, indent=4)
        
    print(f"✅ Se han guardado {len(productos)} productos en 'productos.json'")
    
if __name__ == "__main__":
    scrapear_productos()
