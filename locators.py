import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Temu:
    # Step 1:
    account_field = (By.XPATH, '//div[@class="_10iL_95W"]//div[@class=\
                           "_2CSyqUbD"]/div[@role="button"]')
    email_field = (By.CSS_SELECTOR, "div[dir='ltr'] input[type='text']")
    continue_botton = (By.CSS_SELECTOR, "#submit-button")
    password_field = (By.CSS_SELECTOR, "#pwdInputInLoginDialog")
    login_botton = (By.CSS_SELECTOR, "#submit-button")

    name_field = (By.CSS_SELECTOR, 'div._1MYxPpz3 span')

    # Step 2:
    search_field = (By.ID, 'searchInput')
    search_botton = (By.CSS_SELECTOR, 'input#searchInput div[role="button"]')
    item_location = (By.XPATH, f"//h2[@class='_28vQbnbN _2fLnHBGs']//span[contains(text(), {data.description})]")

    object_selected = (By.XPATH, "//div[@class='_1Zf27vaY']//span")

    # Step 3:
    color = (By.XPATH, "//div[@class='_1thUmrmy']//div[contains(@aria-label, 'Negro')]")
    shopping_cart = (By.XPATH, "//div[@class='_100Uy0HO']//span[@class='_3cgghkPI']")
    go_to_the_cart = (By.CSS_SELECTOR, "div._2oPZebLl div.vd-NrRvD")

    color_selected = (By.XPATH, "//div[@class='_2ftNi7ce RaHoOjN4']//span")

    # Step 4:
    buy_botton = (By.CSS_SELECTOR, "span._3cgghkPI div.f1y5eRaa")

    oxxo_confirmation = (By.CSS_SELECTOR, "div[role='combobox'] span[role='radio'] span")

    # Step 5:
    oxxo_botton = (By.CSS_SELECTOR, "div[role='combobox'] span[role='radio']")
    complete_purchase = (By.CSS_SELECTOR, "div._1UBLGSqv div._3XAninB_")

    information_of_the_purchase = (By.CSS_SELECTOR, "div._2Ek7-WZa div._1X1ghNit")

    def __init__(self, driver):
        self.temu_driver = driver

    # Step 1:
    def click_account_field(self):
        WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.account_field)).click()

    def set_email_field(self, email):
        WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.email_field)).send_keys(email)

    def click_continue_botton(self):
        self.temu_driver.find_element(*self.continue_botton).click()

    def set_password_field(self, password):
        WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.password_field)).send_keys(password)

    def click_login_button(self):
        self.temu_driver.find_element(*self.login_botton).click()

    def set_login(self, email, password):
        self.click_account_field()
        self.set_email_field(email)
        self.click_continue_botton()
        self.set_password_field(password)
        self.click_login_button()

    def get_name(self):
        return self.temu_driver.find_element(*self.name_field).text

    # Step 2:
    def search_for_item(self, object_to_buy):
        WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.search_field)).send_keys(object_to_buy)

    def click_search_botton(self):
        self.temu_driver.find_element(*self.search_botton).click()

    def click_select_object(self):
        WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.item_location)).click()

    def complete_search(self, object_to_buy):
        self.search_for_item(object_to_buy)
        self.click_search_botton()
        self.click_select_object()

    def confirm_the_object_selected(self):
        return self.temu_driver.find_element(*self.object_selected).text

    # Step 3:
    def select_the_color(self):
        WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.color)).click()

    def click_add_item(self):
        self.temu_driver.find_element(*self.shopping_cart).click()

    def click_go_to_the_cart(self):
        self.temu_driver.find_element(*self.go_to_the_cart).click()

    def add_item(self):
        self.select_the_color()
        self.click_add_item()
        self.click_go_to_the_cart()

    def get_color(self):
        return self.temu_driver.find_elment(*self.color_selected).text

    # Step 4:
    def click_buy_botton(self):
        WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.buy_botton)).click()

    def get_oxxo_option(self):
        return self.temu_driver.find_element(*self.oxxo_confirmation).text

    # Step 5:
    def search_method_of_payment(self):
        element = WebDriverWait(self.temu_driver, 10).until \
            (EC.element_to_be_clickable(self.oxxo_botton))
        self.temu_driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_complete_purchase(self):
        self.temu_driver.find_element(*self.complete_purchase).click()

    def finish_the_purchase(self):
        self.search_method_of_payment()
        self.click_complete_purchase()

    def confirm_the_purchase(self):
        return self.temu_driver.find_element(*self.information_of_the_purchase).text
