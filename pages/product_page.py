from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button.click()

    def item_added_in_basket(self):
        item = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        item_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
        assert item.text == item_in_basket.text, "Item not in the basket"
        print(f"{item_in_basket.text} in the basket")

    def price_in_basket_equal_item_price(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.COST_BASKET)
        assert price.text == price_in_basket.text, "Price incorrect in the basket"
        print(f"Price {price_in_basket.text} is correct")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
