from pages.home_page import HomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")

    home_page.get_page_title() == "Products"
    """
    home_page.add_to_chart_first()
    home_page.add_to_chart_second()
    home_page.click_basket_icon()
    """
    home_page.choose_products()

    home_page.get_page_title() =="Your Cart"
    home_page.verify_product() == "Sauce Labs Backpack"
    home_page.verify_product() == "Sauce Labs Bike Light"

    home_page.checkout_action()

    home_page.get_page_title() == "Checkout: Your Information"
    home_page.checkout_your_information("Ime","Prezime","12345")

    home_page.get_page_title() == "Checkout: Overview"
    home_page.verify_product() == "Sauce Labs Backpack"
    home_page.verify_product() == "Sauce Labs Bike Light"
    home_page.finish_action()

    home_page.get_page_title =="Checkout: Complete!"
    home_page.click_burger_menu()
    home_page.log_out()

    home_page.login_page()



