import pytest
from selenium import webdriver

def pytest_addoption(parser): 
    parser.addoption('--browser_name', action='store', default='chrome', 
                     help = 'Choose browser: chrome or') 
    parser.addoption('--language', action='store', default='es', 
                     help ='Choose lang') 
    
@pytest.fixture(scope='function') 
def browser(request): 
    browser_name=request.config.getoption('browser_name') 
    user_language = request.config.getoption('language') 
    if browser_name == 'chrome': 
        print("\nstart chrome browser for test..") 
        options_chrome = webdriver.ChromeOptions() 
        options_chrome.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}) 
        browser = webdriver.Chrome(options=options_chrome) 
    elif browser_name == 'firefox': 
        print("\nstart firefox browser for test..") 
        options_firefox = webdriver.FirefoxOptions() 
        options_firefox.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe' 
        options_firefox.set_preference("intl.accept_languages", user_language) 
        browser = webdriver.Firefox(options=options_firefox) 
    else: 
        raise pytest.UsageError("--browser_name should be chrome or firefox") 
    yield browser print("\nquit browser..") 
    browser.quit()

    