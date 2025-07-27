import data
import helpers
import pages
import time
from selenium import webdriver



class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities  # imported inside method
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        assert page.get_from()==data.ADDRESS_FROM
        assert page.get_to()==data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)
        page.click_call_taxi_button()
        page.click_supportive_car_button()
        assert page.is_supportive_tab_selected() == "Supportive", "Supportive tab is not selected"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi_button()
        page.click_supportive_car_button()
        page.click_phone_number_button()
        page.enter_phone_number_text(data.PHONE_NUMBER)
        page.select_confirm_button()
        time.sleep(2)
        assert page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)
        page.click_call_taxi_button()
        page.click_supportive_car_button()
        page.select_method_payment_button()
        page.click_add_card_button()
        page.enter_card_number_text(data.CARD_NUMBER)
        page.enter_code_input_field(data.CARD_CODE)
        assert page.get_card_number()==data.CARD_NUMBER
        assert page.get_card_code()==data.CARD_CODE

        page.click_link_button()
        page.click_x_button()

        assert page.get_payment_method() == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)
        page.click_call_taxi_button()
        page.click_supportive_car_button()
        page.enter_message_the_driver_input_field(data.MESSAGE_FOR_DRIVER)
        assert page.get_message_the_driver()==data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)
        page.click_call_taxi_button()
        page.click_supportive_car_button()
        page.click_blanket_handkerchiefs_toggle()
        assert page.is_blanket_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)
        page.click_call_taxi_button()
        page.click_supportive_car_button()
        page.click_ice_cream_increment_button()
        page.click_ice_cream_increment_button()
        assert page.get_ice_cream_quantity() == 2
        time.sleep(2)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi_button()
        page.click_supportive_car_button()
        page.click_enter_number_and_order_button()
        assert page.ordering_car_screen_selected()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()