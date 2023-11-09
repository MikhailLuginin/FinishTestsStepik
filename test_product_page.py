from .pages.product_page import ProductPage
import time
import pytest
@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])

def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    page.item_in_basket()
    page.price_of_item_in_basket()

