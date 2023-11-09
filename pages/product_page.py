from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
class ProductPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        link.click()
        #return ProductPage(browser=self.browser, url=self.browser.current_url)
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def item_in_basket(self):
        str1 = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_TITLE)
        str2 = self.browser.find_element(*ProductPageLocators.TITLE_BOOK)
        # проверка, что товар добавлен в корзину
        assert str2.text == str1.text, "Ошибка"
        print("Товар {} добавлен в корзину".format(str2.text))
    def price_of_item_in_basket(self):
        str3 = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        str4 = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        # проверка, что товар добавлен в корзину
        assert str4.text == str3.text, "Ошибка"
        print("Стоимость корзины = {}. СТоимость корзины совпадает с ценой товара".format(str4.text))

