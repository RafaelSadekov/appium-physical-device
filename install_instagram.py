from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Настройки Appium
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RZ8M820SRYL"
options.automation_name = "UiAutomator2"
options.app_package = "com.android.vending"
options.app_activity = ".AssetBrowserActivity"

# Подключаемся к Appium
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(5)

print("✅ Открыли Google Play, ищем кнопку 'Поиск'...")

search_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Поиск")')
search_button.click()
time.sleep(1)

# Ищем поисковую строку "Поиск" и кликаем
search_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Поиск приложений и игр")')
search_button.click()
time.sleep(2)

print("✅ Поле поиска открыто, вводим 'Instagram'.")

# Вводим "Instagram" в поле поиска
search_input = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
search_input.send_keys("Instagram")
time.sleep(1)

# Нажимаем "Enter" для поиска
driver.press_keycode(66)  # 66 = ENTER
time.sleep(5)

print("✅ Ищем кнопку 'Установить'.")

# Нажимаем кнопку "Установить"
install_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Установить")')
install_button.click()
time.sleep(30)  # Ждём установку

print("✅ Instagram установлен!")
driver.quit()
