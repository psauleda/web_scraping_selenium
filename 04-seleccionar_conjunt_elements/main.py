# Seguint amb l'exemple anterior, (03-seleccionar...), i a la mateixa
# web, https://www.python.org/, volem seleccionar
# no un sol element com hem fet fins ara, sinó varis elements,
# (veure imatge adjunta) i un cop seleccionats els volem desar en un
# diccionari que contingui -> time: data, event: event.
# Comencem.
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
# Inspeccionem els elements que volem recuperar amb el navegador i observem
# que aquests elements estan a dins de:
# <div class ="medium-widget event-widget last">
# i a dins d'una llista <ul class="menu">
# i cada línia és un <li> amb un <time> i un <a> a dins.
# Fins ara hem vist find_element(), ara usarem find_elements() en plural, pel
# qual tenim els mateixos selectors que hem fet servir fins ara, (veure documentació).
times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li time")
# Obtenim una llista que podem recòrrer amb un loop
print("DATES")
for time in times:
    print(time.text)
# Fem el mateix pels links:
print("EVENTS")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li a")
for event in events:
    print(event.text)
# Amb això hem recuperat el que voliem, ara ens queda crear un diccionari:
# Ho podem fer amb un loop però també amb un dict comprehension:
result = {f"event{n}":{"time": times[n].text, "name": events[n].text} for n in range(len(events))}
print(result)

# Tanquem el navegador manualment cop s'han realitzat totes les operacions
driver.quit()