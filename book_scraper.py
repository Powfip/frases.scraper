from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json

class Libros:
    def __init__(self, titulo, precio, imagen=None):
        self.titulo = titulo
        self.precio = precio
        self.imagen = imagen
        
def scrapear_livros(url='https://books.toscrape.com/'):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service('/opt/homebrew/bin/chromedriver')
    wd = webdriver.Chrome(service=service, options=options)
    
    wd.get(url)
    soup = BeautifulSoup(wd.page_source, "lxml")
    wd.quit()
    
    libros = []
    
    for libro in soup.find_all('article', {'class': 'product_pod'}):
        # Título
        titulo_tag = libro.find('h3').find('a')
        titulo = titulo_tag['title'] if titulo_tag and titulo_tag.has_attr('title') else "Título no encontrado"
        
        # Precio
        precio_tag = libro.find('p', {'class': 'price_color'})
        precio = precio_tag.get_text(strip=True) if precio_tag else "Precio no encontrado"
        
        # Imagen
        imagen_tag = libro.find('img')
        imagen = 'https://books.toscrape.com/' + imagen_tag['src'].replace('../', '') if imagen_tag else "Imagen no encontrada"
        
        libro_obj = Libros(titulo, precio, imagen)
        libros.append(libro_obj)
        
    for l in libros:
        print(f"📦Título: {l.titulo}\n💰 Precio: {l.precio}\n🖼️ Imagen: {l.imagen}")
        
    with open('libros.json', 'w', encoding='utf-8') as archivo:
        json.dump([l.__dict__ for l in libros], archivo, ensure_ascii=False, indent=4)
        
    print(f"✅ Se han guardado {len(libros)} libros en 'libros.json'.")
    
if __name__ == "__main__":
    scrapear_livros()