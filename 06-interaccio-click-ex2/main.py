# Seguim amb el segon exemple de clicar un enllaç.
# Recordem que estem a https://en.wikipedia.org/wiki/Main_Page
# Ara clicarem un enllaç fent servir un altre selector de selenium.
# (Veure imatge adjunta click-link.png)

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
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)
driver.maximize_window()

# Selenium té un selector per links més senzill, seleccionem el link pel text que conté.
# Considerem per exemple l'enllaç de la imatge adjunta 'Content portals'.
portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# i ara el cliquem
portals.click()
# Novament comprovem que anem a parar al lloc clicat amb selenium.
# Recordem que hem comentat la línia driver.quit() per poder observar el resultat del click.
# Tanquem el navegador manualment cop s'han realitzat totes les operacions
# driver.quit()