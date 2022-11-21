import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.pages.Destinations import Destination

def test_1():
    service_obj = Service("C:/Users/IT School Lenovo/PycharmProjects/pythonProject9/Drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)

    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://www.booking.com/")

    destination_vacation = Destination(driver)

    destination_vacation.click_accept_button()
    print ("before_select_destionation")
    destination_vacation.select_destination()
    print ("Before start date")
    time.sleep(5)
    destination_vacation.visibile_genius()
    destination_vacation.select_start_date("2022-11-01")
    # destination_vacation.click_btn_Genius_X()
    # destination_vacation.get_destination_name()

    time.sleep(200)
    # driver.quit()