from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class Destination(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'destination': ('ID', "ss"),
        'btn_accept': ('ID', "onetrust-accept-btn-handler"),
        'btn_Genius_X': ('ID', "b2searchresultsPage"),
        'start_date': ('CSS', ".b21c1c6c83 e505d9d049 e5f46f434c"),
        'sign_in_genius': ('class_name', 'b9def0936d')
    }

    def select_destination(self):
        self.destination.set_text('Croatia\n')

    def click_accept_button(self):
        self.btn_accept.click()

    def click_btn_Genius_X(self):
        self.btn_Genius_X.click()

    def visibile_genius(self):

        self.sign_in_genius.click()

    def select_start_date(self, DateParam):
            Alert(self.driver).dismiss()
            print ("Before")
            dates = self.driver.find_elements(By.CLASS_NAME, "b21c1c6c83")

            print("Oana", len(dates))

            for date in dates:
                if date.get_attribute("data-date") == DateParam:
                    date.click()
                    break

    def get_destination_name(self):
        retrieved_destination_name = self.destination.get_text()
        assert retrieved_destination_name == 'Croatia'
