from seleniumpagefactory.Pagefactory import PageFactory

class Produse(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
         'produs_first':  ('XPATH', '// *[ @ id = "1"] / div[4]'),
         'produs_second': ('XPATH', '//*[ @ id = "2"]  / div[4]'),
         'produs_third':  ('XPATH', '//*[ @ id = "4"] / div[4]'),
         'checkout_btn': ('XPATH', '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]/div[3]')
    }

    def select_element(self):
        self.produs_first.click()
        self.produs_second.click()
        self.produs_third.click()

    def checkout_elements(self):
        self.checkout_btn.click()


