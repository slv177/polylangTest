import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_btn_presents(browser):
    browser.get(link)
    time.sleep(30)
    addToBasketButtons = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert addToBasketButtons > 0, "There is no 'Add to basket' button"




