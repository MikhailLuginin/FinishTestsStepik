from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Корзина не пуста"

    def basket_null(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NULL), "Сообщения о то что корзина пустая - нет"
