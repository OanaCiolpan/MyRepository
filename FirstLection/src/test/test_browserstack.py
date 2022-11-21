import time

from selenium import webdriver
from src.pages.Destinations import Homepage
from src.pages.sign_in_page import SignInPage
from src.pages.produse import Produse
def test_1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://bstackdemo.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)
    produse = Produse(driver)

    homepage.click_sign_in()
    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    homepage.get_username()
    produse.select_element()
    produse.checkout_elements()
    time.sleep(15)
    # driver.quit()