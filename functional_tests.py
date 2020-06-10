from selenium import webdriver

browser = webdriver.Chrome('/home/itamart/Documents/chromedriver')  # Optional argument, if not specified will search path.
browser.get('http://localhost:8000/');

try:
    assert 'Django' in browser.title
except AssertionError:
    print("Browser is not running")
finally:
    browser.quit()