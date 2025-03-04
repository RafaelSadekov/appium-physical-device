# Appium Android Automation

Этот проект использует **Appium** для автоматизации физического Android-устройства 📱.  
📌 Основные возможности:
- 📲 Автоматическая установка приложений через Google Play
- 🔄 Свайпы и клики в приложениях
- 🤖 Тестирование реального устройства с использованием **Appium Inspector**
- 🔍 Поиск элементов UI и взаимодействие с ними

## 🔧 Установка
## **1. Устанавливаем необходимые компоненты на хосте** 🖥  

### **1.1. Устанавливаем JDK (Java Development Kit)**
Appium требует **Java**. Устанавливаем **JDK 17 или 21**:
- **Скачать JDK**:  
  🔗 [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html)  
  🔗 [OpenJDK (через Chocolatey)](https://chocolatey.org/packages/openjdk)  

- **Проверяем установку**:
  ```cmd
  java -version
  ```

### **1.2. Устанавливаем Node.js**
Appium работает через **Node.js**.

- **Скачиваем Node.js**:  
  🔗 [Node.js Official](https://nodejs.org/)  
  (Рекомендуется **LTS-версия**)

- **Проверяем установку**:
  ```cmd
  node -v
  npm -v
  ```

### **1.3. Устанавливаем Appium**
После установки Node.js просто вводим в терминале:
```cmd
npm install -g appium
```
Проверяем:
```cmd
appium -v
```

### **1.4. Устанавливаем `commandlinetools` (Android SDK)**
1. **Скачиваем `commandlinetools`**:  
   🔗 [Android Command Line Tools](https://developer.android.com/studio#command-tools)  
2. **Распаковываем архив в**:
   ```
   C:\Users\User\AppData\Local\Android\Sdk\cmdline-tools\latest\
   ```

### **1.5. Настраиваем переменные среды**
Открываем **"Переменные среды"** (`Win + R` → `sysdm.cpl`)  
1. В **Системных переменных** создаём:  
   - **Имя:** `ANDROID_HOME`  
     **Значение:** `C:\Users\User\AppData\Local\Android\Sdk`
   - **Имя:** `ANDROID_SDK_ROOT`  
     **Значение:** `C:\Users\User\AppData\Local\Android\Sdk`

2. В **Path** добавляем:
   ```
   C:\Users\User\AppData\Local\Android\Sdk\cmdline-tools\latest\bin
   C:\Users\User\AppData\Local\Android\Sdk\platform-tools
   ```

### **1.6. Устанавливаем Android SDK через `sdkmanager`**
После настройки переменных **перезапускаем терминал** и выполняем:
```cmd
sdkmanager --list
sdkmanager --install "platform-tools" "build-tools;34.0.0"
```
📌 Заменяй `34.0.0` на актуальную версию.

---

## **2. Настраиваем проект с Appium**  
Теперь создадим **проект и изолированное окружение Python**.

### **2.1. Создаём папку проекта**
```cmd
mkdir C:\swipe
cd C:\swipe
```

### **2.2. Устанавливаем Python и создаём виртуальное окружение**
- **Проверяем Python**:
  ```cmd
  python --version
  ```
- **Создаём виртуальное окружение**:
  ```cmd
  python -m venv venv
  ```
- **Активируем окружение**:
  ```cmd
  venv\Scripts\activate
  ```

### **2.3. Устанавливаем библиотеки Python**
```cmd
pip install appium-python-client
```

pip install -r requirements.txt

---

## **3. Подключаем устройство**
### **3.1. Проверяем, видит ли ADB телефон**
```cmd
adb devices
```
Если статус `unauthorized`, **разреши отладку USB на телефоне**.

### **3.2. Запускаем Appium**
```cmd
appium server
```

### **3.3. Проверяем Appium Inspector**
1. **Скачиваем**:  
   🔗 [Appium Inspector](https://github.com/appium/appium-inspector/releases)  
2. **Подключаемся к Appium** (`localhost:4723`).
3. **Находим элементы на экране и их `resource-id`**.

---

## **4. Пишем автоматизированный скрипт**
Создаём файл test_name.py:

```python
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Настройки подключения
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RZ8M820SRYL"
options.automation_name = "UiAutomator2"

# Подключаемся к Appium
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(5)

# Прописываем дествия

print("✅")
driver.quit()
```

---

## **5. Запускаем тест**
```cmd
python test_name.py
```
✅ **Appium сам откроет Google Play, найдёт Instagram и установит его!** 🚀  

---
