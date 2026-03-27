import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado
    en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código\
                             en tu aplicación.")
        return code


class UrbanRoutesPage:
    # Step 1
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Step 2
    pedir_un_taxi_field = (By.XPATH, "//div[@class='workflow']//button[@class='button round']")
    Comfort_field = (By.XPATH, "//div[@class='tcard activate']//div[@class='tcard-icon']")
    # Step 3
    cellphone_field = (By.XPATH, "//div[@class='form']/div[@class='np-button']")
    frame_cellphone_field = (By.CSS_SELECTOR, "#phone")
    cellphone_number = data.phone_number
    click_siguiente_after_cellphone = (By.CSS_SELECTOR, "button[type='submit']\
    [class='button fully']")
    click_introduce_codigo = (By.ID, "code")
    click_on_confirmar_after_code = (By.XPATH, "//form//button[text()='Confirmar']")
    # Step 4
    search_element_payment = (By.XPATH, "//div[@class='form']//div[text()='Método de pago']")
    choose_card = (By.XPATH, "//div//div[text()='Agregar tarjeta']")
    click_card_number = (By.ID, "number")
    click_code_of_card = (By.ID, "code")
    save_card = (By.XPATH, "//div//button[text()='Agregar']")
    click_on_exit = (By.CSS_SELECTOR, '.close-button section-close')
    # Step 5
    click_mensaje_para_el_conductor = (By.ID, 'comment')
    # Step 6
    select_manta_y_panuelos = (By.XPATH, "//div[@class='reqs open']//span[@class='slider round']")
    # Step 7
    see_cubeta_de_helado = (By.XPATH, "//div[@class='r r-type-group']//div\
    [text()='Cubeta de helado']")
    choose_2_helados = (By.XPATH, "//div[@class='r r-type-group']//div[text()='+']")
    # Step 8
    click_on_pedir_un_taxi = (By.CLASS_NAME, "smart-button-wrapper")
    wait_to_see_the_order_body = (By.CLASS_NAME, "order-body")
    select_info_conductor = (By.XPATH, "//div[@class='order-subbody']\
    //div[@class='order-btn-group']")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Step 2
    def click_on_Pedir_un_taxi(self):
        self.driver.find_element(*self.pedir_un_taxi_field).click()

    def click_on_Comfort(self):
        self.driver.find_element(*self.Comfort_field).click()

    # Step 3
    def click_on_Número_de_teléfono(self):
        self.driver.find_element(*self.cellphone_field).click()

    def click_on_the_frame_Número_de_telefono(self):
        self.driver.find_element(*self.frame_cellphone_field).send_keys(self.cellphone_number)

    def click_on_siguiente(self):
        self.driver.find_element(*self.click_siguiente_after_cellphone).click()

    def attach_the_phone_code(self):
        self.driver.find_element(*self.click_introduce_codigo).send_keys(retrieve_phone_code(self.driver))

    def click_on_confirmar(self):
        self.driver.find_element(*self.click_on_confirmar_after_code).click()

    def set_up_phone_number(self):
        self.click_on_Número_de_teléfono()
        self.click_on_the_frame_Número_de_telefono()
        self.click_on_siguiente()
        self.attach_the_phone_code()
        self.click_on_confirmar()

    # Step 4
    def search_payment(self):
        element = self.driver.find_element(*self.search_element_payment)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def select_card(self):
        self.driver.find_element(*self.choose_card).click()

    def add_card(self, card_number, card_code):
        self.driver.find_element(*self.click_card_number).send_keys(card_number)
        cvv_field = self.driver.find_element(*self.click_code_of_card)
        cvv_field.send_keys(card_code)
        cvv_field.send_keys(Keys.TAB)
        self.driver.find_element(*self.save_card).click()

    def exit_the_metodo_de_pago(self):
        self.driver.find_element(*self.click_on_exit).click()

    def add_card_as_a_payment(self, card_number, card_code):
        self.search_payment()
        self.select_card()
        self.add_card(card_number, card_code)
        self.exit_the_metodo_de_pago()

    def get_card_number(self):
        return self.driver.find_element(*self.click_card_number).get_property('value')

    def get_code_of_card(self):
        return self.driver.find_element(*self.click_code_of_card).get_property('value')

    # Step 5
    def send_mensaje_para_conductor(self, mensaje):
        self.driver.find_element(*self.click_mensaje_para_el_conductor)\
            .send_keys(mensaje)

    def get_mensaje_para_el_conductor(self):
        return self.driver.find_element(*self.click_mensaje_para_el_conductor)\
        .get_property('value')

    # Step 6
    def click_manta_y_panuelos(self):
        self.driver.find_element(*self.click_manta_y_panuelos) .click()

    # Step 7
    def search_cubeta_de_helado(self):
        cubeta = self.driver.find_element(*self.see_cubeta_de_helado)
        self.driver.execute_script("arguments[0].scrollIntoView();", cubeta)

    def add_2_helados(self):
        helado = self.driver.find_element(*self.choose_2_helados)
        helado.click()
        helado.click()

    def select_2_helados(self):
        self.click_manta_y_panuelos()
        self.search_cubeta_de_helado()
        self.add_2_helados()

    # Step 8
    def select_a_taxi(self):
        self.driver.find_element(*self.click_on_pedir_un_taxi).click()

    def see_the_order_body(self):
        WebDriverWait(self.driver, 5).until(EC.\
        visibility_of_element_located(self.wait_to_see_the_order_body))

    def wait_until_you_see_the_order_body(self):
        self.select_a_taxi()
        self.see_the_order_body()

    # Step 9
    def check_the_info_of_the_driver(self):
        WebDriverWait(self.driver, 5).until(EC.\
        visibility_of_element_located(self.select_info_conductor))


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para
        # recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_complete_taxi_booking(self):
        # Agregar el controlador
        self.driver.get(data.urban_routes_url)
        # Seleccionar la clase de la que nos vamos a basar
        routes_page = UrbanRoutesPage(self.driver)

        # Paso 1: Configurar dirección
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        # Paso 2: Seleccionar tarifa Comfort
        routes_page.click_on_Pedir_un_taxi()
        routes_page.click_on_Comfort()

        # Paso 3: Rellenar el número de teléfono
        routes_page.set_up_phone_number()

        # Paso 4: Agregar una tarjeta de crédito
        card = data.card_number
        code = data.card_code
        routes_page.add_card_as_a_payment(card, code)
        assert routes_page.get_card_number() == card
        assert routes_page.get_code_of_card() == code

        # Paso 5: Escribir un mensaje para el controlador
        mensaje = data.message_for_driver
        routes_page.send_mensaje_para_conductor(mensaje)
        assert routes_page.get_mensaje_para_el_conductor() == mensaje

        # Paso 6: Pedir una manta y pañuelos
        routes_page.click_manta_y_panuelos()

        # Paso 7: Pedir 2 helados
        routes_page.select_2_helados()

        # Paso 8: Aparece el modal para buscar un taxi
        routes_page.wait_until_you_see_the_order_body()

        # Paso 9
        routes_page.check_the_info_of_the_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


