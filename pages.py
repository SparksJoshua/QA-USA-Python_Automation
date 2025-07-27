from selenium.webdriver.common.by import By

import time

import helpers



class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.CSS_SELECTOR, '.button.round')
    SUPPORTIVE_CAR_BUTTON = (By.XPATH, '//img[@alt="Supportive"]')
    SUPPORTIVE_ACTIVE_SELECTED = (By.CSS_SELECTOR, "div.tcard.active")
    SUPPORTIVE_TEXT_DISPLAY = (By.CLASS_NAME, "tcard-title")
    PHONE_NUMBER_BUTTON = (By.XPATH, '//div[@class="np-button"]')
    PHONE_NUMBER_DISPLAYED_TEXT = (By.XPATH, '//div[@class="np-text"]')
    PHONE_NUMBER_TEXT =(By.ID, 'phone')
    PHONE_NUMBER_NEXT_BUTTON = (By.XPATH, '//button[text()="Next"]')
    SMS_CODE_INPUT_FIELD = (By.ID, 'code')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Confirm"]')
    METHOD_PAYMENT_BUTTON = (By.CSS_SELECTOR, '.pp-value-text')
    ADD_CARD_BUTTON = (By.XPATH, '//img[contains(@src, "card.411e0152")]')
    CARD_NUMBER_INPUT_FIELD = (By.ID, 'number')
    CODE_INPUT_FIELD = (By.XPATH, '//input[@placeholder="12"]')
    LINK_BUTTON = (By.XPATH, '//button[text()="Link"]')
    X_BUTTON = (By.CSS_SELECTOR, 'button.section-close')
    PAYMENT_METHOD_TYPE = (By.CSS_SELECTOR, ".pp-value-text")
    MESSAGE_THE_DRIVER_INPUT_FIELD = (By.XPATH, '//input[@placeholder="Get some whiskey"]')
    BLANKET_HANDKERCHIEFS_TOGGLE = (By.XPATH, '//div[@class="r-sw-label" and text()="Blanket and handkerchiefs"]/following-sibling::div[@class="r-sw"]//span[contains(@class, "slider")]')
    BLANKET_HANDKERCHIEFS_CHECKBOX = (By.XPATH, '//div[@class="r-sw-label" and text()="Blanket and handkerchiefs"]/following-sibling::div[@class="r-sw"]//input[@type="checkbox"]')
    ICE_CREAM_DECREMENT_BUTTON = (By.XPATH, '//div[text()="Ice cream"]/following-sibling::div//div[contains(@class, "counter-minus")]')
    ICE_CREAM_INCREMENT_BUTTON = (By.CSS_SELECTOR, ".counter-plus")
    ICE_CREAM_QUANTITY = (By.XPATH, '//div[text()="Ice cream"]/following-sibling::div//div[@class="counter-value"]')
    ENTER_THE_NUMBER_AND_ORDER_BUTTON = (By.CSS_SELECTOR, "div.smart-button-wrapper > button.smart-button")
    ORDER_CAR_SCREEN   = (By.XPATH, "//div[@class='order-header-title' and text()='Car search']")


    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, address):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(address)

    def enter_to_location(self, address):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(address)

    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property('value')

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def click_supportive_car_button(self):
        self.driver.find_element(*self.SUPPORTIVE_CAR_BUTTON).click()

    def is_supportive_tab_selected(self):
        active_card = self.driver.find_element(*self.SUPPORTIVE_ACTIVE_SELECTED)
        title = active_card.find_element(*self.SUPPORTIVE_TEXT_DISPLAY).text
        return title

    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    def enter_phone_number_text(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_TEXT).send_keys(phone_number)
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()
        code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.SMS_CODE_INPUT_FIELD).send_keys(code)

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_DISPLAYED_TEXT).text

    def click_phone_number_next_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()

    def select_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def select_method_payment_button(self):
        self.driver.find_element(*self.METHOD_PAYMENT_BUTTON).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()

    def enter_card_number_text(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_INPUT_FIELD).send_keys(card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.CARD_NUMBER_INPUT_FIELD).get_property('value')

    def enter_code_input_field(self, code):
        self.driver.find_element(*self.CODE_INPUT_FIELD).send_keys(code)
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, 'body').click()

    def get_card_code(self):
        return self.driver.find_element(*self.CODE_INPUT_FIELD).get_property('value')

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON).click()

    def click_x_button(self):
        buttons = self.driver.find_elements(*self.X_BUTTON)
        for button in buttons:
            if button.is_displayed() and button.is_enabled():
                button.click()
                return
        raise Exception("No visible close button found")

    def get_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_TYPE).text

    def enter_message_the_driver_input_field(self, messages):
        self.driver.find_element(*self.MESSAGE_THE_DRIVER_INPUT_FIELD).send_keys(messages)

    def get_message_the_driver(self):
        return self.driver.find_element(*self.MESSAGE_THE_DRIVER_INPUT_FIELD).get_property('value')

    def click_blanket_handkerchiefs_toggle(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEFS_TOGGLE).click()

    def is_blanket_handkerchiefs_selected(self):
        checkbox = self.driver.find_element(*self.BLANKET_HANDKERCHIEFS_CHECKBOX)
        return checkbox.is_selected()

    def click_ice_cream_increment_button(self):
        self.driver.find_element(*self.ICE_CREAM_INCREMENT_BUTTON).click()

    def get_ice_cream_quantity(self):
        quantity_text = self.driver.find_element(*self.ICE_CREAM_QUANTITY).text
        return int(quantity_text)

    def click_enter_number_and_order_button(self):
        self.driver.find_element(*self.ENTER_THE_NUMBER_AND_ORDER_BUTTON).click()

    def ordering_car_screen_selected(self):
        return self.driver.find_element(*self.ORDER_CAR_SCREEN).is_displayed()