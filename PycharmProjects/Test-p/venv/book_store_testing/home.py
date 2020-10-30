
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

print("===================================================================")
print("1 - Home: добавление комментария (стр.94)")
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

# 2 - Проскролльте страницу вниз на 600 пикселей
N = 600
driver.execute_script("window.scrollBy(0,"+ str(N) +");")  # эта команда проскроллит страницу на N пикселей вниз
print("2 - Проскролили страницу на "+ str(N) +" пикселей - +")

# 3 - Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
ASR = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 h3')
ASR.click()
print("3 - Выполненно нажатие на название книги \"Selenium Ruby\" - +")

# 4 - Нажмите на вкладку "REVIEWS"
ARV = driver.find_element_by_css_selector('.reviews_tab a')
ARV.click()
print("4 - Выполненно нажатие на вкладку \"REVIEWS\" - +")

# 5 - Поставьте 5 звёзд
S5 = driver.find_element_by_css_selector('.star-5')
S5.click()
print("5 - Было выбрано 5 звезд - +")

# 6 - Заполните поле "Review" сообщением: "Nice book!"
Coment = driver.find_element_by_css_selector('#comment')
Coment.send_keys("Nice book!")
print("6 - Заполнен комментарий \"Nice book!\" - +")

# 7 - Заполните поле "Name"
Pname = driver.find_element_by_css_selector('#author')
Pname.send_keys("Anton")
print("7 - Заполненно поле \"Name\" = \"Anton\" - +")

# 8 - Заполните "Email"
Pname = driver.find_element_by_css_selector('#email')
Pname.send_keys("1234@ya.ru")
print("8 - Заполненно поле \"Email\" = \"1234@ya.ru\" - +")

# 9 - Нажмите на кнопку "SUBMIT"
BSUB = driver.find_element_by_css_selector('[name="submit"]')
BSUB.click()
print("9 - Выполенно нажатие на кнопку \"SUBMIT\" - +")

driver.quit()