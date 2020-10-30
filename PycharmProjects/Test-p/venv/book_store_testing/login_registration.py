from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

print("===================================================================")
print("2 - Registration_login: регистрация аккаунта  (стр.95)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10) # вынесли повторяющуюся часть в переменную wait
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")

t = 5
driver.implicitly_wait(t) # говорим WebDriver искать каждый элемент в течение 5 секунд
print("---------/Реализовано неявное ожидание с помощью \"implicitly_wait\" в " + str(t) + "секунд - +")

# 2 - Нажмите на вкладку "My Account Menu"
MMA = driver.find_element_by_css_selector('#menu-item-50 a')
MMA.click()
print("3 - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 3 - В разделе "Register", введите email для регистрации
R_email = driver.find_element_by_css_selector('.register [type="email"]')
R_email.send_keys("1234@ya.ru")
print("3 - В разделе \"Register\" введен email \"1234@ya.ru\" - +")

# 4 - В разделе "Register", введите пароль для регистрации
#             составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
#             почту и пароль сохраните, потребуюутся в дальнейшем
R_pass = driver.find_element_by_css_selector('.register [type="password"]')
R_pass.send_keys("Qpoi90000123")
print("4 - В разделе \"Register\" введен пароль \"Qpoi90000123\" - +")

# 5 - Нажмите на кнопку "Register"
B_Register = driver.find_element_by_css_selector('.register [type="password"]')
B_Register.click()
print("5 - Было выполенно нажатие на кнопку \"Register\" - +")


print("")
print("===================================================================")
print("3 - Registration_login: логин в систему (стр.96)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")

# 2 - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("2 - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 3 - В разделе "Login", введите email для логина 		# данные можно взять из предыдущего теста
L_email = driver.find_element_by_css_selector('.login [type="text"]')
L_email.send_keys("1234@ya.ru")
print("3 - В разделе \"Login\" введен email \"1234@ya.ru\" - +")

# 4 - В разделе "Login", введите пароль для логина 	# данные можно взять из предыдущего теста
L_pass = driver.find_element_by_css_selector('.login [type="password"]')
L_pass.send_keys("Qpoi90000123")
print("4 - В разделе \"Register\" введен пароль \"Qpoi90000123\" - +")

# 5 - Нажмите на кнопку "Login"
B_Login = driver.find_element_by_css_selector('.login [type="submit"]')
B_Login.click()
print("5 - Было выполенно нажатие на кнопку \"Login\" - +")

# 6 - Добавьте проверку, что на странице есть элемент "Logout"
print("6 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 10 сек, что на странице есть элемент \"Logout\"")
wait10 = WebDriverWait(driver, 10)

try:
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a [text() = "Logout"]')))
    print("--------> На странице есть элемент \"Logout\" - +")
except Exception as e:
    e
    print("--------> На странице НЕТ элемента \"Logout\" !!!")

time.sleep(3)

driver.quit()