from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

def get_driver(app_package=None, app_activity=None):
    """
    Подключается к Appium и возвращает WebDriver.
    
    :param app_package: Указывает пакет приложения, которое нужно запустить (например, "com.android.vending").
    :param app_activity: Указывает стартовую активность приложения (например, ".AssetBrowserActivity").
    :return: WebDriver, готовый к работе.
    """

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "RZ8M820SRYL"
    options.automation_name = "UiAutomator2"

    # Если указаны package и activity, передаём их
    if app_package and app_activity:
        options.app_package = app_package
        options.app_activity = app_activity

    # Подключаемся к Appium
    driver = webdriver.Remote("http://localhost:4723", options=options)
    time.sleep(5)
    
    return driver
