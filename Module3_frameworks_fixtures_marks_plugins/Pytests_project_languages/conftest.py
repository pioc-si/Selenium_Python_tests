import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
        help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="es",
        help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        user_language = request.config.getoption("language")
        options_firefox = Options()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_firefox)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser....")
    browser.quit()


#if __name__ == "__main__":
#    pytest.main()

