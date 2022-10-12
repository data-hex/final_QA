from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button.click()

    def item_added_in_basket(self):
        pass

    def price_in_basket_equal_item_price(self):
        pass
