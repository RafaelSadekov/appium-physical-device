from appium_helper import get_driver
from appium.webdriver.common.appiumby import AppiumBy
import time

# Открываем Twinby
driver = get_driver(app_package="com.twinby", app_activity=".MainActivity", no_reset=True)

time.sleep(15)

# Проверяем, действительно ли приложение открылось
current_activity = driver.current_activity
if current_activity != ".MainActivity":
    print(f"⚠️ Ошибка: приложение не открылось, текущая активность: {current_activity}")
    driver.quit()
    exit()

print("✅ Twinby открыт, анализируем профиль...")

def analyze_profile():
    try:
        name, age, compatibility, profile_text = "Unknown", 0, 0, "Unknown"

        # Получаем описание (имя и возраст)
        try:
            description_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").index(5)')
            description = description_element.get_attribute("content-desc").strip()
            
            if description:
                name, age = description.split(", ")
                age = int(age)
        except:
            print("⚠️ Не удалось получить имя и возраст")

        # Получаем текст профиля (описание, интересы)
        try:
            profile_text_element = driver.find_element(AppiumBy.CLASS_NAME, "android.view.View")
            profile_text = profile_text_element.text.strip() if profile_text_element.text else "Нет описания"
        except:
            print("⚠️ Не удалось получить текст профиля")

        # Получаем процент совместимости
        try:
            compatibility_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionMatches("\\d+%")')
            compatibility = int(compatibility_element.get_attribute("content-desc").replace("%", ""))
        except:
            print("⚠️ Не удалось получить процент совместимости")

        print(f"👤 {name}, {age} лет | {profile_text} | Совместимость: {compatibility}%")

        # Фильтрация типов связи
        unwanted_types = ["отношения"]  # Можно изменить список
        if any(unwanted in profile_text.lower() for unwanted in unwanted_types):
            print("🚫 Пропущено: нежелательный тип связи")
            return "left"

        # Возрастной фильтр
        if age < 25 or age > 35:
            print("🚫 Пропущено: неподходящий возраст")
            return "left"

        # Совместимость
        if compatibility >= 70:
            print("✅ Подходит: высокая совместимость")
            return "right"

        print("🚫 Пропущено: нет совпадений")
        return "left"

    except Exception as e:
        print(f"❌ Ошибка при анализе: {e}")
        return "left"

# Анализ одной карточки и свайп
for _ in range(1):
    direction = analyze_profile()
    if direction == "right":
        print("➡️ Делаем свайп вправо (лайк)")
        driver.swipe(100, 1500, 800, 1500, 500)  # Свайп вправо
    elif direction == "left":
        print("⬅️ Делаем свайп влево (пропуск)")
        driver.swipe(800, 1500, 100, 1500, 500)  # Свайп влево
    time.sleep(2)

print("✅ Анализ завершён!")
driver.quit()
