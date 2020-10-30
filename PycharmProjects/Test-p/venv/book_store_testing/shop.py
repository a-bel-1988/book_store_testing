from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import keyboard




# 1 - Откройте http://practice.automationtesting.in/
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 20) # вынесли повторяющуюся часть в переменную wait
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")

# 2 - Залогиньтесь
# 2.1 - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("2.1 - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 2.2 - В разделе "Login", введите email для логина       # данные можно взять из предыдущего теста
L_email = driver.find_element_by_css_selector('.login [type="text"]')
L_email.send_keys("1234@ya.ru")
print("2.2 - В разделе \"Login\" введен email \"1234@ya.ru\" - +")

# 2.3 - В разделе "Login", введите пароль для логина   # данные можно взять из предыдущего теста
L_pass = driver.find_element_by_css_selector('.login [type="password"]')
L_pass.send_keys("Qpoi90000123")
print("2.3 - В разделе \"Register\" введен пароль \"Qpoi90000123\" - +")

# 2.4 - Нажмите на кнопку "Login"
B_Login = driver.find_element_by_css_selector('.login [type="submit"]')
B_Login.click()
print("2.4 - Было выполенно нажатие на кнопку \"Login\" - +")

# 2.5 - Добавьте проверку, что на странице есть элемент "Logout"
print("2.5 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 10 сек, что на странице есть элемент \"Logout\"")
wait10 = WebDriverWait(driver, 10)

try:
    element = wait10.until(EC.presence_of_element_located((By.XPATH, '//a [text() = "Logout"]')))
    print("--------> На странице есть элемент \"Logout\" - +")
except Exception as e:
    e
    print("--------> На странице НЕТ элемента \"Logout\" !!!")

# 3 - Нажмите на вкладку "Shop"
M_Shop = driver.find_element_by_css_selector('#menu-item-40 a')
M_Shop.click()
print("3 - Был выполнен переход на вкладку \"Shop\" - +")
time.sleep(2)
# 4 - Откройте книгу "HTML 5 Forms"
A_H5F = driver.find_element_by_xpath('//h3[text() = "HTML5 Forms"]')
A_H5F.click()
print("4 - Открыта книга \"HTML 5 Forms\" - +")
time.sleep(2)
# 5 - Добавьте тест, что заголовок книги называется: "HTML5 Forms"
print("6 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 10 сек, что на странице есть заголовок \"HTML5 Forms\"")
wait10 = WebDriverWait(driver, 10)

try:
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//h1[text() = "HTML5 Forms"]')))
    print("--------> На странице есть заголовок \"HTML5 Forms\" - +")
except Exception as e:
    e
    print("--------> На странице НЕТ элемента \"HTML5 Forms\" !!!")
time.sleep(1)

print("")
print("--------------------------------------------------------------------")

# 00.1 - Выполняем выход из ЛК - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("00.1 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 00.2 - Нажать на элемент "Logout"
LK_Logout = driver.find_element_by_css_selector('[class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"] a')
LK_Logout.click()
print("00.2 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"Logout\" - +")

time.sleep(2)

print("")
print("===================================================================")
print("5 - Shop: количество товаров в категории (стр.98)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")

# 2 - Залогиньтесь
# 2.1 - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("2.1 - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 2.2 - В разделе "Login", введите email для логина       # данные можно взять из предыдущего теста
L_email = driver.find_element_by_css_selector('.login [type="text"]')
L_email.send_keys("1234@ya.ru")
print("2.2 - В разделе \"Login\" введен email \"1234@ya.ru\" - +")

# 2.3 - В разделе "Login", введите пароль для логина   # данные можно взять из предыдущего теста
L_pass = driver.find_element_by_css_selector('.login [type="password"]')
L_pass.send_keys("Qpoi90000123")
print("2.3 - В разделе \"Register\" введен пароль \"Qpoi90000123\" - +")

# 2.4 - Нажмите на кнопку "Login"
B_Login = driver.find_element_by_css_selector('.login [type="submit"]')
B_Login.click()
print("2.4 - Было выполенно нажатие на кнопку \"Login\" - +")

# 2.5 - Добавьте проверку, что на странице есть элемент "Logout"
print("2.5 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 10 сек, что на странице есть элемент \"Logout\"")
wait10 = WebDriverWait(driver, 10)

try:
    element = wait10.until(EC.presence_of_element_located((By.XPATH, '//a [text() = "Logout"]')))
    print("--------> На странице есть элемент \"Logout\" - +")
except Exception as e:
    e
    print("--------> На странице НЕТ элемента \"Logout\" !!!")

# 3 - На-жмите на вкладку "Shop"
M_Shop = driver.find_element_by_css_selector('#menu-item-40 a')
M_Shop.click()
print("3 - Был выполнен переход на вкладку \"Shop\" - +")
time.sleep(2)

# 4 - Откройте категорию "HTML"
A_HTML = driver.find_element_by_css_selector('[class="cat-item cat-item-19"] a')
A_HTML.click()
print("4 - Был выполенен переход в категорию \"HTML\" - +")

# 5 - Добавьте тест, что отображается три товара
M_Count = driver.find_element_by_css_selector('[class="cat-item cat-item-19 current-cat"] [class="count"]')
M_CT = M_Count.text
print("5.1 - В категории \"HTML\" стоит что есть " + M_CT + " товара")

e=0
for N in range(1, 200):
    #k2 = "#personal_cmbNation [value=" + "\"" + str(N) + "\"]"
    k2 = "[class='products masonry-done'] li:nth-child(" + str(N) + ")"
    try:
        Tovar = driver.find_element_by_css_selector(k2)
    except Exception as e:
        break

print("5.2 - Фактическое кол-во показаных товаров = " + str(N - 1))

print("")
print("--------------------------------------------------------------------")

# 00.1 - Выполняем выход из ЛК - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("00.1 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 00.2 - Нажать на элемент "Logout"
LK_Logout = driver.find_element_by_css_selector('[class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"] a')
LK_Logout.click()
print("00.2 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"Logout\" - +")

print("")
print("===================================================================")
print("6- Shop: сортировка товаров (стр.99)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")

# 2 - Залогиньтесь
# 2.1 - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("2.1 - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 2.2 - В разделе "Login", введите email для логина       # данные можно взять из предыдущего теста
L_email = driver.find_element_by_css_selector('.login [type="text"]')
L_email.send_keys("1234@ya.ru")
print("2.2 - В разделе \"Login\" введен email \"1234@ya.ru\" - +")

# 2.3 - В разделе "Login", введите пароль для логина   # данные можно взять из предыдущего теста
L_pass = driver.find_element_by_css_selector('.login [type="password"]')
L_pass.send_keys("Qpoi90000123")
print("2.3 - В разделе \"Register\" введен пароль \"Qpoi90000123\" - +")

# 2.4 - Нажмите на кнопку "Login"
B_Login = driver.find_element_by_css_selector('.login [type="submit"]')
B_Login.click()
print("2.4 - Было выполенно нажатие на кнопку \"Login\" - +")

# 2.5 - Добавьте проверку, что на странице есть элемент "Logout"
print("2.5 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 10 сек, что на странице есть элемент \"Logout\"")
wait10 = WebDriverWait(driver, 10)

try:
    element = wait10.until(EC.presence_of_element_located((By.XPATH, '//a [text() = "Logout"]')))
    print("--------> На странице есть элемент \"Logout\" - +")
except Exception as e:
    e
    print("--------> На странице НЕТ элемента \"Logout\" !!!")

# 3 - На-жмите на вкладку "Shop"
M_Shop = driver.find_element_by_css_selector('#menu-item-40 a')
M_Shop.click()
print("3 - Был выполнен переход на вкладку \"Shop\" - +")
time.sleep(2)

# 4 - Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
#     Используйте проверку по value
element = driver.find_element_by_css_selector('[selected="selected"]')
E_txt = element.text

if E_txt == "Sort by price: high to low":
    print("4 - В селекторе выбрана сортировка: \"high to low\" - +")
else:
    print("4 - В селекторе выбрана сортировка: " + "\"" + E_txt + "\" !!!")

# 5 - Отсортируйте товары от большего к меньшему
#     в селекторах используйте класс Select
S_Pr_desc = driver.find_element_by_css_selector('[name="orderby"]')
select = Select(S_Pr_desc)
select.select_by_value("price-desc")
print("5 - Выбран метод сортировки: \"high to low\"  - +")

# 6 - Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
element = driver.find_element_by_css_selector('[selected="selected"]')
print("6 - Обьявлена переменнуя с локатором основного селектора сортировки - +")

# 7 - Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
#     Используйте проверку по value
E_txt = element.text

if E_txt == "Sort by price: high to low":
    print("7 - В селекторе выбрана сортировка: \"high to low\" - +")
else:
    print("7 - В селекторе выбрана сортировка: " + "\"" + E_txt + "\" !!!")

print("")
print("--------------------------------------------------------------------")

# 00.1 - Выполняем выход из ЛК - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("00.1 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 00.2 - Нажать на элемент "Logout"
LK_Logout = driver.find_element_by_css_selector('[class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"] a')
LK_Logout.click()
print("00.2 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"Logout\" - +")

print("")
print("===================================================================")
print("7- Shop: отображение, скидка товара (стр.100)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")

# 2 - Залогиньтесь
# 2.1 - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("2.1 - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 2.2 - В разделе "Login", введите email для логина       # данные можно взять из предыдущего теста
L_email = driver.find_element_by_css_selector('[id="username"]')
L_email.send_keys("1234@ya.ru")
print("2.2 - В разделе \"Login\" введен email \"1234@ya.ru\" - +")

# 2.3 - В разделе "Login", введите пароль для логина   # данные можно взять из предыдущего теста
L_pass = driver.find_element_by_css_selector('.login [type="password"]')
L_pass.send_keys("Qpoi90000123")
print("2.3 - В разделе \"Register\" введен пароль \"Qpoi90000123\" - +")

# 2.4 - Нажмите на кнопку "Login"
B_Login = driver.find_element_by_css_selector('.login [type="submit"]')
B_Login.click()
print("2.4 - Было выполенно нажатие на кнопку \"Login\" - +")

# 2.5 - Добавьте проверку, что на странице есть элемент "Logout"
print("2.5 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 10 сек, что на странице есть элемент \"Logout\"")
wait10 = WebDriverWait(driver, 10)

try:
    element = wait10.until(EC.presence_of_element_located((By.XPATH, '//a [text() = "Logout"]')))
    print("--------> На странице есть элемент \"Logout\" - +")
except Exception as e:
    e
    print("--------> На странице НЕТ элемента \"Logout\" !!!")

# 3 - На-жмите на вкладку "Shop"
M_Shop = driver.find_element_by_css_selector('#menu-item-40 a')
M_Shop.click()
print("3 - Был выполнен переход на вкладку \"Shop\" - +")
time.sleep(2)

# 4 - Откройте книгу "Android Quick Start Guide"
AQSG = driver.find_element_by_css_selector('[class="products masonry-done"] h3')
AQSG.click()
print("4 - Открыта книга \"Android Quick Start Guide\" - +")

# 5 - Добавьте тест, что содержимое старой цены = "₹600.00"    # используйте assert
element2 = driver.find_element_by_css_selector(".price del")
element_get_text = element2.text         # получили текст элемента с помощью .text
try:
    assert str(element_get_text) == "₹600.00"  # добавили проверку что содержимое равно ожидаемому
    print("5 - Cодержимое старой цены = ₹600.00 - +")
except Exception as e:
    e
    print("5 - Cодержимое старой цены = ₹" + str(element_get_text) + " !!!")

# 6 - Добавьте тест, что содержимое новой цены = "₹450.00"    # используйте assert
element2 = driver.find_element_by_css_selector('.price ins [class="woocommerce-Price-amount amount"]') # нашли элемент по составному селектору
element_get_text2 = element2.text         # получили текст элемента с помощью .text
try:
    assert str(element_get_text2) == "₹450.00"  # добавили проверку что содержимое равно ожидаемому
    print("6 - Cодержимое новой цены = ₹450.00 - +")
except Exception as e:
    e
    print("6 - Cодержимое новой цены = ₹" + str(element_get_text2) + " !!!")

# 7 - Добавьте явное ожидание и нажмите на обложку книги
#     Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
A_Obl = driver.find_element_by_css_selector('.images')
A_Obl.click()
print("7 - Выполненно нажатие на обложку книги - +")
print("7.1 - Добавленно явное ожидание 4 секунды - +")
time.sleep(4)

# 8 - Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
B_krest = driver.find_element_by_css_selector('.pp_close')
B_krest.click()
print("8 - Выполненно нажатие на крестик - +")

print("")
print("--------------------------------------------------------------------")

# 00.1 - Выполняем выход из ЛК - Нажмите на вкладку "My Account Menu"
MMA_2 = driver.find_element_by_css_selector('#menu-item-50 a')
MMA_2.click()
print("00.1 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"My Account Menu\" - +")

# 00.2 - Нажать на элемент "Logout"
LK_Logout = driver.find_element_by_css_selector('[class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"] a')
LK_Logout.click()
print("00.2 - Выполняеется выход из ЛК - Выполненно нажатие на вкладку \"Logout\" - +")

print("")
print("===================================================================")
print("8 - Shop: проверка цены в корзине (стр.101)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")
#driver.implicitly_wait(10) # говорим WebDriver искать каждый элемент в течение 5 секунд

# 2 - Нажмите на вкладку "Shop"
M_Shop = driver.find_element_by_css_selector("#menu-item-40 a")
M_Shop.click()
print("2 - Был выполнен переход на вкладку \"Shop\" - +")

# 3 - Добавьте в корзину книгу "HTML5 WebApp Development"
B_HTML5 = driver.find_element_by_css_selector('[data-product_id="182"]')
B_HTML5.click()
print("3 - Добавили в корзину книгу \"HTML5 WebApp Development\" - +")
time.sleep(5)

# 4 - Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
#     Используйте для проверки assert
Prov = driver.find_element_by_css_selector('[class="cartcontents"]')
pr = Prov.text
assert pr == "1 Item"
print("4.1 - Вверху справа количество товаров = \"1 item\" - +")

Prov2 = driver.find_element_by_css_selector('[class="amount"]')
pr2 = Prov2.text
assert pr2 == "₹180.00"
print("4.2 - Вверху справа стоимость = \"₹180.00\" - +")

# 5 - Перейдите в корзину
Basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]').click()
print("5 - Выполнен переход в корзину - +")
time.sleep(5)

# 6 - Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
Subtotal = driver.find_element_by_css_selector('[data-title="Subtotal"] span')
Sub = Subtotal.text
assert Sub != ""
print("6 - В Subtotal отобразилась стоимость - +")

if Sub == pr2:
    print("6.1 - В Subtotal стоимость = стоимости вверху справа - +")
else:
    print("6.1 - В Subtotal стоимость != стоимости вверху справа !!!")



print("")
print("--------------------------------------------------------------------")
print("-------------Выполняется удаление добаленных товаров----------------")
time.sleep(5)

# 000 - Перейдите в корзину
Basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
time.sleep(2)
Basket.click()
print("000 - Выполнен переход в корзину - +")
time.sleep(2)

for N in range(1, 200):
    try:
        M_krest2 = driver.find_element_by_css_selector('[class ="product-name"] a')
        M_krest2_txt = M_krest2.text
        M_krest = driver.find_element_by_css_selector('[class="cart_item"] [class="product-remove"] a')
        M_krest.click()
        print("000-"+ str(N)+ " - Выполненно удаление товара \"" + str(M_krest2_txt) +"\" - +")

        time.sleep(4)


    except Exception as e:
        break




print("")
print("===================================================================")
print("9- Shop: работа в корзине (стр.102)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")
driver.implicitly_wait(10) # говорим WebDriver искать каждый элемент в течение 5 секунд

driver.implicitly_wait(20)

# 2 - Нажмите на вкладку "Shop"
M_Shop = driver.find_element_by_css_selector('#menu-item-40 a')
M_Shop.click()
print("2 - Был выполнен переход на вкладку \"Shop\" - +")

# 3 - Добавьте в корзину книгу "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
#     Перед добавлением первой книги, проскролльте вниз на 300 пикселей
#     После добавления 1-й книги добавьте sleep
B_HTML5 = driver.find_element_by_css_selector('[data-product_id="182"]')
B_HTML5.click()
print("3.1 - Добавили в корзину книгу \"HTML5 WebApp Development\" - +")

time.sleep(4)

JSD = driver.find_element_by_css_selector('[data-product_id="180"]')
JSD.click()
print("3.2 - Добавили в корзину книгу \"JS Data Structures and Algorithm\" - +")

#time.sleep(10)

# 4 - Перейдите в корзину
Basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
Basket.click()
print("4 - Выполнен переход в корзину - +")
#time.sleep(10)

# 5 - Удалите первую книгу
#     Перед удалением добавьте sleep
B_del = driver.find_element_by_css_selector('[class="product-remove"] a')
B_del.click()
print("5 - Удалена первая книга - +")

# 6 - Нажмите на Undo (отмена удаления)
#time.sleep(10)
B_undo = driver.find_element_by_css_selector('[class="woocommerce-message"] a')
B_undo.click()
print("6 - Нажата кнопка \"Undo?\" - +")

# 7 - В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
#     Предварительно очистите поле с помощью локатор_поля.clear()
B_plus = driver.find_element_by_css_selector('[class="cart_item"]:nth-child(2) input')
B_plus.clear()
B_plus.send_keys("3")
print("7 - Увеличили кол-во товара до 3 шт. - +")

# 8 - Нажмите на кнопку "UPDATE BASKET"
B_upb = driver.find_element_by_css_selector('[name="update_cart"]')
B_upb.click()
print("8 - Нажата кнопка \"Update Basket\" - +")

# 9 - Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
#       используйте assert
B_prov = driver.find_element_by_css_selector('[class="cart_item"]:nth-child(2) input')
B_pr = B_prov.get_attribute("value")
assert str(B_pr) == "3"
print("9 -  Value элемента quantity для \"JS Data Structures and Algorithm\" равно 3 - +")

# 10 - Нажмите на кнопку "APPLY COUPON"
#      Перед нажатимем добавьте sleep
time.sleep(5)
B_AC = driver.find_element_by_css_selector('[name="apply_coupon"]').click()
print("10 -  Нажмита кнопка \"APPLY COUPON\" - +")

# 11 - Добавьте тест, что возникло сообщение: "Please enter a coupon code."
B_pecc = driver.find_element_by_xpath('//li [text()="Please enter a coupon code."]')

if B_pecc is not None:
    print("Возникло сообщение: \"Please enter a coupon code.\" - +")
else:
    print("НЕ возникло сообщение: \"Please enter a coupon code.\" !!!")

print("")
print("--------------------------------------------------------------------")
print("-------------Выполняется удаление добаленных товаров----------------")
time.sleep(5)

# 000 - Перейдите в корзину
Basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
time.sleep(2)
Basket.click()
print("000 - Выполнен переход в корзину - +")
time.sleep(2)

for N in range(1, 200):
    try:
        M_krest2 = driver.find_element_by_css_selector('[class ="product-name"] a')
        M_krest2_txt = M_krest2.text
        M_krest = driver.find_element_by_css_selector('[class="cart_item"] [class="product-remove"] a')
        M_krest.click()
        print("000-"+ str(N)+ " - Выполненно удаление товара \"" + str(M_krest2_txt) +"\" - +")

        time.sleep(4)


    except Exception as e:
        break

print("")
print("===================================================================")
print("10- Shop: покупка товара (стр.103)")
print("===================================================================")

# 1 - Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
print("1 - Открылась страница: http://practice.automationtesting.in/ - +")
#driver.implicitly_wait(10)

#driver.implicitly_wait(20) # говорим WebDriver искать каждый элемент в течение 20 секунд

# 2 - Нажмите на вкладку "Shop"
M_Shop = driver.find_element_by_css_selector('#menu-item-40 a')
M_Shop.click()
print("2 - Был выполнен переход на вкладку \"Shop\" - +")
time.sleep(5)

# 3 - Добавьте в корзину книгу "HTML5 WebApp Development"
B_HTML5 = driver.find_element_by_css_selector('[data-product_id="182"]')
B_HTML5.click()
print("3.1 - Добавили в корзину книгу \"HTML5 WebApp Development\" - +")

# 4 - Перейдите в корзину
Basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
#time.sleep(5)
Basket.click()
print("4 - Выполнен переход в корзину - +")

# 5 - Нажмите "PROCEED TO CHECKOUT"
#     Перед нажатием, добавьте явное ожидание
B_ptc = driver.find_element_by_css_selector('[class="wc-proceed-to-checkout"] a')
time.sleep(5)
B_ptc.click()
print("5 - Выполненно нажатие на кнопку \"PROCEED TO CHECKOUT\" - +")

# 6 - Заполните все обязательные поля
#     Перед заполнением first name, добавьте явное ожидание
#     Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
#     Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку                  нажмите на неё, затем на вариант в списке ниже
T_first_n_txt = "Anton"
T_last_n_txt = "Belyaev"
T_mail_txt = "1234@ya.ru"
T_phone_txt = "89635647235"
T_Country_txt = "Russia"
T_Address_txt = "st.Lenina 45"
T_Town_City_txt = "St.Peterburg"
T_State_Country_txt = "St.Peterburg"
T_postcode_txt = "124566"

time.sleep(5)
T_first_n = driver.find_element_by_css_selector('[id="billing_first_name"]')
T_first_n.send_keys(T_first_n_txt)
print("6.1 - Заполненно поле \"first name\" = \"" + T_first_n_txt + "\" - +")

T_last_n = driver.find_element_by_css_selector('[id="billing_last_name"]')
T_last_n.send_keys(T_last_n_txt)
print("6.2 - Заполненно поле \"last name\" = \"" + str(T_last_n_txt) + "\" - +")

T_mail = driver.find_element_by_css_selector('[id="billing_email"]')
T_mail.send_keys(T_mail_txt)
print("6.3 - Заполненно поле \"email\" = \"" + str(T_mail_txt) + "\" - +")

T_phone = driver.find_element_by_css_selector('[id="billing_phone"]')
T_phone.send_keys(T_phone_txt)
print("6.4 - Заполненно поле \"phone\" = \"" + str(T_phone_txt) + "\" - +")

T_Country = driver.find_element_by_css_selector('[id="s2id_billing_country"]')
T_Country.click()

time.sleep(5)

T_Country2 = driver.find_element_by_css_selector('[id="s2id_autogen1_search"]')
T_Country2.send_keys(T_Country_txt)
time.sleep(2)

keyboard.press('Enter')
print("6.5 - Заполненно поле \"Country\" = \"" + str(T_Country_txt) + "\" - +")

T_Address = driver.find_element_by_css_selector('[id="billing_address_1"]')
T_Address.send_keys(T_Address_txt)
print("6.6 - Заполненно поле \"Address\" = \"" + str(T_Address_txt) + "\" - +")

T_Town_City = driver.find_element_by_css_selector('[id="billing_city"]')
T_Town_City.send_keys(T_Town_City_txt)
print("6.7 - Заполненно поле \"State/County\" = \"" + str(T_Town_City_txt) + "\" - +")

T_State_Country = driver.find_element_by_css_selector('[id="billing_state"]')
T_State_Country.send_keys(T_State_Country_txt)
print("6.8 - Заполненно поле \"State/Country\" = \"" + str(T_State_Country_txt) + "\" - +")

T_postcode = driver.find_element_by_css_selector('[id="billing_postcode"]')
T_postcode.send_keys(T_postcode_txt)
print("6.9 - Заполненно поле \"State/Country\" = \"" + str(T_postcode_txt) + "\" - +")

# 7 - Выберите способ оплаты "Check Payments"
#     Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
N = 600
driver.execute_script("window.scrollBy(0,"+ str(N) +");")  # эта команда проскроллит страницу на N пикселей вниз
print("7.1 - Проскролили страницу на "+ str(N) +" пикселей - +")

RB_Check_Payments = driver.find_element_by_css_selector('input[id="payment_method_cheque"]')
driver.execute_script("return arguments[0].scrollIntoView(true);", RB_Check_Payments)	 # автоматически проскроллили до зоны видимости кнопки
RB_Check_Payments.click()
print("7.2 - Выбран способ оплаты - \"Check Payments\" - +")
time.sleep(3)

# 8 - Нажмите PLACE ORDER
B_PLACE_ORDER = driver.find_element_by_css_selector('[id="place_order"]')
B_PLACE_ORDER.click()
print("8 - Выполненно нажатие на кнопку - \"PLACE ORDER\" - +")

# 9 - Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
time.sleep(10)

wait10 = WebDriverWait(driver, 20).until
print("9 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 20 сек, что на странице есть элемент \"Thank you. Your order has been received.\"")
try:
    element = wait10(EC.presence_of_element_located((By.XPATH, '//p [text() = "Thank you. Your order has been received."]')))
    print("--------> На странице есть элемент \"Thank you. Your order has been received.\" - +")
except Exception as e:

    e
    print("--------> На странице НЕТ элемента \"Thank you. Your order has been received.\" !!!")

# 10 - Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"

print("10 - Выполняем проверку с помощью \"presence_of_element_located\" с задержкой 20 сек, что в Payment Method отображается текст \"Check Payments\"")
try:
    element = wait10(EC.presence_of_element_located((By.XPATH, '//strong [text() = "Check Payments"]')))
    print("--------> в Payment Method отображается текст \"Check Payments\" - +")
except Exception as e:
    e
    print("--------> в Payment Method НЕ отображается текст \"Check Payments\" !!!")

time.sleep(5)

driver.quit()
