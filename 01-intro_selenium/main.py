# Fem servir com a navegador el Chrome
# Importem selenium, en particular el webdriver que és
# una guia pel navegador per fer tasques automàtiques
from selenium import webdriver

# Opcions per mantenir el navegador (Chrome) obert i
# que no es tanqui al finalitzar el programa
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Creem un driver, en aquest cas com hem dit usem el Chrome,
# però també el podem crear per altres navegadors si volem.
# Aquest driver el que fa és obrir el Chrome i fa la petició
# HTTP a través d'ell, de manera que no cal canviar la capçalera.
driver = webdriver.Chrome(options=chrome_options)

# Amb el mètode get() obrim el navegador a la pagina que li indiquem,
# per exemple, Amazon
URL = "https://www.uoc.edu/ca"
driver.get(URL)
# Maximitzem la finestra del navegador per tal siguin visibles tots els elements.
driver.maximize_window()
# Observem (veure imatge adjunta) que el navegador s'obre amb un missatge que diu:
# Un programari automatitzat està controlant Chrome.

# Tanquem el navegador manualment, si descomentem la següent línia el navegador es tanca
# un cop s'han realitzat totes les operacions
# driver.quit()
