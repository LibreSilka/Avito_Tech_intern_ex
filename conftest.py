import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    """Инициализация WebDriver"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


























# @pytest.fixture(params=["chrome", "firefox"], scope="module")
# def driver(request):
#     """Инициализация WebDriver для нескольких браузеров"""
#     if request.param == "chrome":
#         service = Service(ChromeDriverManager().install())
#         options = webdriver.ChromeOptions()
#         options.add_argument("--start-maximized")
#         driver = webdriver.Chrome(service=service, options=options)
#
#     elif request.param == "edge":
#         service = Service(EdgeChromiumDriverManager().install())
#         options = webdriver.EdgeOptions()
#         driver = webdriver.Firefox(service=service, options=options)
#
#     else:
#         raise ValueError(f"Unsupported browser: {request.param}")
#
#     yield driver
#     driver.quit()
