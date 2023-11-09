from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    #product_page = ProductPage(browser, browser.current_url)
    #login_page.should_be_login_page()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    page.item_in_basket()
    page.price_of_item_in_basket()

