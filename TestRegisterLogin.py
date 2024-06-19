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


# IR A: INGRESAR
signButton = driver.find_element(By.XPATH, '//*[@id="MenuContent"]/a[2]').click()
time.sleep(2)


# IR A: CREAR USURARIO/ REGISTRARSE
registerUser = driver.find_element(By.XPATH, '//*[@id="Catalog"]/a').click()


# INGRESAR DATOS PARA CREAR LA CUENTA

# DATOS PRINCIPALES (OBLIGATORIOS)
id = {"ID":"00"}


userID = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
userID.send_keys(id["ID"])
time.sleep(1)

userPassword_1 = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
userPassword_1.send_keys("Contraseña1")
time.sleep(1)

userPassword_2 = driver.find_element(By.CSS_SELECTOR, "input[name='repeatedPassword']")
userPassword_2.send_keys("Contraseña1")
time.sleep(1)

# DATOS SECUNDARIOS (OBLIGATORIOS)
userFirstname = driver.find_element(By.CSS_SELECTOR, "input[name='account.firstName']")
userFirstname.send_keys("Usuario")
time.sleep(1)

userLastname = driver.find_element(By.CSS_SELECTOR, "input[name='account.lastName']")
userLastname.send_keys("Test")
time.sleep(1)

userEmail = driver.find_element(By.CSS_SELECTOR, "input[name='account.email']")
userEmail.send_keys("usuario@mail.com")
time.sleep(1)

userPhone = driver.find_element(By.CSS_SELECTOR, "input[name='account.phone']")
userPhone.send_keys("123456789")
time.sleep(1)

userAddress_1 = driver.find_element(By.CSS_SELECTOR, "input[name='account.address1']")
userAddress_1.send_keys("Direccion 1")
time.sleep(1)

userAddress_2 = driver.find_element(By.CSS_SELECTOR, "input[name='account.address2']")
userAddress_2.send_keys("Direccion 2")
time.sleep(1)

userCity = driver.find_element(By.CSS_SELECTOR, "input[name='account.city']")
userCity.send_keys("Ciudad 1")
time.sleep(1)

userState = driver.find_element(By.CSS_SELECTOR, "input[name='account.state']")
userState.send_keys("Estado 1")
time.sleep(1)

userZip = driver.find_element(By.CSS_SELECTOR, "input[name='account.zip']")
userZip.send_keys("1234")
time.sleep(1)

userCountry = driver.find_element(By.CSS_SELECTOR, "input[name='account.country']")
userCountry.send_keys("País 1")
time.sleep(1)

# GUARDAR LA INFORMACION DEL REGISTRO/ CREAR LA CUENTA
safeData = driver.find_element(By.XPATH, '//*[@id="Catalog"]/form/input').click()
time.sleep(2)


# INICIAR SESIÓN
signButton = driver.find_element(By.XPATH, '//*[@id="MenuContent"]/a[2]').click()
time.sleep(1)

# CARGAR DATOS
userName = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
userName.send_keys(id["ID"])
time.sleep(2)

userPass = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
userPass.clear()
userPass.send_keys("Contraseña1")
time.sleep(1)

loginButton = driver.find_element(By.XPATH, '//*[@id="Catalog"]/form/input').click()
time.sleep(2)


# CERRAR LA PAGINA DESPUES DE 10 SEGUNDOS
time.sleep(10)
driver.quit()
