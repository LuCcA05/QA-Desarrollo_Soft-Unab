from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# CONFIGURAR LAS OPCIONES DE CHROME (NOTIFICACIONES)
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2,  # Desactivar notificaciones
    "profile.password_manager_enabled": False,  # Desactivar el administrador de contraseñas
    "autofill.profile_enabled": False,  # Desactivar autocompletar perfiles
    "autofill.address_enabled": False,  # Desactivar autocompletar direcciones
}
chrome_options.add_experimental_option("prefs", prefs)


# INICIAR EL WEBDRIVER CON LAS OPCIONES CONFIGURADAS
driver = webdriver.Chrome(options=chrome_options)


# NAVEGAR A LA PAGINA WEB
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
time.sleep(5)
    

# BÚSCAR Y AGREGAR PRODUCTOS AL CARRITO
# BÚSCAR PERRO (GOLDEN)
keyword = driver.find_element(By.CSS_SELECTOR, "input[name='keyword']")
keyword.clear()
keyword.send_keys("Chihuahua")
time.sleep(2)

search = driver.find_element(By.CSS_SELECTOR, "input[name='searchProducts']").click()
time.sleep(2)


dog_main = driver.find_element(By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[2]/td[1]/a/img').click()
time.sleep(2)

dog_select = driver.find_element(By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[3]/td[5]/a').click()
time.sleep(2)

# BÚSCAR GATO (PERSIAN)
keyword = driver.find_element(By.CSS_SELECTOR, "input[name='keyword']")
keyword.clear()
keyword.send_keys("Persian")
time.sleep(2)

search = driver.find_element(By.CSS_SELECTOR, "input[name='searchProducts']").click()
time.sleep(2)

cat_main = driver.find_element(By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[2]/td[1]/a/img').click()
time.sleep(2)

cat_select = driver.find_element(By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[2]/td[5]/a').click()
time.sleep(2)

# BÚSCAR PEZ (GOLDENFISH)
keyword = driver.find_element(By.CSS_SELECTOR, "input[name='keyword']")
keyword.clear()
keyword.send_keys("Goldfish")
time.sleep(2)

search = driver.find_element(By.CSS_SELECTOR, "input[name='searchProducts']").click()
time.sleep(2)

fish_main = driver.find_element(By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[2]/td[1]/a/img').click()
time.sleep(2)

fish_select = driver.find_element(By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[3]/td[5]/a').click()
time.sleep(2)

checkout = driver.find_element(By.XPATH, '//*[@id="Cart"]/a').click()
time.sleep(2)

# CARGAR DATOS (LOGIN)
id = {"ID":"000001"}

userName = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
userName.clear()
userName.send_keys(id["ID"])
time.sleep(2)

userPass = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
userPass.clear()
userPass.send_keys("Contraseña1")
time.sleep(1)

loginButton = driver.find_element(By.XPATH, '//*[@id="Catalog"]/form/input').click()
time.sleep(2)


# VOLVER AL CARRITO
cart_button = driver.find_element(By.CSS_SELECTOR, "img[name='img_cart']").click()
time.sleep(2)

# CONTINUAR CON LA COMPRA
checkout = driver.find_element(By.XPATH, '//*[@id="Cart"]/a').click()
time.sleep(2)

continue_1 = driver.find_element(By.CSS_SELECTOR, "input[name='newOrder']").click()
time.sleep(2)

continue_2 = driver.find_element(By.XPATH, '//*[@id="Catalog"]/a').click()
time.sleep(5)

# VOLVER AL INICIO DESPUES DE COMPRAR
return_ = driver.find_element(By.XPATH, '//*[@id="BackLink"]/a').click()
time.sleep(2)

time.sleep(10)
driver.quit()


