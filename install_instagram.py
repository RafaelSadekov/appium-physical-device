from appium.webdriver.common.appiumby import AppiumBy
from appium_helper import get_driver

import time
import subprocess

# Подключаемся к Google Play
driver = get_driver(app_package="com.android.vending", app_activity=".AssetBrowserActivity")

print("✅ Открыли Google Play, ищем кнопку 'Поиск'...")
# Ищем и нажимаем "Поиск"
search_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Поиск")')
search_button.click()
time.sleep(1)
print("✅ Ищем Поиск'.")
# Ищем поисковую строку "Поиск" и кликаем

search_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Поиск приложений и игр")')
search_button.click()
time.sleep(2)

# Вводим "Instagram"
search_input = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
search_input.send_keys("Instagram")
time.sleep(1)

# Нажимаем "Enter"
driver.press_keycode(66)  
time.sleep(5)

print("✅ Ищем кнопку 'Установить'.")

try:
    install_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Установить")')
    install_button.click()
    print("⏳ Устанавливаем Instagram, ждём появления кнопки 'Открыть'...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Открыть")'))
    )
except:
    print("⚠️ Instagram уже установлен!")

# Проверяем, появился ли Instagram
print("🔍 Проверяем, установлен ли Instagram...")
try:
    open_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Открыть")')
    open_button.click()
    print("✅ Instagram установлен и открыт!")
    time.sleep(5)
except:
    print("❌ Ошибка: Instagram не найден или не запустился, попробуй установить вручную.")

driver.quit()
