import pytest
from playwright.sync_api import Page

from LoginPage import LoginPage
from HomePage import HomePage
from CheckoutPage import CheckoutPage
from Order_Confirm_Page import Order_Confirm_Page
from LogoutPage import LogoutPage

@pytest.mark.parametrize("username, password, item_name, firstname, lastname, email, company, country, state, city, address, address2, zip_n, phone, fax, instore, ship_type, pay_type",
            [("admin.test@hmail.com", "Admin@123", "14.1-inch Laptop", "Paul", "Sean", "paul.sean@sample.com", "Samplecomp", "Canada", "British Columbia", "Vancouver", "6108 301F street", "", "G3A 0P9", "4566892201", "", "False", "ground", "cashOndel"),
             ("admin2.test@hmail.com", "Admin2@345", "14.1-inch Laptop", "Sally", "Synks", "sally.synks@sample.com", "Samplecomp2", "Canada", "British Columbia", "Vancouver", "6109 308B street", "", "G5A 0Q9", "6546892201", "", "False", "nextDay", "moneyOrder")])

def test_user_buying_item(page:Page, username, password, item_name, firstname, lastname, email, company, country, state, city, address, address2, zip_n, phone, fax, instore, ship_type, pay_type ):
    page.goto("https://demowebshop.tricentis.com/")

    #login
    login_page = LoginPage(page)
    login_page.login_action(username, password)

    #homepage
    home_page = HomePage(page)
    home_page.select_product_action(item_name)
    home_page.add_to_cart_action()
    home_page.shop_cart_action()
    home_page.accept_terms_action()
    home_page.checkout_action()

    #checkout
    checkout_page = CheckoutPage(page)
    checkout_page.billing_action(firstname, lastname, email, company, country, state, city, address, address2, zip_n, phone, fax)
    checkout_page.shipadd_action(instore)
    checkout_page.shipmethod_action(ship_type)
    checkout_page.paymentmethod_action(pay_type)
    checkout_page.payment_info()
    checkout_page.confirm()

    #OrderConfirm
    order_confirmed_page = Order_Confirm_Page(page)
    order_confirmed_page.order_confirm_action()

    #logout
    logout_page = LogoutPage(page)
    logout_page.logout_action()

