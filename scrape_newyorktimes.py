import requests
from bs4 import BeautifulSoup
import sys

def scrape_article(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al acceder a la URL: {response.status_code}")
        return 
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Ejemplo de extracción del New York times
    title = soup.find('h1')
    content = soup.find_all('p')
    
    print("\nTitulo del articulo:\n")
    print(title.get_text() if title else "No encontrado")
    
    print("\nContenido del articulo:\n") 
    for p in content:
        print(p.get_text())
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scrape_newyorktimes.py <URL>")
    else:
        scrape_article(sys.argv[1])