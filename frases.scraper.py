from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json

class Frases:
    def __init__(self, texto, autor, etiquetas):
        self.texto = texto
        self.autor = autor
        self.etiquetas = etiquetas
        
def scrapear_frases(url='https://quotes.toscrape.com/'):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service('/opt/homebrew/bin/chromedriver')
    wd = webdriver.Chrome(service=service, options=options)
    
    wd.get(url)
    soup = BeautifulSoup(wd.page_source, 'lxml')
    wd.quit()
    
    frases = []
    
    for frase in soup.find_all('div', {'class':'quote'}):
        # Texto
        texto_tag = frase.find('span', {'class': 'text'})
        texto = texto_tag.get_text(strip=True) if texto_tag else "Texto no encontrado"
        
        # Autor
        autor_tag = frase.find('small', {'class':'author'})
        autor = autor_tag.get_text(strip=True) if autor_tag else "Autor no encontrado"
        
        # Etiquetas
        etiquetas_tags = frase.find_all('a', {'class': 'tags'})
        etiquetas = [tag.get_text(strip=True) for tag in etiquetas_tags]
        
        frases_obj = Frases(texto, autor, etiquetas)
        frases.append(frases_obj)
    
    # Mostrar por pantalla    
    for f in frases:
        print(f"💬Texto: {f.texto}\n✍️ Autor: {f.autor}\n🏷️ Etiquetas: {', '.join(f.etiquetas)}")
    # Guardar como JSON   
    with open('frases.json', 'w', encoding='utf-8') as archivo:
        json.dump([f.__dict__ for f in frases], archivo, ensure_ascii=False, indent=4)
    print(f"✅ Se han guardado {len(frases)} frases en 'frases.json'.")
       
if __name__ == "__main__":
    scrapear_frases()