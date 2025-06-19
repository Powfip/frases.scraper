from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar sin abrir ventana

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.mercadolibre.com.mx")

print(driver.title)
driver.quit()
