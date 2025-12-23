from playwright.sync_api import Page, expect


class CreateWalletPage:
    def __init__(self, page: Page):
        self.page = page
        self.button_create_wallet = page.locator("//span[text()='Добавить кошелек']")
        self.input_id_user = page.locator("//input[@id='user_id']")
        self.input_address = page.locator("//input[@id='address']")
        self.input_secret_key = page.locator("//input[@id='secret']")
        self.input_type = page.locator("//input[@id='type']")
        self.input_create_wallet_end = page.locator("//span[text()='Создать']")


    def click_create_wallet(self):
        self.button_create_wallet.click()

    def enter_user_id_wallet_input(self, user_id):
         self.input_id_user.fill(user_id)

    def enter_address_wallet_input(self, address_wallet):
         self.input_address.fill(address_wallet)

    def enter_secret_key_wallet_input(self, secret_key):
         self.input_secret_key.fill(secret_key)

    def enter_type_wallet_input(self, type):
         self.input_type.fill(type)


    def click_dropdown_menu_user_wallet(self):
        dropdown = self.page.locator("input#user_id").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")

        first_item = self.page.locator("div.ant-select-dropdown:visible div.ant-select-item-option").first
        first_item.click()

    def click_dropdown_menu_type(self):
        dropdown = self.page.locator("input#type").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="X").last
        dropdown_link.click()

    def click_dropdown_menu_network(self):
        dropdown = self.page.locator("input#network").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="BSC").last
        dropdown_link.click()

    def click_dropdown_menu_direction(self):
        dropdown = self.page.locator("input#direction").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="Внутренний").last
        dropdown_link.click()


    async def click_create_wallet_end(self, custom_page=None):
        await self.input_create_wallet_end.click()

        locator = custom_page.locator('div.ant-notification-notice-message', has_text='Успех')
        await expect(locator).to_be_visible(timeout=3000)

    '''создание кошелька AP'''
    def click_dropdown_menu_type_ap(self):
        dropdown = self.page.locator("input#type").locator("xpath=parent::span")
        dropdown.click()

        self.page.wait_for_selector("div.ant-select-dropdown:visible")
        dropdown_link = self.page.locator("div.ant-select-dropdown:visible div", has_text="AP").last
        dropdown_link.click()

    def click_switch_default_wallet(self):
        switch = self.page.locator(
            "xpath=//label[@for='default' and contains(., 'По умолчанию')]"
            "/following::button[@id='default' and @role='switch']"
        )
        switch.click()

    def click_switch_active_wallet(self):
        switch = self.page.locator(
            "xpath=//label[@for='active' and contains(., 'Активный')]"
            "/following::button[@id='active' and @role='switch']"
        )
        switch.click()


