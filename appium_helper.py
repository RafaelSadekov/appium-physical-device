from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

def get_driver(app_package=None, app_activity=None, no_reset=False):
    """
    Подключается к Appium и возвращает WebDriver.

    :param app_package: Указывает пакет приложения (например, "com.twinby.app").
    :param app_activity: Указывает стартовую активность приложения.
    :param no_reset: Если True, не сбрасывает данные приложения.
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

    # Добавляем параметр noReset
    if no_reset:
        options.no_reset = True

    # Подключаемся к Appium
    driver = webdriver.Remote("http://localhost:4723", options=options)
    time.sleep(5)
    
    return driver
