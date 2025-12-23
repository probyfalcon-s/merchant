from playwright.sync_api import Page, expect


class CreateTransactionPage:
    def __init__(self, page: Page):
        self.page = page
        self.button_create_transaction = page.locator("//span[text()='Создать транзакцию']")
        self.input_client_transaction = page.locator("//input[@id='client']")
        self.input_amount_transaction = page.locator("//input[@id='amount']")
        self.input_address_client_transaction = page.locator("//input[@id='address_client']")
        self.button_create_transaction_end = page.locator("//span[text()='Создать']")


    def click_create_transaction(self):
        self.button_create_transaction.click()

    def enter_client_transaction_input(self, client_transaction):
        self.input_client_transaction.fill(client_transaction)

    def enter_amount_transaction_input(self, amount_transaction):
        self.input_amount_transaction.fill(amount_transaction)


    def click_dropdown_menu_user_transaction(self):
        dropdown = self.page.locator("input#user").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")

        first_item = self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").first
        first_item.click()

    def click_dropdown_menu_network(self):
        dropdown = self.page.locator("input#network").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="BSC").last
        dropdown_link.click()


    def click_dropdown_menu_address(self):
        dropdown = self.page.locator("input#address").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        self.page.locator("div.ant-select-dropdown").highlight()
        self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").highlight()

        first_item = self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").first
        first_item.click()


    def click_dropdown_menu_token(self):
        dropdown = self.page.locator("input#token").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="BNB").last
        dropdown_link.click()


    def click_dropdown_menu_type_transaction(self):
        dropdown = self.page.locator("input#type").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="Вывод").last
        dropdown_link.click()

    def enter_address_client_transaction_input(self, address_client):
        self.input_address_client_transaction.fill(address_client)


    async def click_create_transaction_end(self, custom_page=None):
        await self.button_create_transaction_end.click()

        locator = custom_page.locator('div.ant-notification-notice-message', has_text='Успех')
        await expect(locator).to_be_visible(timeout=3000)

    '''создание транзакции с deposit'''
    def click_dropdown_menu_type_transaction_deposit(self):
        dropdown = self.page.locator("input#type").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="Пополнение").last
        dropdown_link.click()

    '''создание транзакции с deposit, withdrawal usdt'''
    def click_dropdown_menu_token_usdt(self):
        dropdown = self.page.locator("input#token").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="USDT").last
        dropdown_link.click()

