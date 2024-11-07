# En aquest exercici seleccionarem tres elements diferents, (veure imatges adjuntes)
# corresponents a la web de https://www.python.org/
# Partint de l'exemple anterior, (02-seleccio_elements), volem seleccionar
# l'input de cerca, (veure imatge adjunta No. 1)
# Importem selenium, en particular el webdriver.
from selenium import webdriver

# per seleccionar elements
from selenium.webdriver.common.by import By

# Opcions per mantenir el navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Creem un driver
driver = webdriver.Chrome(options=chrome_options)

# Obrim el navegador a la pagina que volem fer scraping,
# en aquest cas és https://www.python.org/
URL = "https://www.python.org/"
driver.get(URL)
driver.maximize_window()
# Veure documentació pels selectors que podem fer servir:
# https://www.selenium.dev/documentation/webdriver/elements/locators/
# En aquest cas en farem servir un que és molt útil a l'hora de treballar
# amb formularis i és, primer find_element() i després By.NAME.
# Inspeccionem l'element que volem recuperar amb el navegador i observem:
# <input id="id-search-field" name="q" type="search" role="textbox"
# class="search-field" placeholder="Search" value="" tabindex="1">
# Per tant:
search_input = driver.find_element(By.NAME, value="q")
# Això és un objecte de selenium:
print(search_input)
# Podem recuperar diferent informació:
# Tag:
print(search_input.tag_name)
# Algun dels atributs que té, e.g., placeholder,
print(search_input.get_attribute("placeholder"))

# Si volem seleccionar per exemple el botó de submit, inspeccionem i
# i observem que té un id="submit":
# <button type="submit" name="submit" id="submit" class="search-button"
# title="Submit this Search" tabindex="3">GO</button>
# Per tant, per seleccionar-lo:
button = driver.find_element(By.ID, value="submit")
# Podem recuperar diferents propietats:
print(button.size)
print(button.text)

# Com es pot veure de la documentació, tenim altres selectors.
# Considerem ara (veure imatge adjunta, No. 2), volem recuperar el
# link (marcat amb vermell a la imatge adjunta).
# Inspeccionem:
# <a href="https://docs.python.org">docs.python.org</a>
# És un link que no té cap identificador ni classe.
# Si seguim inspeccionant més amunt, veiem que està a dins d'un <p>
# més amunt veiem que està a dins d'un <div>:
# <div class="small-widget documentation-widget">
# Per tant podem usar la classe 'documentation-widget' per
# arribar al selector <a> que volem seleccionar i ho fem
# tal com es fa amb CSS, '.classe selector_interior':
doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# El seu contingut és:
print(doc_link.text)

# Considerem un altre exemple, en aquest cas ens podem trobar amb elements
# que són de difícil accés, una manera de solucionar-ho és amb l'XPATH.
# Volem seleccionar el link que es troba a baix de tot de la web,
# el que posa "Submit Website Bug", (veure imatge adjunta No. 3).
# Inspeccionem:
# <a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a>
# Amb el botó dret del ratolí cliquem a sobre d'aquesta etiqueta i seleccionem
# copiar XPATh i l'enganxem al seguent selector (vigilar que no hi hagi cometes):
bug = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
# El seu contingut és:
print(bug.text)

# Tanquem el navegador manualment cop s'han realitzat totes les operacions
driver.quit()