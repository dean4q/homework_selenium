import time

from selenium.webdriver.common.by import By

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_different_language(browser):

    browser.get(link)

    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), 'button not found'
    time.sleep(10)