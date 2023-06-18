from pages.home_page import HomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")

    assert home_page.get_page_title() == "Products"
    """
    home_page.add_to_chart_first()
    home_page.add_to_chart_second()
    home_page.click_basket_icon()
    """
    home_page.choose_products()

    assert home_page.get_page_title() =="Your Cart"
    assert home_page.verify_first_product() == "Sauce Labs Backpack"
    assert home_page.verify_second_product() == "Sauce Labs Bike Light"

    home_page.checkout_action()

    assert home_page.get_page_title() == "Checkout: Your Information"
    home_page.checkout_your_information("Ime","Prezime","12345")

    assert home_page.get_page_title() == "Checkout: Overview"
    assert home_page.verify_first_product() == "Sauce Labs Backpack"
    assert home_page.verify_second_product() == "Sauce Labs Bike Light"
    home_page.finish_action()

    assert home_page.get_page_title() == "Checkout: Complete!"
    home_page.click_burger_menu()
    home_page.log_out()

    home_page.login_page()



