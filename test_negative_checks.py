from .pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.get(link)
    page = ProductPage(browser, link, 0)
    page.open()
    page.go_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    browser.get(link)
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.get(link)
    page = ProductPage(browser, link, 0)
    page.open()
    page.go_to_basket()
    page.should_disappeared_of_success_message()

