import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost:8888/Opencart/opencart-3.0.3.2/upload/", help="choose your browser")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request, url):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)

    def open(path=""):
        return driver.get(url + path)
    driver.open = open
    driver.open()
    return driver
