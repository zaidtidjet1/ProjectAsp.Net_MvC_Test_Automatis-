import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service



driver =webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://localhost:5281/")
# 1 test acueil
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/nav/div/button[1]').click()
time.sleep(2)
# 2 test A propos
driver.find_element(By.XPATH, '/html/body/nav[1]/div/button[2]').click()
time.sleep(2)

# 3 test prndre Rendez vous
#driver.find_element(By.XPATH, '/html/body/div[1]/button').click()
#driver.find_element(By.ID, 'prenom').send_keys('allo')
#driver.find_element(By.ID, 'nom').send_keys('allo')
#driver.find_element(By.ID, 'sexe').send_keys('Homme')
#driver.find_element(By.ID, 'ville').send_keys('Rimouski')
#driver.find_element(By.ID, 'dob').send_keys("002020-12-12")

#driver.find_element(By.ID, 'email').send_keys('allo@gmail.com')
#driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/button[1]').click()

time.sleep(3)

# 4 test Professionnel de santé
driver.find_element(By.XPATH, '/html/body/nav[1]/div/button[3]').click()

# 5 test cliquer sur le botton conexion dans professionel de sante
driver.find_element(By.XPATH, '/html/body/div[1]/button').click()

# 6 test création d'un compte
#driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/form/button[2]').click()
#driver.find_element(By.ID, 'prenom').send_keys('allo')
#driver.find_element(By.ID, 'nom').send_keys('allo')
#driver.find_element(By.ID, 'Spec').send_keys('Cardiologue')
#driver.find_element(By.ID, 'sexe').send_keys('Homme')
#driver.find_element(By.ID, 'ville').send_keys('Montréal')
#driver.find_element(By.ID, 'dob').send_keys('001995-07-05')
#driver.find_element(By.ID, 'email').send_keys('allo@allo.com')
#driver.find_element(By.ID, 'password').send_keys('Zaid1995@')
#driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/form/button[1]').click()
#time.sleep(3)

# 7 test Connexion

#driver.find_element(By.ID, 'username').send_keys('allo@allo.com')
#driver.find_element(By.ID, 'pwd').send_keys('Zaid1995@')
#driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/form/button[1]').click()
#time.sleep(2)



# 8 test Nous joindre et aide

#driver.find_element(By.XPATH, '/html/body/nav[1]/div/button[4]').click()
#time.sleep(2)
#driver.find_element(By.XPATH, '/html/body/div[1]/button[1]').click()
#time.sleep(2)
#driver.find_element(By.XPATH,'/html/body/div[1]/button[2]').click()

# 9 test chercher un medecin

driver.find_element(By.XPATH, '/html/body/nav/div/button[5]').click()
driver.find_element(By.ID, 'fName').send_keys('Zaid')
driver.find_element(By.ID, 'LName').send_keys('Tidjet')
driver.find_element(By.ID, 'spec').send_keys('Cardiologue')
driver.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[4]/button').click()

time.sleep(5)


