from locators import Temu
import data
from selenium import webdriver

class TestTemu:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.edge.options import Options

        edge_options = Options()
        edge_options.add_argument("--inprivate")

        cls.driver = webdriver.Edge(options=edge_options)

    def test_purchase_flow(self):
        # add the driver
        self.driver.get(data.temu_url)
        temu_page = Temu(self.driver)

        # Step 1: Enter to the account
        email = data.email_address
        password = data.password_text
        temu_page.set_login(email, password)
        assert temu_page.get_name() == data.account_name

        # Step 2: Select the product
        temu_page.complete_search(data.product)
        assert temu_page.confirm_the_object_selected() == data.product

        # Step 3: Select the color
        temu_page.add_item()
        assert data.color in temu_page.get_color()

        # step 4: see the next page
        temu_page.click_buy_botton()
        assert temu_page.get_oxxo_option() == data.payment

        # Step 5: Finish the buy
        temu_page.finish_the_purchase()
        assert data.final_text in temu_page.confirm_the_purchase()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()