# Aquesta és potser la part més interessant de l'scraping amb selenium.
# Volem interaccionar amb la web de la wikipedia:
# https://en.wikipedia.org/wiki/Main_Page
# El primer que farem és clicar un enllaç, en particular l'enllaç del nombre d'articles.
# (Veure imatge adjunta click_num_articles.png)

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
# Inspeccionem l'element que volem recuperar amb el navegador:
# <a href="/wiki/Special:Statistics" title="Special:Statistics">6,897,451</a>
# És a dins d'un <div id="articlecount>, recuperem el primer <a>:
comptador = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# Fem click a l'element seleccionat (comentem diver.quit() per poder veure el resultat)
comptador.click()
# Es comprova que efectivament anem aparar a l'enllaç que apunta el comptador.
# Tanquem el navegador manualment cop s'han realitzat totes les operacions
# driver.quit()