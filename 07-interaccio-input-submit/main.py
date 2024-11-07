# Seguim a https://en.wikipedia.org/wiki/Main_Page
# Volem volem omplir un input de text i volem clicar el botó d'enviar la consulta.
# Això ens servirà per exemple per omplir i enviar formularis.
# Tal com podem veure a la imatge adjunta (interaccio-input-submit.png), seleccionarem
# l'input de search, l'omplirem amb un text i clicarem el botó search.

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

# Volem omplir l'input i clicar el botó de Search (veure imatge adjunta).
# Inspeccionem l'element que volem recuperar amb el navegador:
# Tenim un <form id="searchform" ....>
# A dins: <input ... name="search" ...> i un <button ...>
search_input = driver.find_element(By.NAME, value="search")
# Omplim l'input amb text
search_input.send_keys("Scraping")
# Seleccionem i cliquem el botó de search
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
print(submit.text)
submit.click()
# Observem que el resultat és que anem a parar a la web de la que hem demanat informació.
# Novament tenim comentada la següent línia per evitar que es tanqui el chrome.
# Tanquem el navegador manualment cop s'han realitzat totes les operacions
# driver.quit()