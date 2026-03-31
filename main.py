import data
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        # Configuración correcta para logging de performance en Selenium 4.x
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=chrome_options)

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
        routes_page.click_on_comfort()
        assert "Comfort" in routes_page.get_the_text_comfort()

        # Paso 3: Rellenar el número de teléfono
        routes_page.set_up_phone_number()
        assert routes_page.get_the_phone_number() == routes_page.cellphone_number

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
        assert routes_page.check_number_of_ice_creams() == '2'

        # Paso 8: Aparece el modal para buscar un taxi
        routes_page.wait_until_you_see_the_order_body()
        assert routes_page.check_the_order_body() == "Buscar automóvil"

        # Paso 9
        routes_page.check_the_info_of_the_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


