from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    ID_LOGIN = (By.CSS_SELECTOR, "#login_form")
    ID_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    ICON_USER = (By.CSS_SELECTOR, "#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a")
    EMAIL_USER = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > table > tbody > tr:nth-child(2) > td")


class ProductPageLocators():
    BUTTON_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket") #Добавить в корзину
    ADD_TO_BASKET_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")#Название книги в корзине
    PRICE_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color") #(By.CLASS_NAME, "price_color")#Цена книги
    TITLE_BOOK = (By.CSS_SELECTOR, "h1")#Название книги
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")#Цена книги в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_NULL = (By.CSS_SELECTOR, "#content_inner>p")
