from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import random

# Настройки подключения
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RZ8M820SRYL"
options.automation_name = "UiAutomator2"

# Подключаемся к Appium
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(3)

print("✅ Устройство подключено. Начинаем свайпы!")

# Функция свайпа
def swipe(direction="right"):
    start_x, end_x = (400, 1000) if direction == "right" else (1000, 400)
    start_y = end_y = 1200
    driver.swipe(start_x, start_y, end_x, end_y, 300)

# Делаем 10 случайных свайпов
for _ in range(10):
    swipe(random.choice(["right", "left"]))
    time.sleep(random.uniform(1, 2))

print("✅ Тест свайпа завершен.")
driver.quit()
