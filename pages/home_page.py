from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()

    def login(self, username, password):
        username_field_locator = (By.ID, "user-name")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()    

    def is_login_and_signup_invisible(self):
        shopping_icon_locator = (By.ID, "shopping_cart_container")
        self.wait.until(EC.visibility_of_element_located(shopping_icon_locator))
       
    def get_page_title(self):
        page_title = (By.CLASS_NAME, "title")
        wait_page_title = self.wait.until(EC.element_to_be_clickable(page_title))

        title_text = wait_page_title.text
        return title_text       
    
    """
    def add_to_chart_first(self):
        add_button = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_button.click()

    def add_to_chart_second(self):
        add_button = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_button.click()

    def click_basket_icon(self):
        basket_icon = self.selenium_driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a")
        basket_icon.click()
    """

    def choose_products(self):
        add_button = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_button.click()

        add_button_two = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_button_two.click()

        basket_icon = self.selenium_driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a")
        basket_icon.click()        
    
    def verify_first_product(self):
        product_title = self.selenium_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div")
        product_name = product_title.text
        return product_name
    
    def verify_second_product(self):
        product_title = self.selenium_driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div")
        product_name = product_title.text
        return product_name

    def checkout_action(self):
        checkout_button = self.selenium_driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_button.click()   
       
    def checkout_your_information(self, firstname, lastname, zip):
        firstname_field = self.selenium_driver.find_element(By.ID, "first-name")
        firstname_field.click()
        firstname_field.clear()
        firstname_field.send_keys(firstname)

        lastname_field = self.selenium_driver.find_element(By.ID, "last-name")
        lastname_field.click()
        lastname_field.clear()
        lastname_field.send_keys(lastname)

        zip_field = self.selenium_driver.find_element(By.ID, "postal-code")
        zip_field.click()
        zip_field.clear()
        zip_field.send_keys(zip)

        submit_button = self.selenium_driver.find_element(By.ID, "continue")
        submit_button.click()  

    def finish_action(self):
        finish_button = self.selenium_driver.find_element(By.ID, "finish")
        finish_button.click()     
 
    def click_burger_menu(self):
        burger_menu_locator = self.selenium_driver.find_element(By.ID, "react-burger-menu-btn")
        burger_menu_locator.click()

    def log_out(self):
        log_out_locator = (By.ID, "logout_sidebar_link")
        log_out = self.wait.until(EC.element_to_be_clickable(log_out_locator))
        log_out.click()  

    def login_page(self):
        login_button_locator = (By.ID, "login-button")
        self.wait.until(EC.element_to_be_clickable(login_button_locator))
        
   
        
    
    