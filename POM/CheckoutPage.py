from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

#Billing Links

        self.customer_field = page.locator("#billing-address-select")

        self.firstNm_field = page.locator("#BillingNewAddress_FirstName")
        self.lastNm_field = page.locator("#BillingNewAddress_LastName")
        self.email_field = page.locator("#BillingNewAddress_Email")
        self.company_field = page.locator("#BillingNewAddress_Company")
        self.country_list_field = page.locator("#BillingNewAddress_CountryId")
        self.state_list_field = page.locator("#BillingNewAddress_StateProvinceId")
        self.city_field = page.locator("#BillingNewAddress_City")
        self.add1_field = page.locator("#BillingNewAddress_Address1")
        self.add2_field = page.locator("#BillingNewAddress_Address2")
        self.zip_field = page.locator("#BillingNewAddress_ZipPostalCode")
        self.phn_field = page.locator("#BillingNewAddress_PhoneNumber")
        self.fax_field = page.locator("#BillingNewAddress_FaxNumber")

        self.continue_link = page.locator("#billing-buttons-container input[value='Continue']")


#Shipping Address links

        self.instore_radio = page.locator("#PickUpInStore")
        self.continue2_link = page.locator("//input[@onclick='Shipping.save()']")


#Shipping Method links

        self.ground_radio = page.locator("#shippingoption_0")
        self.nextDay_radio = page.locator("#shippingoption_1")
        self.SndDay_radio = page.locator("#shippingoption_2")

        self.continue3_link = page.locator('input.button-1.shipping-method-next-step-button')


#Payment Method links

        self.cash_on_delivery_radio = page.locator("#paymentmethod_0")
        self.money_order_radio = page.locator("#paymentmethod_1")
        self.credit_card_radio = page.locator("#paymentmethod_2")
        self.purchase_order_radio = page.locator("#paymentmethod_3")

        self.continue4_link = page.locator("input[class='button-1 payment-method-next-step-button']")


 #Payment Info Links

        self.continue5_link = page.locator('input.button-1.payment-info-next-step-button')


#Confirm Order

        self.confirm_link = page.locator("input[value='Confirm']")


#Billing Action
    def billing_action(self, firstname, lastname, email, company, country, state, city, address, address2, zip_n, phone, fax):
        customer_label = (f"{firstname} {lastname}, " f"{address}, " f"{city}, " f"{state} {zip_n}, " f"{country}")

        # Existing customer may already have saved addresses.
        # Select New Address so that our test data can be entered.
        if self.customer_field.is_visible():
            self.customer_field.select_option(label=customer_label)
        else:
            self.customer_field.select_option(label="New Address")

            self.firstNm_field.fill(firstname)
            self.lastNm_field.fill(lastname)
            self.email_field.fill(email)
            self.company_field.fill(company)
            self.country_list_field.select_option(label=country)
            self.state_list_field.select_option(label=state)
            self.city_field.fill(city)
            self.add1_field.fill(address)
            self.add2_field.fill(address2)
            self.zip_field.fill(zip_n)
            self.phn_field.fill(phone)
            self.fax_field.fill(fax)

        self.continue_link.click()


# Shipping Add Action

    def shipadd_action(self, instore):

        if instore == "True":
            self.instore_radio.check()
        else:
            self.instore_radio.uncheck()

        self.continue2_link.click()

# Shipping Method Action

    def shipmethod_action(self, ship_type):

        if ship_type == "ground":
            self.ground_radio.check()

        elif ship_type == "nextDay":
            self.nextDay_radio.check()

        else:
            self.SndDay_radio.check()

        self.continue3_link.click()

# Payment Method Action

    def paymentmethod_action(self, pay_type):

        if pay_type == "cashOndel":
            self.cash_on_delivery_radio.check()

        elif pay_type == "moneyOrder":
            self.money_order_radio.check()

        elif pay_type == "creditCard":
            self.credit_card_radio.check()

        else:
            self.purchase_order_radio.check()

        self.continue4_link.click()


# Payment Information Action

    def payment_info(self):
        self.continue5_link.click()


#Confirm Action

    def confirm(self):
        self.confirm_link.click()