import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    # Step 1
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Step 2
    pedir_un_taxi_field = (By.XPATH, "//div[@class='workflow']//button[@class='button round']")
    comfort_field = (By.XPATH, "//div[@class='tariff-cards']//div[text()='Comfort']")
    # Step 3
    cellphone_field = (By.XPATH, "//div[@class='form']//div[@class='np-text']")
    frame_cellphone_field = (By.CSS_SELECTOR, "#phone")
    cellphone_number = data.phone_number
    boton_siguiente_after_cellphone = (By.XPATH, "//div[@class='modal']//button[text()='Siguiente']")
    boton_introduce_codigo = (By.ID, "code")
    boton_confirmar_after_code = (By.XPATH, "//form//button[text()='Confirmar']")
    # Step 4
    element_payment = (By.XPATH, "//div[@class='form']//div[text()='Método de pago']")
    card_option = (By.XPATH, "//div//div[text()='Agregar tarjeta']")
    card_number = (By.ID, "number")
    code_of_card = (By.XPATH, "//div[@class='card-wrapper']//input[@id='code']")
    save_card = (By.XPATH, "//div//button[text()='Agregar']")
    boton_exit = (By.XPATH, "(//div[@class='modal']//button\
    [@class='close-button section-close'])[3]")
    # Step 5
    mensaje_para_el_conductor = (By.ID, 'comment')
    # Step 6
    manta_y_panuelos = (By.XPATH, "//div[@class='reqs open']//span[@class='slider round']")
    # Step 7
    cubeta_de_helado = (By.XPATH, "//div[@class='r r-type-group']//div\
    [text()='Cubeta de helado']")
    boton_helado = (By.XPATH, "//div[@class='r r-type-group']//div[text()='+']")
    number_of_ice_creams = (By.XPATH, "//div[@class='r r-type-group']//div[@class='counter-value']")
    # Step 8
    boton_pedir_un_taxi = (By.CLASS_NAME, "smart-button-wrapper")
    order_body = (By.CLASS_NAME, "order-body")
    info_order_body = (By.CLASS_NAME, "order-header-title")
    # Step 9
    info_conductor = (By.XPATH, "//div[contains(text(),'El conductor llegará')]")
    detalles = (By.XPATH, "(//div[@class='order-btn-group']")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 5).until(EC.\
                                    element_to_be_clickable(self.from_field))

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def wait_to_set_route(self):
            WebDriverWait(self.driver, 5).until(EC. \
                                                element_to_be_clickable(self.pedir_un_taxi_field))

    def set_route(self, from_address, to_address):
        self.wait_for_load_home_page()
        self.set_from(from_address)
        self.set_to(to_address)
        self.wait_to_set_route()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Step 2
    def click_on_pedir_un_taxi(self):
        self.driver.find_element(*self.pedir_un_taxi_field).click()

    def wait_for_comfort(self):
        WebDriverWait(self.driver, 5).until(EC. \
                                                element_to_be_clickable(self.comfort_field))

    def click_on_it(self):
        self.driver.find_element(*self.comfort_field).click()

    def click_on_comfort(self):
        self.click_on_pedir_un_taxi()
        self.wait_for_comfort()
        self.click_on_it()

    def get_the_text_comfort(self):
        return self.driver.find_element(*self.comfort_field).text

    # Step 3
    def click_on_numero_de_telefono(self):
        self.driver.find_element(*self.cellphone_field).click()

    def wait_for_numero_de_tel(self):
        WebDriverWait(self.driver, 5).until(EC. \
                                            element_to_be_clickable(self.frame_cellphone_field))

    def click_on_the_frame_numero_de_telefono(self):
        self.driver.find_element(*self.frame_cellphone_field).send_keys(self.cellphone_number)

    def click_on_siguiente(self):
        self.driver.find_element(*self.boton_siguiente_after_cellphone).click()

    def wait_for_code(self):
        WebDriverWait(self.driver, 5).until(EC. \
                                            element_to_be_clickable(self.boton_introduce_codigo))

    def attach_the_phone_code(self):
        self.driver.find_element(*self.boton_introduce_codigo).send_keys(retrieve_phone_code(self.driver))

    def click_on_confirmar(self):
        self.driver.find_element(*self.boton_confirmar_after_code).click()

    def set_up_phone_number(self):
        self.click_on_numero_de_telefono()
        self.wait_for_numero_de_tel()
        self.click_on_the_frame_numero_de_telefono()
        self.click_on_siguiente()
        self.wait_for_code()
        self.attach_the_phone_code()
        self.click_on_confirmar()
        self.wait_for_comfort()

    def get_the_phone_number(self):
        return self.driver.find_element(*self.cellphone_field).text

    # Step 4
    def search_payment(self):
        element = self.driver.find_element(*self.element_payment)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def wait_for_select_payment(self):
        WebDriverWait(self.driver, 5).until(EC. \
                                                element_to_be_clickable(self.card_option))

    def select_card(self):
        self.driver.find_element(*self.card_option).click()

    def wait_for_more_details(self):
        WebDriverWait(self.driver, 5).until(EC. \
                                                element_to_be_clickable(self.card_number))

    def add_card(self, card_number, card_code):
        self.driver.find_element(*self.card_number).send_keys(card_number)
        self.driver.find_element(*self.code_of_card).send_keys(card_code)
        self.driver.find_element(*self.card_number).click()
        self.driver.find_element(*self.save_card).click()

    def exit_the_metodo_de_pago(self):
        WebDriverWait(self.driver, 5).until(EC. element_to_be_clickable(self.boton_exit))
        self.driver.find_element(*self.boton_exit).click()

    def add_card_as_a_payment(self, card_number, card_code):
        self.search_payment()
        self.wait_for_select_payment()
        self.select_card()
        self.wait_for_more_details()
        self.add_card(card_number, card_code)
        self.exit_the_metodo_de_pago()
        self.wait_for_comfort()

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def get_code_of_card(self):
        return self.driver.find_element(*self.code_of_card).get_property('value')

    # Step 5
    def send_mensaje_para_conductor(self, mensaje):
        self.driver.find_element(*self.mensaje_para_el_conductor)\
            .send_keys(mensaje)

    def get_mensaje_para_el_conductor(self):
        return self.driver.find_element(*self.mensaje_para_el_conductor)\
        .get_property('value')

    # Step 6
    def click_manta_y_panuelos(self):
        self.driver.find_element(*self.manta_y_panuelos) .click()

    # Step 7
    def search_cubeta_de_helado(self):
        cubeta = self.driver.find_element(*self.cubeta_de_helado)
        self.driver.execute_script("arguments[0].scrollIntoView();", cubeta)

    def add_2_helados(self):
        helado = self.driver.find_element(*self.boton_helado)
        helado.click()
        helado.click()

    def select_2_helados(self):
        self.click_manta_y_panuelos()
        self.search_cubeta_de_helado()
        self.add_2_helados()

    def check_number_of_ice_creams(self):
        return self.driver.find_element(*self.number_of_ice_creams).text
    # Step 8
    def select_a_taxi(self):
        self.driver.find_element(*self.boton_pedir_un_taxi).click()

    def see_the_order_body(self):
        WebDriverWait(self.driver, 5).until(EC.\
        visibility_of_element_located(self.order_body))

    def wait_until_you_see_the_order_body(self):
        self.select_a_taxi()
        self.see_the_order_body()

    def check_the_order_body(self):
        return self.driver.find_element(*self.info_order_body).text

    # Step 9
    def check_the_info_of_the_driver(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.info_conductor))



