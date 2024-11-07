# Partint de l'estructura bàsica, (exemple anterior01-intro),
# volem seleccionar el preu del llibre d'amazon, (veure imatge adjunta)
# Importem selenium, en particular el webdriver.
from selenium import webdriver
# Afegim el següent per evitar captchas
# https://stackoverflow.com/questions/58872451/how-can-i-bypass-the-google-captcha-with-selenium-and-python
from fake_useragent import UserAgent
ua = UserAgent()
user_agent = ua.random
# Importem By per seleccionar elements
from selenium.webdriver.common.by import By

# Opcions per mantenir el navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f'--user-agent={user_agent}')
# Creem un driver
driver = webdriver.Chrome(options=chrome_options)

# Obrim el navegador a la pagina que volem fer scraping
URL = "https://www.amazon.com/Scraping-Python-Community-Experience-Distilled/dp/1782164367/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr="
driver.get(URL)
driver.maximize_window()

# Podem usar diferents selectors:
# https://www.selenium.dev/documentation/webdriver/elements/locators/
# Inspeccionem l'element que volem recuperar amb el navegador, el preu és a:
# <span class="a-price-whole">26</span>
# <span class="a-price-fraction">99</span>
# Això és a dins d'un div amb un id:
# <div id="corePriceDisplay_desktop_feature_div" ...
# En aquest cas fem servir, (veure documentació):
# find_element() i By.CLASS_NAME, seleccionem el que ens interessa.
dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# Mostrem per consola el preu. Per fer-ho però, cal tenir en compte que
# les variables dollars i cents contenen un objecte selenium i nosaltres volem
# el contingut (textContent) de l'objecte, això ho recuperem amb la propietat text:
print(f"El preu del llibre és ${dollars.text}.{cents.text}")

# Tanquem el navegador manualment cop s'han realitzat totes les operacions
driver.quit()
